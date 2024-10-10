import React from 'react';
import { render, fireEvent, within } from '@testing-library/react';
import '@testing-library/jest-dom';
import { MainPage } from './MainPage';
import { useCurrentTime, useProducts } from '../../hooks';
import { productsMock } from '../../types/mocks/productsMock';
import { Category } from '../../types';
import { getPrice } from '../../utils';

jest.mock('../../hooks');
const currentTime = '12:00:00';

describe('MainPage test', () => {
    let rendered: ReturnType<typeof render>;
    let categoryButton: HTMLElement;
    let targetCategories: Category[]; // выбранные категории, которые мы хотим увидеть
    const checkProductCards = () => {
        const productContainer = rendered.getAllByTestId('product_container');
        const filteredProducts = productsMock.filter((product) =>
            targetCategories.includes(product.category)
        );
        const otherProducts = productsMock.filter(
            (product) => !targetCategories.includes(product.category)
        );
        expect(productContainer.length).toEqual(filteredProducts.length);
        // проверяем, что отображаются только продукты из выбранных категорий
        filteredProducts.forEach((product, index) => {
            expect(
                within(productContainer[index]).getByText(product.description)
            ).toBeInTheDocument();
        });
        otherProducts.forEach((product) => {
            expect(rendered.queryByText(product.name)).not.toBeInTheDocument();
        });
    };

    beforeEach(() => {
        jest.mocked(useProducts).mockReturnValue(productsMock);
        jest.mocked(useCurrentTime).mockReturnValue(currentTime);
        rendered = render(<MainPage />);
        const categories = rendered.getByTestId('categories');
        categoryButton = within(categories).getByText(productsMock[1].category);
    });

    afterEach(() => {
        jest.clearAllMocks();
    });

    it('should render correctly', () => {
        expect(rendered.asFragment()).toMatchSnapshot();
    });

    it('should display the current time', () => {
        const timeElement = rendered.getByTestId('current_time');
        expect(timeElement).toHaveTextContent(currentTime);
    });

    it('should display products of the selected category when category is clicked', () => {
        targetCategories = [productsMock[1].category];
        fireEvent.click(categoryButton);
        checkProductCards();
    });

    it('should render ProductCard for everything after unselecting all selected categories', () => {
        targetCategories = [productsMock[0].category, productsMock[1].category];
        fireEvent.click(categoryButton);
        fireEvent.click(categoryButton);
        checkProductCards();
    });
});

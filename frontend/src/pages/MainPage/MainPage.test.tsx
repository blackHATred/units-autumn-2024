import React from 'react';
import { render, fireEvent, act } from '@testing-library/react';
import '@testing-library/jest-dom';
import { MainPage } from './MainPage';
import { useProducts } from '../../hooks';
import { Product } from '../../types';

// Мокаем хуки, которые используются в MainPage
jest.mock('../../hooks', () => ({
    // хук со временем сохраняем, а useProducts мокаем
    ...jest.requireActual('../../hooks'),
    useProducts: jest.fn(),
}));

const products: Product[] = [
    {
        name: 'name',
        description: 'description',
        price: 100,
        priceSymbol: '₽',
        category: 'Электроника',
        imgUrl: 'imgUrl',
        id: 1,
    },
    {
        name: 'name2',
        description: 'description2',
        price: 200,
        priceSymbol: '$',
        category: 'Одежда',
        imgUrl: 'imgUrl2',
        id: 2,
    },
];

describe('MainPage test', () => {
    let setIntervalSpy: jest.SpyInstance;
    let clearIntervalSpy: jest.SpyInstance;

    beforeEach(() => {
        (useProducts as jest.Mock).mockReturnValue(products);

        // мокаем и следим за setInterval и clearInterval
        jest.useFakeTimers();
        setIntervalSpy = jest.spyOn(global, 'setInterval');
        clearIntervalSpy = jest.spyOn(global, 'clearInterval');
        jest.spyOn(global, 'Date').mockImplementation(
            () =>
                ({
                    toLocaleTimeString: () => '12:00:00',
                } as unknown as Date)
        );
    });

    afterEach(() => {
        jest.clearAllTimers();
        setIntervalSpy.mockRestore();
        clearIntervalSpy.mockRestore();
        (global.Date as unknown as jest.Mock).mockRestore();
    });

    it('should display the current time and update every second', () => {
        const { getByText } = render(<MainPage />);

        const initialTime = new Date().toLocaleTimeString('ru-RU');

        // проверяем, что начальное время отображается
        expect(getByText(initialTime)).toBeInTheDocument();

        // прокручиваем время на 1 секунду вперед
        act(() => {
            jest.advanceTimersByTime(1000);
        });

        const updatedTime = new Date().toLocaleTimeString('ru-RU');

        // проверяем, что время обновилось
        expect(getByText(updatedTime)).toBeInTheDocument();
    });

    it('should clear the interval on unmount', () => {
        const { unmount } = render(<MainPage />);

        // проверяем, что setInterval был вызван
        expect(setIntervalSpy).toHaveBeenCalledTimes(1);

        unmount();

        // проверяем, что clearInterval был вызван
        expect(clearIntervalSpy).toHaveBeenCalledTimes(1);
    });

    it('should call callback when category click', () => {
        const rendered = render(<MainPage />);
        // есть 2 элемента с текстом "Одежда": кнопка выбора категории и непосредственно категория на карточке,
        // здесь нужна кнопка выбора категории
        fireEvent.click(rendered.getAllByText('Одежда')[0]);
        // проверяем, что категория была выбрана
        expect(rendered.getByText('name2')).toBeInTheDocument();
    });

    it('should render ProductCard for everything after unselecting all categories', () => {
        const rendered = render(<MainPage />);

        fireEvent.click(rendered.getAllByText('Одежда')[0]);
        fireEvent.click(rendered.getAllByText('Одежда')[0]);
        // проверяем, что все продукты отображаются
        expect(rendered.getByText('name')).toBeInTheDocument();
        expect(rendered.getByText('name2')).toBeInTheDocument();
    });

    it('should render ProductCard for electronics', () => {
        const rendered = render(<MainPage />);

        expect(rendered.getByText('name')).toBeInTheDocument();
        expect(rendered.getByText('description')).toBeInTheDocument();
        expect(rendered.getByText('100 ₽')).toBeInTheDocument();
        expect(rendered.getAllByText('Электроника')[0]).toBeInTheDocument();
        expect(rendered.getByAltText('name')).toBeInTheDocument();
    });

    it('should render ProductCard for clothing', () => {
        const rendered = render(<MainPage />);

        fireEvent.click(rendered.getAllByText('Одежда')[0]);

        expect(rendered.getByText('name2')).toBeInTheDocument();
        expect(rendered.getByText('description2')).toBeInTheDocument();
        expect(rendered.getByText('200 $')).toBeInTheDocument();
        expect(rendered.getAllByText('Одежда')[0]).toBeInTheDocument();
        expect(rendered.getByAltText('name2')).toBeInTheDocument();
    });
});

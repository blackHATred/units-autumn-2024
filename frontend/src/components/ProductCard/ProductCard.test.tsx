import React from 'react';
import { render } from '@testing-library/react';
import '@testing-library/jest-dom';
import { ProductCard } from './ProductCard';

describe('ProductCard test', () => {
    it('should render correctly', () => {
        const rendered = render(
            <ProductCard
                name="name"
                description="description"
                price={100}
                priceSymbol="$"
                category="Электроника"
                imgUrl="imgUrl"
                id={6}
            />
        );

        expect(rendered.asFragment()).toMatchSnapshot();
    });

    it('should render correctly without image', () => {
        const rendered = render(
            <ProductCard
                name="name"
                description="description"
                price={100}
                priceSymbol="$"
                category="Электроника"
                id={6}
            />
        );

        expect(rendered.asFragment()).toMatchSnapshot();
    });

    it('should render correctly without price symbol', () => {
        const rendered = render(
            <ProductCard
                name="name"
                description="description"
                price={100}
                category="Электроника"
                imgUrl="imgUrl"
                id={6}
            />
        );

        expect(rendered.asFragment()).toMatchSnapshot();
    });
});

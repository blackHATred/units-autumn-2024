import React from 'react';
import { render, RenderResult } from '@testing-library/react';
import '@testing-library/jest-dom';
import { ProductCard } from './ProductCard';

describe('ProductCard test', () => {
    let rendered: RenderResult;

    beforeEach(() => {
        rendered = render(
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
    });

    it('should render correctly', () => {
        expect(rendered.asFragment()).toMatchSnapshot();
    });

    it('should render correctly without image', () => {
        rendered = render(
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

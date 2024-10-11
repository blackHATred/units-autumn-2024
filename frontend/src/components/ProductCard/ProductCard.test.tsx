import React from 'react';
import { render, RenderResult } from '@testing-library/react';
import '@testing-library/jest-dom';
import { ProductCard } from './ProductCard';
import { productsMock } from '../../types/mocks/productsMock';

describe('ProductCard test', () => {
    let rendered: RenderResult;

    it('should render correctly', () => {
        rendered = render(<ProductCard {...productsMock[0]} />);
        expect(rendered.asFragment()).toMatchSnapshot();
    });

    it('should render correctly without image', () => {
        rendered = render(<ProductCard {...productsMock[1]} />);
        expect(rendered.asFragment()).toMatchSnapshot();
    });

    it('should render correctly without price symbol', () => {
        rendered = render(<ProductCard {...productsMock[2]} />);
        expect(rendered.asFragment()).toMatchSnapshot();
    });
});

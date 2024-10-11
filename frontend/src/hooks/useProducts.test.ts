import { renderHook } from '@testing-library/react';
import { useProducts } from './useProducts';
import { productsMock } from '../types/mocks/productsMock';

describe('useProducts hook', () => {
    it('should return an array of products', () => {
        const { result } = renderHook(() => useProducts());
        expect(Array.isArray(result.current)).toBe(true);
        expect(result.current.length).toBe(4);
    });

    it('should return products with correct structure', () => {
        const { result } = renderHook(() => useProducts());
        expect(result.current).toEqual(productsMock);
    });

    it('should contain products with necessary fields', () => {
        const { result } = renderHook(() => useProducts());
        result.current.forEach((product) => {
            expect(product).toHaveProperty('id');
            expect(product).toHaveProperty('name');
            expect(product).toHaveProperty('description');
            expect(product).toHaveProperty('price');
            expect(product).toHaveProperty('category');
        });
    });
});

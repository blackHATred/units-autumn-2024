import { renderHook } from '@testing-library/react';
import { useProducts } from './useProducts';
import type { Product } from '../types';

describe('useProducts hook', () => {
    it('should return an array of products', () => {
        const { result } = renderHook(() => useProducts());
        expect(Array.isArray(result.current)).toBe(true);
        expect(result.current.length).toBe(4);
    });

    it('should return products with correct structure', () => {
        const { result } = renderHook(() => useProducts());
        const expectedProducts: Product[] = [
            {
                id: 1,
                name: 'IPhone 14 Pro',
                description: 'Latest iphone, buy it now',
                price: 999,
                priceSymbol: '$',
                category: 'Электроника',
                imgUrl: '/iphone.png',
            },
            {
                id: 2,
                name: 'Костюм гуся',
                description: 'Запускаем гуся, работяги',
                price: 1000,
                priceSymbol: '₽',
                category: 'Одежда',
            },
            {
                id: 3,
                name: 'Настольная лампа',
                description: 'Говорят, что ее использовали в pixar',
                price: 699,
                category: 'Для дома',
                imgUrl: '/lamp.png',
            },
            {
                id: 4,
                name: 'Принтер',
                description: 'Незаменимая вещь для студента',
                price: 7000,
                category: 'Электроника',
            },
        ];
        expect(result.current).toEqual(expectedProducts);
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

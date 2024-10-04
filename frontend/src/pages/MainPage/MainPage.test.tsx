import React from 'react';
import { render, fireEvent, act } from '@testing-library/react';
import '@testing-library/jest-dom';
import { MainPage } from './MainPage';
import { useProducts } from '../../hooks';
import { Product } from '../../types';

// Мокаем хуки, которые используются в MainPage
jest.mock('../../hooks', () => ({
    // хук с временем сохраняем, а useProducts мокаем
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
        jest.useFakeTimers(); // Переключаемся на фейковые таймеры

        // Замокируем глобальные функции setInterval и clearInterval
        setIntervalSpy = jest.spyOn(global, 'setInterval');
        clearIntervalSpy = jest.spyOn(global, 'clearInterval');

        // Мокаем Date и toLocaleTimeString, чтобы вернуть фиксированное время
        jest.spyOn(global, 'Date').mockImplementation(
            () =>
                ({
                    toLocaleTimeString: () => '12:00:00', // Возвращаем фиксированное время
                } as unknown as Date)
        );
    });

    afterEach(() => {
        jest.clearAllTimers(); // Очищаем все таймеры после каждого теста

        // Восстанавливаем оригинальные реализации
        setIntervalSpy.mockRestore();
        clearIntervalSpy.mockRestore();

        // Восстанавливаем оригинальный Date
        (global.Date as unknown as jest.Mock).mockRestore();
    });

    it('should display the current time and update every second', () => {
        // Рендерим MainPage
        const { getByText } = render(<MainPage />);

        const initialTime = new Date().toLocaleTimeString('ru-RU');

        // Проверяем, что начальное время отображается
        expect(getByText(initialTime)).toBeInTheDocument();

        // Прокручиваем время на 1 секунду вперед
        act(() => {
            jest.advanceTimersByTime(1000);
        });

        const updatedTime = new Date().toLocaleTimeString('ru-RU');

        // Проверяем, что время обновилось
        expect(getByText(updatedTime)).toBeInTheDocument();
    });

    it('should clear the interval on unmount', () => {
        const { unmount } = render(<MainPage />);

        // Проверяем, что setInterval был вызван
        expect(setIntervalSpy).toHaveBeenCalledTimes(1);

        // Размонтируем компонент
        unmount();

        // Проверяем, что clearInterval был вызван при размонтировании
        expect(clearIntervalSpy).toHaveBeenCalledTimes(1);
    });

    it('should render correctly', () => {
        const rendered = render(<MainPage />);

        expect(rendered.asFragment()).toMatchSnapshot();
    });

    it('should call callback when category click', () => {
        const rendered = render(<MainPage />);

        fireEvent.click(rendered.getAllByText('Одежда')[0]);
        // Проверяем, что категория была выбрана
        expect(rendered.getByText('name2')).toBeInTheDocument();
    });

    it('should render ProductCard for everything after unselecting all categories', () => {
        const rendered = render(<MainPage />);

        fireEvent.click(rendered.getAllByText('Одежда')[0]);
        fireEvent.click(rendered.getAllByText('Одежда')[0]);
        // Проверяем, что все продукты отображаются
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

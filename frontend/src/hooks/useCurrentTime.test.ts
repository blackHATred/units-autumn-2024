import { renderHook, act } from '@testing-library/react';
import { useCurrentTime } from './useCurrentTime';

// юзаем fake таймеры
jest.useFakeTimers();

describe('useCurrentTime hook', () => {
    afterEach(() => {
        jest.clearAllMocks();
    });

    it('should return current time initially', () => {
        const mockTime = '12:00:00';

        // мокаем метод toLocaleTimeString у прототипа Date
        jest.spyOn(Date.prototype, 'toLocaleTimeString').mockReturnValue(
            mockTime
        );

        const { result } = renderHook(() => useCurrentTime());
        expect(result.current).toBe(mockTime);
    });

    it('should update time every second', () => {
        const initialTime = '12:00:00';
        const updatedTime = '12:00:01';

        // мокаем два разных значения для toLocaleTimeString
        const toLocaleTimeStringMock = jest.spyOn(
            Date.prototype,
            'toLocaleTimeString'
        );
        toLocaleTimeStringMock
            .mockReturnValueOnce(initialTime)
            .mockReturnValueOnce(updatedTime);

        const { result } = renderHook(() => useCurrentTime());

        expect(result.current).toBe(initialTime);
        act(() => {
            jest.advanceTimersByTime(1000); // мотаем таймер на 1 секунду
        });
        expect(result.current).toBe(updatedTime);
    });

    it('should clear interval on unmount', () => {
        const clearIntervalSpy = jest.spyOn(global, 'clearInterval');
        const { unmount } = renderHook(() => useCurrentTime());
        unmount();
        expect(clearIntervalSpy).toHaveBeenCalled(); // должен был быть вызван clearInterval
    });
});

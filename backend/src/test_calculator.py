import math
import unittest
from src.calculator import Calculator


class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    def test_add(self):
        """
        Тестирование метода сложения
        """
        # Сложение integer
        self.assertEqual(self.calculator.addition(1, 2), 3)
        # Сложение float
        self.assertEqual(self.calculator.addition(0.2, 0.2), 0.4)
        # Сложение отрицательных чисел
        self.assertEqual(self.calculator.addition(-1, -2.1), -3.1)
        # Сложение 0
        self.assertEqual(self.calculator.addition(0, 0), 0)
        # Сложение огромных чисел
        self.assertEqual(self.calculator.addition(100**100, 100**100), 2 * 100**100)
        # Неверный (не численный) тип данных в аргументе
        self.assertRaises(TypeError, self.calculator.addition, 1, 'a')
        # Сложение бесконечностей
        self.assertEqual(self.calculator.addition(float('inf'), float('inf')), float('inf'))
        # Сложение числа и бесконечности
        self.assertEqual(self.calculator.addition(1, float('inf')), float('inf'))
        # Сложение минус бесконечности и бесконечности не определено в математике
        self.assertTrue(math.isnan(self.calculator.addition(-float('inf'), float('inf'))))
        # Сложение комплексных чисел
        self.assertEqual(self.calculator.addition(1 + 1j, 1 + 1j), 2 + 2j)

    def test_multiply(self):
        """
        Тестирование метода умножения
        """
        # Умножение integer
        self.assertEqual(self.calculator.multiplication(1, 2), 2)
        # Умножение float
        self.assertEqual(self.calculator.multiplication(0.2, 2), 0.4)
        # Умножение отрицательных чисел
        self.assertEqual(self.calculator.multiplication(-1, -2.1), 2.1)
        # Умножение на 0
        self.assertEqual(self.calculator.multiplication(10, 0), 0)
        # Умножение на 1
        self.assertEqual(self.calculator.multiplication(10, 1), 10)
        # Умножение на -1
        self.assertEqual(self.calculator.multiplication(1, -1), -1)
        # Умножение на бесконечность
        self.assertEqual(self.calculator.multiplication(1, float('inf')), float('inf'))
        # Умножение бесконечности на 0 не определено в математике
        self.assertTrue(math.isnan(self.calculator.multiplication(float('inf'), 0)))
        # Умножение минус бесконечности на бесконечность
        self.assertEqual(self.calculator.multiplication(-float('inf'), float('inf')), -float('inf'))
        # Умножение на комплексное число
        self.assertEqual(self.calculator.multiplication(1, 1 + 1j), 1 + 1j)
        # Неверный (не численный) тип данных в аргументе
        self.assertRaises(TypeError, self.calculator.multiplication, 'a', 'a')
        # Умножение бесконечностей
        self.assertEqual(self.calculator.multiplication(float('inf'), float('inf')), float('inf'))

    def test_subtract(self):
        """
        Тестирование метода вычитания
        """
        # Вычитание integer
        self.assertEqual(self.calculator.subtraction(1, 2), -1)
        # Вычитание float
        self.assertEqual(self.calculator.subtraction(0.2, 0.2), 0)
        # Вычитание отрицательных чисел
        self.assertEqual(self.calculator.subtraction(-1, -2.1), 1.1)
        # Вычитание 0
        self.assertEqual(self.calculator.subtraction(1, 0), 1)
        # Вычитание огромных чисел
        self.assertEqual(self.calculator.subtraction(100**100, 100**100), 0)
        # Неверный (не численный) тип данных в аргументе
        self.assertRaises(TypeError, self.calculator.subtraction, 1, 'a')
        # Вычитание числа из бесконечности
        self.assertEqual(self.calculator.subtraction(float('inf'), 1), float('inf'))
        # Вычитание бесконечности из бесконечности не определено в математике
        self.assertTrue(math.isnan(self.calculator.subtraction(float('inf'), float('inf'))))
        # Вычитание комплексных чисел
        self.assertEqual(self.calculator.subtraction(1 + 1j, 1 + 1j), 0 + 0j)

    def test_divide(self):
        """
        Тестирование метода деления
        """
        # Деление integer
        self.assertEqual(self.calculator.division(1, 2), 0.5)
        # Деление float
        self.assertEqual(self.calculator.division(0.2, 0.2), 1)
        # Деление отрицательных чисел
        self.assertEqual(self.calculator.division(-1, -2.1), 0.47619047619047616)
        # Деление на 0
        self.assertIsNone(self.calculator.division(1, 0))
        # Деление 0 на число
        self.assertEqual(self.calculator.division(0, 1), 0)
        # Деление числа на бесконечность
        self.assertEqual(self.calculator.division(1, float('inf')), 0)
        # Деление бесконечности на число
        self.assertEqual(self.calculator.division(float('inf'), 1), float('inf'))
        # Деление комплексных чисел
        self.assertEqual(self.calculator.division(1 + 1j, 1 + 1j), 1 + 0j)
        # Неверный (не численный) тип данных в аргументе
        self.assertRaises(TypeError, self.calculator.division, 1, 'a')
        # Деление бесконечностей не определено в математике
        self.assertTrue(math.isnan(self.calculator.division(float('inf'), float('inf'))))

    def test_abs(self):
        """
        Тестирование метода модуля числа
        """
        # Модуль integer
        self.assertEqual(self.calculator.absolute(1), 1)
        # Модуль float
        self.assertEqual(self.calculator.absolute(-0.2), 0.2)
        # Модуль отрицательного числа
        self.assertEqual(self.calculator.absolute(-1), 1)
        # Модуль 0
        self.assertEqual(self.calculator.absolute(0), 0)
        # Модуль бесконечности
        self.assertEqual(self.calculator.absolute(float('inf')), float('inf'))
        # Неверный (не численный) тип данных в аргументе
        self.assertRaises(TypeError, self.calculator.absolute, 'a')
        # Модуль комплексного числа
        self.assertEqual(self.calculator.absolute(1 + 1j), 1.4142135623730951)

    def test_degree(self):
        """
        Тестирование метода возведения в степень
        """
        # Возведение в степень integer
        self.assertEqual(self.calculator.degree(2, 3), 8)
        # Возведение в степень float
        self.assertEqual(self.calculator.degree(2.5, 2), 6.25)
        # Возведение в степень отрицательного числа
        self.assertEqual(self.calculator.degree(-2, 2), 4)
        # Возведение в степень 0
        self.assertEqual(self.calculator.degree(0, 2), 0)
        # Возведение в степень 1
        self.assertEqual(self.calculator.degree(2, 1), 2)
        # Возведение в степень 0
        self.assertEqual(self.calculator.degree(2, 0), 1)
        # Возведение в степень бесконечности
        self.assertEqual(self.calculator.degree(2, float('inf')), float('inf'))
        # Неверный (не численный) тип данных в аргументе
        self.assertRaises(TypeError, self.calculator.degree, 1, 'a')
        # Возведение в степень комплексного числа
        self.assertEqual(self.calculator.degree(1 + 1j, 2), 2j)

    def test_ln(self):
        """
        Тестирование метода натурального логарифма
        """
        # Натуральный логарифм integer
        self.assertEqual(self.calculator.ln(1), 0)
        # Натуральный логарифм float
        self.assertAlmostEqual(self.calculator.ln(2.718281828459045), 1)
        # Натуральный логарифм отрицательного числа
        self.assertRaises(ValueError, self.calculator.ln, -1)
        # Натуральный логарифм 0
        self.assertRaises(ValueError, self.calculator.ln, 0)
        # Натуральный логарифм бесконечности
        self.assertEqual(self.calculator.ln(float('inf')), float('inf'))
        # Неверный (не численный) тип данных в аргументе
        self.assertRaises(TypeError, self.calculator.ln, 'a')
        # Натуральный логарифм комплексного числа
        self.assertRaises(TypeError, self.calculator.ln, 1 + 1j)

    def test_log(self):
        """
        Тестирование метода логарифма
        """
        # Логарифм integer
        self.assertEqual(self.calculator.log(1, 10), 0)
        # Логарифм float
        self.assertEqual(self.calculator.log(100, 10), 2)
        # Логарифм отрицательного числа
        self.assertRaises(ValueError, self.calculator.log, -1, 10)
        # Логарифм 0
        self.assertRaises(ValueError, self.calculator.log, 0, 10)
        # Логарифм бесконечности
        self.assertEqual(self.calculator.log(float('inf'), 10), float('inf'))
        # Неверный (не численный) тип данных в аргументе
        self.assertRaises(TypeError, self.calculator.log, 'a', 10)
        # Логарифм комплексного числа
        self.assertRaises(TypeError, self.calculator.log, 1 + 1j, 10)

    def test_sqrt(self):
        """
        Тестирование метода квадратного корня
        """
        # Квадратный корень integer
        self.assertEqual(self.calculator.sqrt(1), 1)
        # Квадратный корень float
        self.assertEqual(self.calculator.sqrt(4), 2)
        # Квадратный корень отрицательного числа это мнимая единица
        self.assertAlmostEqual(self.calculator.sqrt(-1), 1j)
        # Квадратный корень 0
        self.assertEqual(self.calculator.sqrt(0), 0)
        # Квадратный корень бесконечности
        self.assertEqual(self.calculator.sqrt(float('inf')), float('inf'))
        # Неверный (не численный) тип данных в аргументе
        self.assertRaises(TypeError, self.calculator.sqrt, 'a')
        # Квадратный корень комплексного числа
        self.assertAlmostEqual(self.calculator.sqrt(1 + 1j), 1.09868411346781 + 0.45508986056222733j)

    def test_nth_root(self):
        """
        Тестирование метода корня n-ой степени
        """
        # Корень n-ой степени integer
        self.assertEqual(self.calculator.nth_root(1, 2), 1)
        # Корень n-ой степени float
        self.assertEqual(self.calculator.nth_root(27, 3), 3)
        # Корень n-ой степени отрицательного числа это комплексное число
        self.assertAlmostEqual(self.calculator.nth_root(-1, 3), 0.5 + 0.8660254037844386j)
        # Корень n-ой степени 0
        self.assertEqual(self.calculator.nth_root(0, 2), 0)
        # Корень n-ой степени бесконечности
        self.assertEqual(self.calculator.nth_root(float('inf'), 2), float('inf'))
        # Неверный (не численный) тип данных в аргументе
        self.assertRaises(TypeError, self.calculator.nth_root, 'a', 2)
        # Корень n-ой степени комплексного числа это комплексное число
        self.assertAlmostEqual(self.calculator.nth_root(1 + 1j, 2), 1.09868411346781 + 0.45508986056222733j)


if __name__ == "__main__":
    unittest.main()

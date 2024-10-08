import math
import unittest
from src.calculator import Calculator


class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    """
    Тесты для сложения
    """

    def test_add_integers(self):
        self.assertEqual(self.calculator.addition(1, 2), 3)

    def test_add_floats(self):
        self.assertEqual(self.calculator.addition(2.2, 2.2), 4.4)

    def test_add_negative_numbers(self):
        self.assertEqual(self.calculator.addition(-1, -2.1), -3.1)

    def test_add_zeros(self):
        self.assertEqual(self.calculator.addition(0, 0), 0)

    def test_add_huge_numbers(self):
        self.assertEqual(self.calculator.addition(100**100, 100**100), 2 * 100**100)

    def test_add_wrong_type(self):
        self.assertRaises(TypeError, self.calculator.addition, 1, 'a')

    def test_add_positive_infinities(self):
        # Положительная бесконечность
        self.assertEqual(self.calculator.addition(float('inf'), float('inf')), float('inf'))

    def test_add_const_to_inf(self):
        self.assertEqual(self.calculator.addition(1, float('inf')), float('inf'))

    def test_add_minus_inf_to_inf(self):
        self.assertTrue(math.isnan(self.calculator.addition(-float('inf'), float('inf'))))

    def test_add_complex_numbers(self):
        self.assertEqual(self.calculator.addition(1 + 1j, 1 + 1j), 2 + 2j)

    """
    Тесты для умножения
    """

    def test_multiply_integers(self):
        self.assertEqual(self.calculator.multiplication(1, 2), 2)

    def test_multiply_floats(self):
        self.assertEqual(self.calculator.multiplication(0.2, 2), 0.4)

    def test_multiply_negative_numbers(self):
        self.assertEqual(self.calculator.multiplication(-1, -2.1), 2.1)

    def test_multiply_zeros(self):
        self.assertEqual(self.calculator.multiplication(10, 0), 0)

    def test_multiply_ones(self):
        self.assertEqual(self.calculator.multiplication(10, 1), 10)

    def test_multiply_minus_one(self):
        self.assertEqual(self.calculator.multiplication(1, -1), -1)

    def test_multiply_int_by_inf(self):
        self.assertEqual(self.calculator.multiplication(1, float('inf')), float('inf'))

    def test_multiply_inf_by_zero(self):
        self.assertTrue(math.isnan(self.calculator.multiplication(float('inf'), 0)))

    def test_multiply_minus_inf_by_inf(self):
        self.assertEqual(self.calculator.multiplication(-float('inf'), float('inf')), -float('inf'))

    def test_multiply_complex_numbers(self):
        self.assertEqual(self.calculator.multiplication(1, 1 + 1j), 1 + 1j)

    def test_multiply_wrong_type(self):
        self.assertRaises(TypeError, self.calculator.multiplication, 'a', 'a')

    """
    Тесты для вычитания
    """

    def test_subtract_integers(self):
        self.assertEqual(self.calculator.subtraction(1, 2), -1)

    def test_subtract_floats(self):
        self.assertEqual(self.calculator.subtraction(0.2, 0.2), 0)

    def test_subtract_negative_numbers(self):
        self.assertEqual(self.calculator.subtraction(-1, -2.1), 1.1)

    def test_subtract_zeros(self):
        self.assertEqual(self.calculator.subtraction(1, 0), 1)

    def test_subtract_huge_numbers(self):
        self.assertEqual(self.calculator.subtraction(100**100, 100**100), 0)

    def test_subtract_wrong_type(self):
        self.assertRaises(TypeError, self.calculator.subtraction, 1, 'a')

    def test_subtract_int_from_inf(self):
        self.assertEqual(self.calculator.subtraction(float('inf'), 1), float('inf'))

    def test_subtract_inf_from_inf(self):
        self.assertTrue(math.isnan(self.calculator.subtraction(float('inf'), float('inf'))))

    def test_subtract_complex_numbers(self):
        self.assertEqual(self.calculator.subtraction(1 + 1j, 1 + 1j), 0 + 0j)

    """
    Тесты для деления
    """

    def test_divide_integers(self):
        self.assertEqual(self.calculator.division(1, 2), 0.5)

    def test_divide_floats(self):
        self.assertEqual(self.calculator.division(0.2, 0.2), 1)

    def test_divide_negative_numbers(self):
        self.assertAlmostEqual(self.calculator.division(-1, -2.1), 0.47619047619047616)

    def test_divide_by_zero(self):
        self.assertIsNone(self.calculator.division(1, 0))

    def test_divide_zero_by_number(self):
        self.assertEqual(self.calculator.division(0, 1), 0)

    def test_divide_number_by_infinity(self):
        self.assertEqual(self.calculator.division(1, float('inf')), 0)

    def test_divide_infinity_by_number(self):
        self.assertEqual(self.calculator.division(float('inf'), 1), float('inf'))

    def test_divide_complex_numbers(self):
        self.assertEqual(self.calculator.division(1 + 1j, 1 + 1j), 1 + 0j)

    def test_divide_wrong_type(self):
        self.assertRaises(TypeError, self.calculator.division, 1, 'a')

    def test_divide_infinities(self):
        self.assertTrue(math.isnan(self.calculator.division(float('inf'), float('inf'))))

    """
    Тесты для модуля
    """

    def test_abs_integers(self):
        self.assertEqual(self.calculator.absolute(1), 1)

    def test_abs_floats(self):
        self.assertEqual(self.calculator.absolute(-0.2), 0.2)

    def test_abs_negative_numbers(self):
        self.assertEqual(self.calculator.absolute(-1), 1)

    def test_abs_zero(self):
        self.assertEqual(self.calculator.absolute(0), 0)

    def test_abs_infinity(self):
        self.assertEqual(self.calculator.absolute(-float('inf')), float('inf'))

    def test_abs_wrong_type(self):
        self.assertRaises(TypeError, self.calculator.absolute, 'a')

    def test_abs_complex_numbers(self):
        self.assertAlmostEqual(self.calculator.absolute(1 + 1j), 1.4142135623730951)

    """
    Тесты для возведения в степень
    """

    def test_degree_integers(self):
        self.assertEqual(self.calculator.degree(2, 3), 8)

    def test_degree_floats(self):
        self.assertEqual(self.calculator.degree(2.5, 2), 6.25)

    def test_degree_negative_numbers(self):
        self.assertEqual(self.calculator.degree(-2, 2), 4)

    def test_degree_zero(self):
        self.assertEqual(self.calculator.degree(0, 2), 0)

    def test_degree_one(self):
        self.assertEqual(self.calculator.degree(2, 1), 2)

    def test_degree_zero_degree(self):
        self.assertEqual(self.calculator.degree(2, 0), 1)

    def test_degree_integer_by_infinity(self):
        self.assertEqual(self.calculator.degree(2, float('inf')), float('inf'))

    def test_degree_infinity_by_zero(self):
        self.assertEqual(self.calculator.degree(float('inf'), 0), 1)

    def test_degree_infinity_by_negative(self):
        self.assertEqual(self.calculator.degree(float('inf'), -1), 0)

    def test_degree_wrong_type(self):
        self.assertRaises(TypeError, self.calculator.degree, 1, 'a')

    def test_degree_complex_numbers(self):
        self.assertEqual(self.calculator.degree(1 + 1j, 2), 2j)

    """
    Тесты для натурального логарифма
    """

    def test_ln_integers(self):
        self.assertEqual(self.calculator.ln(1), 0)

    def test_ln_floats(self):
        self.assertEqual(self.calculator.ln(math.e), 1)

    def test_ln_negative_numbers(self):
        self.assertRaises(ValueError, self.calculator.ln, -1)

    def test_ln_zero(self):
        self.assertRaises(ValueError, self.calculator.ln, 0)

    def test_ln_infinity(self):
        self.assertEqual(self.calculator.ln(float('inf')), float('inf'))

    def test_ln_wrong_type(self):
        self.assertRaises(TypeError, self.calculator.ln, 'a')

    def test_ln_complex_numbers(self):
        self.assertRaises(TypeError, self.calculator.ln, 1 + 1j)

    """
    Тесты для логарифма с произвольным основанием
    """

    def test_log_integers(self):
        self.assertEqual(self.calculator.log(1, 10), 0)

    def test_log_floats(self):
        self.assertEqual(self.calculator.log(100., 10.), 2)

    def test_log_negative_numbers(self):
        self.assertRaises(ValueError, self.calculator.log, -1, 10)

    def test_log_zero(self):
        self.assertRaises(ValueError, self.calculator.log, 0, 10)

    def test_log_infinity(self):
        self.assertEqual(self.calculator.log(float('inf'), 10), float('inf'))

    def test_log_wrong_type(self):
        self.assertRaises(TypeError, self.calculator.log, 'a', 10)

    def test_log_complex_numbers(self):
        self.assertRaises(TypeError, self.calculator.log, 1 + 1j, 10)

    """
    Тесты для квадратного корня
    """

    def test_sqrt_integers(self):
        self.assertEqual(self.calculator.sqrt(1), 1)

    def test_sqrt_floats(self):
        self.assertEqual(self.calculator.sqrt(4.), 2)

    def test_sqrt_negative_numbers(self):
        self.assertAlmostEqual(self.calculator.sqrt(-1), 1j)

    def test_sqrt_zero(self):
        self.assertEqual(self.calculator.sqrt(0), 0)

    def test_sqrt_infinity(self):
        self.assertEqual(self.calculator.sqrt(float('inf')), float('inf'))

    def test_sqrt_wrong_type(self):
        self.assertRaises(TypeError, self.calculator.sqrt, 'a')

    def test_sqrt_complex_numbers(self):
        self.assertAlmostEqual(self.calculator.sqrt(1 + 1j), 1.09868411346781 + 0.45508986056222733j)

    """
    Тесты для корня произвольной степени
    """

    def test_nth_root_integers(self):
        self.assertEqual(self.calculator.nth_root(1, 2), 1)

    def test_nth_root_floats(self):
        self.assertEqual(self.calculator.nth_root(27., 3.), 3)

    def test_nth_root_negative_numbers(self):
        self.assertAlmostEqual(self.calculator.nth_root(-1, 3), 0.5 + 0.8660254037844386j)

    def test_nth_root_zero(self):
        self.assertEqual(self.calculator.nth_root(0, 2), 0)

    def test_nth_root_infinity(self):
        self.assertEqual(self.calculator.nth_root(float('inf'), 2), float('inf'))

    def test_nth_root_wrong_type(self):
        self.assertRaises(TypeError, self.calculator.nth_root, 'a', 2)

    def test_nth_root_complex_numbers(self):
        self.assertAlmostEqual(self.calculator.nth_root(1 + 1j, 2), 1.09868411346781 + 0.45508986056222733j)


if __name__ == "__main__":
    unittest.main()

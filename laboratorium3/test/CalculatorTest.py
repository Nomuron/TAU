import unittest

from laboratorium3.src.Calculator import add, divide, subtract, multiply


class MyTestCase(unittest.TestCase):

    def test_correctly_add_positive_numbers(self):
        num1, num2 = 1, 3
        self.assertEqual(4, add(num1, num2))

    def test_correctly_add_negative_numbers(self):
        num1, num2 = -7, -4
        self.assertEqual(-11, add(num1, num2))

    def test_adding_whole_numbers_return_int_type(self):
        num1, num2 = 3, 5
        self.assertIs(type(1), type(add(num1, num2)))

    def test_adding_fractional_numbers_return_float_type(self):
        num1, num2 = 3.5, 5
        self.assertIs(type(1.3), type(add(num1, num2)))

    def test_adding_fractional_numbers_doesnt_return_string_type(self):
        num1, num2 = 3.5, 5
        self.assertIsNot(type('a'), type(add(num1, num2)))

    def test_adding_positive_and_negative_same_number_result_in_zero(self):
        num1, num2 = -4, 4
        self.assertEqual(0, add(num1, num2))

    def test_add_string_param(self):
        num1, num2 = 1, "2"
        self.assertRaises(TypeError, add, num1, num2)

    def test_subtracting_from_negative_will_add(self):
        num1, num2 = 1, -3
        self.assertNotEqual(-4, subtract(num1, num2))

    def test_subtracting_zero_from_number(self):
        num1, num2 = 3, 0
        self.assertEqual(num1, subtract(num1, num2))

    def test_multiplication_by_zero_will_be_zero(self):
        num1 = 0
        nums_list = range(6)
        result_list = [multiply(num, num1) for num in nums_list]
        self.assertEqual(0, sum(result_list))

    def test_divide_by_zero(self):
        num1, num2 = 1, 0
        self.assertRaises(ZeroDivisionError, divide, num1, num2)

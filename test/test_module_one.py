import unittest
from src.module_one import addition


class TestMainFunction(unittest.TestCase):

    def test_addition_integer(self):
        result = addition(1, 2)
        self.assertEqual(result, 3)

    def test_addition_float(self):
        result = addition(-10.05, 1)
        self.assertEqual(result, -9.05)

    def test_addition_string_integer(self):
        with self.assertRaises(TypeError):
            addition('a', 'b')
        with self.assertRaises(TypeError):
            addition(123, 'b')

    def test_addition_list_integer(self):
        with self.assertRaises(TypeError):
            addition(1, [1])
        with self.assertRaises(TypeError):
            addition([1], [1])

    def test_addition_set_integer(self):
        with self.assertRaises(TypeError):
            addition(1, {1})
        with self.assertRaises(TypeError):
            addition({1}, {1})


if __name__ == '__main__':
    unittest.main()

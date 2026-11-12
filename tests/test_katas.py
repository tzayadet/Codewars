import unittest

from even_or_odd import even_or_odd
from hello_name_or_world import hello
from make_upper_case import make_upper_case
from multiply import multiply
from quarter_of_the_year import quarter_of


class KataTests(unittest.TestCase):
    def test_even_or_odd(self):
        self.assertEqual(even_or_odd(4), "Even")
        self.assertEqual(even_or_odd(7), "Odd")
        self.assertEqual(even_or_odd(-2), "Even")

    def test_hello(self):
        self.assertEqual(hello(), "Hello, World!")
        self.assertEqual(hello("tzayadet"), "Hello, Tzayadet!")

    def test_uppercase(self):
        self.assertEqual(make_upper_case("Hello, world!"), "HELLO, WORLD!")

    def test_multiply(self):
        self.assertEqual(multiply(6, 7), 42)
        self.assertEqual(multiply(-3, 4), -12)

    def test_quarter_of_year(self):
        self.assertEqual([quarter_of(m) for m in (1, 3, 4, 6, 7, 9, 10, 12)],
                         [1, 1, 2, 2, 3, 3, 4, 4])

    def test_quarter_rejects_invalid_month(self):
        for month in (0, 13, -1):
            with self.subTest(month=month):
                with self.assertRaises(ValueError):
                    quarter_of(month)


if __name__ == "__main__":
    unittest.main()

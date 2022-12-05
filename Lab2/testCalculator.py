import unittest
from calculator import Calculator
from calculator import BadFirstArg, BadSecondArg, BadOperation


class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()

    def test_set_first_arg(self):
        self.assertEqual(self.calculator.set_first_arg(3), 3)
        self.assertEqual(self.calculator.set_first_arg(True), 1)
        self.assertEqual(self.calculator.set_first_arg(-3), -3)
        self.assertEqual(self.calculator.set_first_arg(3.25), 3.25)
        with self.assertRaises(BadFirstArg):
            self.calculator.set_first_arg("hey")

    def test_set_second_arg(self):
        self.assertEqual(self.calculator.set_first_arg(3), 3)
        self.assertEqual(self.calculator.set_first_arg(True), 1)
        self.assertEqual(self.calculator.set_first_arg(-3), -3)
        self.assertEqual(self.calculator.set_first_arg(3.25), 3.25)
        with self.assertRaises(BadSecondArg):
            self.calculator.set_second_arg("hey")

    def test_set_operation(self):
        self.assertEqual(self.calculator.set_operation("+"), "+")
        self.assertEqual(self.calculator.set_operation("-"), "-")
        self.assertEqual(self.calculator.set_operation("*"), "*")
        self.assertEqual(self.calculator.set_operation("/"), "/")
        with self.assertRaises(BadOperation):
            self.calculator.set_operation("hey")

    def test_sum(self):
        self.calculator.set_first_arg(3)
        self.calculator.set_second_arg(4)
        self.calculator.set_operation("+")
        self.assertEqual(self.calculator.sum(), 7)

        self.calculator.set_first_arg(6.57)
        self.calculator.set_second_arg(2.35)
        self.assertEqual(self.calculator.sum(), 8.92)

    def test_sub(self):
        self.calculator.set_first_arg(4)
        self.calculator.set_second_arg(3)
        self.assertEqual(self.calculator.sub(), 1)

        self.calculator.set_first_arg(6.57)
        self.calculator.set_second_arg(2.35)
        self.assertEqual(self.calculator.sub(), 4.22)

    def test_mul(self):
        self.calculator.set_first_arg(4)
        self.calculator.set_second_arg(3)
        self.assertEqual(self.calculator.mul(), 12)

        self.calculator.set_first_arg(6.57)
        self.calculator.set_second_arg(2.35)
        self.assertEqual(self.calculator.mul(), 15.4395)

    def test_div(self):
        self.calculator.set_first_arg(9)
        self.calculator.set_second_arg(3)
        self.assertEqual(self.calculator.div(), 3)

        self.calculator.set_first_arg(6.57)
        self.calculator.set_second_arg(2.35)
        self.assertEqual(self.calculator.div(), 2.79574468085106)

        self.calculator.set_first_arg(23)
        self.calculator.set_second_arg(0)
        with self.assertRaises(ZeroDivisionError):
            self.calculator.div()


if __name__ == '__main__':
    unittest.main()

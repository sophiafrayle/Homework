import unittest
from main import pin, withdraw


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)

    lass
    AtmTest(unittest.TestCase):

    def test_correct_amount(self):
        expected = 100  # withdraw de 70.50
        result = withdraw(70.5)
        self.assertEqual(expected, result)

    def invalid_error(self):
        expected = 1
        result = withdraw(1 / 0)
        self.assertEqual(expected, result)

    def incorrect_amount(self):
        expected = 50.00
        result = withdraw(60)
        self.assertEqual(expected, result)

    def greater_withdraw(self):
        expected = -10
        result = withdraw(110)
        self.assertEqual(expected, result)

    def invalid_data_type(selfS):
        expected = 100
        result = withdraw('0')
        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()

    pass


if __name__ == '__main__':
    unittest.main()
    pass
import unittest
from operations import add, subtract, divide

class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(-1, -1), -2)
        self.assertEqual(add(0, 0), 0)

    def test_subtract(self):
        self.assertEqual(subtract(5, 2), 3)
        self.assertEqual(subtract(-1, 1), -2)
        self.assertEqual(subtract(-1, -1), 0)
        self.assertEqual(subtract(0, 0), 0)

    def test_divide(self):
        self.assertEqual(divide(6, 2), 3)
        self.assertEqual(divide(-4, 2), -2)
        self.assertEqual(divide(-4, -2), 2)
        self.assertEqual(divide(0, 5), 0)
        self.assertEqual(divide(5, 0), 'Error: Cannot divide by zero')

if __name__ == "__main__":
    unittest.main()

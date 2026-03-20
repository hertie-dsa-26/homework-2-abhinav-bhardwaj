import unittest
from circle import Circle
import math

class TestCircle(unittest.TestCase):

    def test_perimeter(self):
        c = Circle(1)
        expected = 2 * math.pi * 1
        self.assertAlmostEqual(c.perimeter(), expected, places=5)

        c2 = Circle(5.5)
        expected2 = 2 * math.pi * 5.5
        self.assertAlmostEqual(c2.perimeter(), expected2, places=5)

    def test_area(self):
        c = Circle(1)
        expected = math.pi * (1 ** 2)
        self.assertAlmostEqual(c.area(), expected, places=5)

        c2 = Circle(5.5)
        expected2 = math.pi * (5.5 ** 2)
        self.assertAlmostEqual(c2.area(), expected2, places=5)

if __name__ == "__main__":
    unittest.main()
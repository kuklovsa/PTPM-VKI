import unittest
import sys
import os

from src.main import get_triangle_vertices
from src.Delivery import calculate_delivery_cost

class Test_Delivery (unittest.TestCase):
    def test_1(self):
        res = 205, "2026-09-04"
        self.assertEqual(calculate_delivery_cost(0.1, 1, "обычный", False), res)

    def test_2(self):
        res = 37800, "2026-09-13"
        self.assertEqual(
            calculate_delivery_cost(50.0, 5000, "обычный", False), res
        )

    def test_3(self):
        res = 840, "2026-09-04"
        self.assertEqual(calculate_delivery_cost(5.0, 100, "обычный", False), res)

    def test_4(self):
        res = 1050, "2026-09-04"
        self.assertEqual(calculate_delivery_cost(20.0, 100, "обычный", False), res)


    def test_5(self):
        res = 700, "2026-09-04"
        self.assertEqual(calculate_delivery_cost(1.0, 100, "  обычный  ", False), res)

    def test_6(self):
        res = -1, "0000-00-00"
        self.assertEqual(calculate_delivery_cost(600, 5, "обычный", True), res)

    def test_7(self):
        res = -1, "0000-00-00"
        self.assertEqual(calculate_delivery_cost(35, 4999, "хрупкий___", False), res)

    def test_8(self):
        res = 56688, "2026-09-07"
        self.assertEqual(calculate_delivery_cost(35, 4999, "обычный", True), res)

    def test_9(self):
        res = 3700, "2026-09-04"
        self.assertEqual(calculate_delivery_cost(2, 500, "опасный", False), res)

    def test_10(self):
        res = 9540, "2026-09-04"
        self.assertEqual(calculate_delivery_cost(15, 1500, "хрупкий", False), res)

if __name__ == "__main__":
  unittest.main()
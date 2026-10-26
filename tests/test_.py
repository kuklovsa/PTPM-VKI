import unittest
import sys
import os

from src.main import get_triangle_vertices
from src.Delivery import calculate_delivery_cost

class Test_TragleCalc (unittest.TestCase):
    def test_1(self):
        res = "разносторонний", (0.0, 0.0),   (5.0, 0.0),   (3.2, 2.3999999999999995)
        self.assertEqual(get_triangle_vertices(3, 4, 5), res)

    def test_2(self):
        res = "равносторонний",   (0.0, 0.0),   (15.0, 0.0),   (7.5, 12.990381056766578)
        self.assertEqual(get_triangle_vertices(15, 15, 15), res)

    def test_3(self):
        res = "равнобедренный",  (0.0, 0.0) ,  (1346.0, 0.0) ,  (770.2106240713225, 1103.853067472145)
        self.assertEqual(get_triangle_vertices(1245, 1346, 1346), res)

    def test_4(self):
        res = "не треугольник",  (-1, -1) ,  (-1, -1) ,  (-1, -1)
        self.assertEqual(get_triangle_vertices(1, 2, 3), res)

    def test_5(self):
        res = "не треугольник",  (-2, -2) ,  (-2, -2) ,  (-2, -2)
        self.assertEqual(get_triangle_vertices("bf", 4, 5), res)

    def test_6(self):
        res = -1, "0000-00-00"
        self.assertEqual(calculate_delivery_cost(600, 5, "обычный", True), res)

    def test_7(self):
        res = -1, "0000-00-00"
        self.assertEqual(calculate_delivery_cost(35, 4999, "хрупкий___", False), res)

    def test_8(self):
        res = 56438.75, "2026-09-07"
        self.assertEqual(calculate_delivery_cost(35, 4999, "обычный", True), res)

    def test_9(self):
        res = 2800, "2026-09-04"
        self.assertEqual(calculate_delivery_cost(2, 500, "опасный", False), res)

    def test_10(self):
        res = 9600, "2026-09-04"
        self.assertEqual(calculate_delivery_cost(15, 1500, "хрупкий", False), res)

if __name__ == "__main__":
  unittest.main()
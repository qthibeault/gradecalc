from unittest import TestCase

from gradecalc.core.assignment import Assignment
from gradecalc.core.category import Category


class CategoryTestCase(TestCase):
    def setUp(self):
        assignments = [
            Assignment(90, 100),
            Assignment(86, 100),
            Assignment(94, 100),
        ]
        self.category = Category("Homework", 0.2, assignments)

    def test_score(self):
        self.assertEqual(self.category.score, 270)

    def test_total(self):
        self.assertEqual(self.category.total, 300)

    def test_percentage(self):
        self.assertEqual(self.category.percentage, 0.9)

    def test_drop_lowest(self):
        category = self.category.drop_lowest(1)
        self.assertEqual(len(category.assignments), 2)
        self.assertNotIn(Assignment(86, 100), category.assignments)

    def test_no_assignments(self):
        with self.assertRaises(ValueError):
            Category("", 0.1, [])

    def test_bad_weight(self):
        with self.assertRaises(ValueError):
            Category("", 0, [Assignment(10, 10)])
            Category("", 1.1, [Assignment(10, 10)])

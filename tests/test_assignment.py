from unittest import TestCase

from gradecalc.core.assignment import Assignment


class AssignmentTestCase(TestCase):
    def test_zero_total(self):
        with self.assertRaises(ValueError):
            Assignment(0, 0)

    def test_grade(self):
        self.assertEqual(Assignment(10, 20).grade, 0.5)

    def test_add(self):
        self.assertEqual(Assignment(10, 10) + Assignment(20, 20), Assignment(30, 30))

    def test_add_with_name(self):
        sum_ = Assignment(1, 1, "Homework 1") + Assignment(1, 1, "Homework 2")
        self.assertIsNone(sum_.name)

    def test_equals(self):
        self.assertEqual(Assignment(10, 10), Assignment(10, 10))
        self.assertEqual(Assignment(10, 10, "Homework 1"), Assignment(10, 10, "Homework 1"))
        self.assertNotEqual(Assignment(10, 10), Assignment(10, 20))
        self.assertNotEqual(Assignment(10, 10), Assignment(20, 10))
        self.assertNotEqual(Assignment(10, 10, "Homework 1"), Assignment(10, 10, "Homework 2"))

    def test_from_dict(self):
        self.assertEqual(
            Assignment.fromdict({"recieved": 10, "possible": 10}), Assignment(10, 10, None)
        )
        self.assertEqual(
            Assignment.fromdict({"recieved": 10, "possible": 10, "name": "Homework 1"}),
            Assignment(10, 10, "Homework 1"),
        )

        with self.assertRaises(Exception):
            Assignment.fromdict({"foo": 10, "bar": 10})
            Assignment.fromdict({"recieved": 10})
            Assignment.fromdict({"recieved": "foo", "possible": "bar"})

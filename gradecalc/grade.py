from functools import reduce


def weighted(categories):
    return sum(category.grade * category.weight for category in categories)


def points_based(categories):
    assignments = [assignment for category in categories for assignment in category.assignments]
    points = reduce(lambda a, b: a + b, assignments)
    return points.grade

from functools import reduce

from attr import attrs, attrib

from .assignment import Assignment


def _drop_lowest(n, assignments):
    for _ in range(n):
        lowest_score = min(assignments, key=lambda a: a.grade)
        assignments = [assignment for assignment in assignments if assignment != lowest_score]

    return assignments


@attrs(frozen=True)
class Category:
    name = attrib(converter=str)
    weight = attrib(converter=float)
    assignments = attrib()

    @property
    def score(self):
        return sum(assignment.score for assignment in self.assignments)

    @property
    def total(self):
        return sum(assignment.total for assignment in self.assignments)

    @property
    def grade(self):
        assignments = reduce(lambda a, b: a + b, self.assignments)
        return Assignment(assignments.score, assignments.total, self.name)


    @weight.validator
    def check_weight(self, attribute, value):
        if value <= 0 or value > 1:
            raise ValueError("Weight must be inside interval (0, 1]")

    @assignments.validator
    def check_assignments(self, attribute, value):
        if len(value) == 0:
            raise ValueError("Assignments must not be empty")

    def __str__(self):
        return f"{self.name} ({self.weight}): {self.grade}"

    def drop_lowest(self, n):
        return Category(self.name, self.weight, _drop_lowest(n, self.assignments))

    @classmethod
    def fromdict(cls, name, data):
        assignments = [Assignment.fromdict(assignment) for assignment in data["scores"]]
        drop_count = data.get("drop_lowest", 0)
        return cls(name, data["weight"], assignments).drop_lowest(drop_count)

from attr import attrs, attrib
from attr.converters import optional


@attrs(frozen=True, eq=True)
class Assignment:
    score = attrib(converter=float)
    total = attrib(converter=float)
    name = attrib(default=None, converter=optional(str))

    @property
    def percentage(self):
        return self.score / self.total

    def __add__(self, other):
        return Assignment(self.score + other.score, self.total + other.total, None)

    def __str__(self):
        return f"{self.percentage:.4f}"

    @total.validator
    def check_total(self, attribute, value):
        if value <= 0:
            raise ValueError("Total must be greater than zero")

    @classmethod
    def fromdict(cls, data):
        return cls(data["recieved"], data["possible"], data.get("name", None))

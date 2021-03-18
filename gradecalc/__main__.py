#!/usr/bin/env python3
from argparse import ArgumentParser

from schema import Optional, Schema, Use
from gradecalc.core import Category
from gradecalc.grade import weighted, points_based
from yaml import safe_load as load_yaml

_score_schema = Schema({"recieved": Use(float), "possible": Use(float)})
_category_schema = Schema(
    {"weight": Use(float), "scores": [_score_schema], Optional("drop_lowest"): int}
)
_grades_schema = Schema({str: _category_schema})

# Parser
_parser = ArgumentParser(description="Compute course grade")
_parser.add_argument(
    "-f", "--file", default="grades.yaml", help="File containing grade information"
)
_parser.add_argument(
    "-v",
    "--verbose",
    action="store_true",
    help="Output additional data",
    default=False,
)
_scheme_group = _parser.add_mutually_exclusive_group()
_scheme_group.add_argument(
    "-w",
    "--weighted",
    action="store_const",
    dest="scheme",
    const=weighted,
    help="Computed weighted grade",
)
_scheme_group.add_argument(
    "-p",
    "--points-based",
    action="store_const",
    dest="scheme",
    const=points_based,
    help="Compute points-based grade ignoring weights",
)
_scheme_group.set_defaults(scheme=weighted)


def _print_grades(grades):
    for grade in grades:
        print(grade)


def main():
    args = _parser.parse_args()
    grades_file = open(args.file, "r")
    grade_data = _grades_schema.validate(load_yaml(grades_file))
    grades = [Category.fromdict(name, category) for name, category in grade_data.items()]

    if args.verbose:
        _print_grades(grades)

    final_grade = args.scheme(grades)

    print(f"Final grade: {final_grade}")


if __name__ == "__main__":
    main()

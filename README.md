gradecalc
=========

Compute class grades defined in YAML files. Supports points-based and weighted grading systems.

Input
-----

__gradecalc__ accepts YAML files that describe the assignments in a course. An example of a valid file looks like:

```yaml
---
homework:
  weight: 0.2
  drop_lowest: 2
  scores:
    - recieved: 94
      possible: 100
    - recieved: 87
      possible: 100
    - recieved: 24
      possible: 30
exams:
  weight: 0.4
  scores:
    - name: "Exam 1"
      recieved: 88
      possible: 110
    - recieved: 97
      possible: 100
quizzes:
  weight: 0.4
  drop_lowest: 1
  scores:
    - recieved: 0
      possible: 10
    - recieved: 10
      possible: 10
...
```

Each grade category is defined by an arbitrary name (in this example they are _homework_, _exams_, and _quizzes_) but
could be anything. Each category is required to have a `scores` list. Each score is required to the `recieved` and
`possible` fields, as well as an optional name field to differentiate the assignments if desired. Each category may have
an optional `drop_lowest` field to indicate the number of assignments to drop going in ascending order of percentage.
Each category may also have a `weight` field to indicate the weight of the category when computing the weighted grade.

When executed, __gradecalc__ will search for a file named _grades.yaml_ by default. This can be changed by specifying a
different filename using the `-f, --file` flag.

Options
-------

__gradecalc__ supports multiple options, which can be listed with the `--help` flag. The most important flags are
`-w, --weighted` and `-p, --points-based` which dictate the way that the final grade is computed.

Installation
------------

This program is available for installation through `pip`.

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pathlib import Path
from typing import Optional


def read_input(location: str, input_file_name: str = "input") -> str:
    folder = Path(location).parent
    input_path = folder / input_file_name
    with open(input_path) as reader:
        content = reader.read()
    return content


class Point(object):
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def distance(self, other: "Point") -> int:
        dx, dy = self - other
        return abs(dx) + abs(dy)

    def __sub__(self, other: "Point") -> tuple:
        return (self.x - other.x, self.y - other.y)

    def __str__(self) -> str:
        return f"({self.x}, {self.y})"

    def __repr__(self) -> str:
        return f"Point({self.x}, {self.y})"

    def __hash__(self) -> int:
        return hash((self.x, self.y))


class Line(object):
    def __init__(
        self, k: Optional[float], b: Optional[float], a: Optional[float] = None
    ) -> None:
        self.k = k
        self.b = b
        self.a = a

    @classmethod
    def from_points(cls, p1: Point, p2: Point) -> "Line":
        try:
            k = (p1.y - p2.y) / (p1.x - p2.x)  # type: Optional[float]
            b = (p1.x * p2.y - p2.x * p1.y) / (p1.x - p2.x)  # type: Optional[float]
            a = None
        except ZeroDivisionError:
            k = None
            b = None
            a = p1.x

        return cls(k, b, a)

    def y(self, x: float) -> float:
        if self.a is None:
            return self.k * x + self.b
        else:
            return self.a

    def __str__(self):
        if self.a is None:
            op = "+" if self.b >= 0 else "-"
            return f"y = {self.k:.2f}x {op} {abs(self.b):.2f}"
        else:
            return f"x = {self.a:.2f}"

    def __repr__(self):
        return f"Line({self.k}, {self.b}, {self.a})"

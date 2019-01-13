#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math

from utils import read_input

serial = int(read_input(__file__))
# square: List[int] = []


def power(x: int, y: int) -> int:
    return (x + 10) * ((x + 10) * y + serial)


def square_power(sx: int, sy: int) -> int:
    return sum(
        (
            math.floor(power(x, y) / 100) % 10 - 5
            for y in range(sy, sy + 3)
            for x in range(sx, sx + 3)
        )
    )


square = [[square_power(x + 1, y + 1) for x in range(298)] for y in range(298)]

max = 0
index = (0, 0)
for y, line in enumerate(square):
    for x, p in enumerate(line):
        if p > max:
            max = p
            index = (x + 1, y + 1)

print(max, index)

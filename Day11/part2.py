#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 9.10s user 0.04s system 99% cpu 9.162 total

from utils import read_input

serial = int(read_input(__file__))


def cell_power(x: int, y: int) -> int:
    return (x + 10) * ((x + 10) * y + serial) // 100 % 10 - 5


powers = [[0 for x in range(301)] for y in range(301)]
for y in range(1, 301):
    for x in range(1, 301):
        powers[y][x] = (
            cell_power(x, y)
            + powers[y][x - 1]
            + powers[y - 1][x]
            - powers[y - 1][x - 1]
        )

max_power = 0
index = None
size = 1
for s in range(1, 301):
    for y in range(1, 301 - s):
        for x in range(1, 301 - s):
            sum_power = (
                powers[y - 1][x - 1]
                - powers[y - 1][x + s - 1]
                - powers[y + s - 1][x - 1]
                + powers[y + s - 1][x + s - 1]
            )
            if sum_power > max_power:
                max_power = sum_power
                index = (x, y)
                size = s

print(max_power, index, size)

#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from utils import Point, read_input

raw = read_input(__file__)
points = [Point(*[int(x) for x in line.split(", ")]) for line in raw.splitlines()]
ys = [p.y for p in points]
xs = [p.x for p in points]
min_x = min(xs)
max_x = max(xs)
min_y = min(ys)
max_y = max(ys)

valid_points = 0
for x in range(min_x, max_x + 1):
    for y in range(min_y, max_y + 1):
        point = Point(x, y)
        distance = sum([point.distance(p) for p in points])
        if distance < 10000:
            valid_points += 1

print(valid_points)

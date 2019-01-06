#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import math
from collections import defaultdict
from typing import Dict, Set
import itertools

from utils import Point, read_input

raw = read_input(__file__)
points = [Point(*[int(x) for x in line.split(", ")]) for line in raw.splitlines()]
ys = [p.y for p in points]
xs = [p.x for p in points]
min_x = min(xs)
max_x = max(xs)
min_y = min(ys)
max_y = max(ys)

boundary_points = itertools.chain.from_iterable(
    (
        (
            Point(x, y)
            for x in range(min_x - 1, max_x + 2)
            for y in (min_y - 1, max_y + 1)
        ),
        (Point(x, y) for y in range(min_y, max_y + 1) for x in (min_x - 1, max_x + 1)),
    )
)

infinity_points: Set[Point] = set()
for point in boundary_points:
    distances = [point.distance(ip) for ip in points]
    min_num = 0
    min_distance = math.inf
    idx = None
    for i, distance in enumerate(distances):
        if distance < min_distance:
            min_distance = distance
            min_num = 1
            idx = i
        elif distance == min_distance:
            min_num += 1
    if min_num == 1:
        infinity_points.add(points[idx])

region: Dict[Point, int] = defaultdict(int)
for x in range(min_x, max_x + 1):
    for y in range(min_y, max_y + 1):
        point = Point(x, y)
        distances = [point.distance(ip) for ip in points]
        min_num = 0
        min_distance = math.inf
        idx = None
        for i, distance in enumerate(distances):
            if distance < min_distance:
                min_distance = distance
                min_num = 1
                idx = i
            elif distance == min_distance:
                min_num += 1
        if min_num == 1:
            region[points[idx]] += 1

finity_points = [p for p in points if p not in infinity_points]
finity_region: Dict[Point, int] = {
    point: size for point, size in region.items() if point in finity_points
}
print(max(finity_region.values()))

# for x in range(int(min_x) - 1, int(max_x) + 2):
#     for y in range(int(min_y) - 1, int(max_y) + 2):
#         point = Point(x, y)
#         distances = [point.distance(ip) for ip in points]
#         min_distance = min(distances)
#         num_min = len(list(filter(lambda d: d == min_distance, distances)))
#         if num_min == 1:
#             index = distances.index(min_distance)
#             second_round[points[index]] += 1

# max = 0
# inner_points = [p for p in points if p not in outer_points]
# for point in inner_points:
#     if first_round[point] == second_round[point]:
#         if first_round[point] > max:
#             max = first_round[point]
#         print((point, first_round[point]))
# print(f"max = {max}")

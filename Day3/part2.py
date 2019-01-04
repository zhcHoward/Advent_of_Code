#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re

from utils import read_input


raw = read_input(__file__)
inputs = raw.split('\n')

fabric = [[[] for _ in range(1000)] for _ in range(1000)]
pattern = re.compile(r"#(\d+) @ (\d+),(\d+): (\d+)x(\d+)")

claims = [
    (id, top, left + width, top + height, left)
    for id, left, top, width, height in map(
        lambda x: (int(i) for i in x),
        (r.groups() for r in map(pattern.match, inputs)),
    )
]

for id, top, right, bottom, left in claims:
    for x in range(left, right):
        for y in range(top, bottom):
            fabric[y][x].append((id, top, right, bottom, left))

for row in fabric:
    for inch in row:
        if len(inch) > 1:
            for rect in inch:
                try:
                    claims.remove(rect)
                except ValueError:
                    continue

print(claims[0][0])

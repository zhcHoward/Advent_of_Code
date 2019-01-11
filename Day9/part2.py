#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from collections import deque


players = 430
last_no = 71588 * 100

points = [0 for _ in range(players)]
marbles = deque([0])

for i in range(1, last_no + 1):
    if i % 23 == 0:
        marbles.rotate(7)
        points[i % players] += i + marbles.pop()
        marbles.rotate(-1)
    else:
        marbles.rotate(-1)
        marbles.append(i)

print(max(points))

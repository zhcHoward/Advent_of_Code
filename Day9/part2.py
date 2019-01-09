#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from typing import List


players = 430
last_no = 71588 * 100

points = [0 for _ in range(players)]
marbles: List[int] = [0]
i = 1
current = 0
while i <= last_no:
    for player in range(players):
        if i % 23 == 0:
            current = (current - 7) % len(marbles)
            points[player] += i + marbles.pop(current)
        else:
            current = (current + 2) % len(marbles)
            marbles.insert(current, i)

        i += 1
        if i > last_no:
            break

print(max(points))

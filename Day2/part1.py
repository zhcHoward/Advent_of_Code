#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from collections import defaultdict

from utils import read_input


raw = read_input(__file__)
inputs = raw.split()


def calculate(string: str) -> tuple(int, int):
    count = defaultdict(int)
    for char in string:
        count[char] += 1
    counts = count.values()
    return 2 in counts, 3 in counts


twos = 0
threes = 0
for two, three in map(calculate, inputs):
    twos += two
    threes += three

print(twos * threes)

# -*- coding: utf-8 -*-

from utils import read_input


def react(raw):
    i = 0
    while i < len(raw) - 1:
        if raw[i] != raw[i + 1] and raw[i].upper() == raw[i + 1].upper():
            raw = raw[:i] + raw[i + 2 :]
            i -= 2
        i += 1
        if i < 0:
            # string[-1] is legal in pythons
            # make sure i will not be smaller than 0s
            i = 0
    return raw


raw = read_input(__file__)
chars = {char.upper() for char in set(raw)}
results = {}

for char in chars:
    temp = raw.replace(char, "").replace(char.lower(), "")
    polymer = react(temp)
    results[char] = len(polymer)

print(min(results.values()))

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from utils import read_input


raw = read_input(__file__)
inputs = raw.split()


def compare(one: str, other: str) -> [str, None]:
    diff = 0
    result = ''
    for i, j in zip(one, other):
        if i != j:
            diff += 1
            if diff > 1:
                return None
        else:
            result += i
    return result


for i in range(len(inputs)):
    one = inputs[i]
    for string in inputs[i + 1:]:
        result = compare(one, string)
        if result:
            print(result)
            exit(0)

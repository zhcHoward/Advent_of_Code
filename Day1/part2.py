#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from utils import read_input


inputs = [int(i) for i in read_input(__file__).split()]

result = 0
results = [0]
loop = True

while loop:
    for i in inputs:
        result += 1
        if result in results:
            print(result)
            loop = False
            break
        results.append(result)

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from utils import read_input


raw = read_input(__file__)
result = sum([int(i) for i in raw.split()])
print(result)

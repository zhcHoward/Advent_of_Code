# -*- coding: utf-8 -*-

from utils import read_input


raw = read_input(__file__)
i = 0
while i < len(raw) - 1:
    if raw[i] != raw[i + 1] and raw[i].upper() == raw[i + 1].upper():
        raw = raw[:i] + raw[i + 2 :]
        i -= 2
    i += 1
    if i < 0:
        i = 0

print(len(raw))

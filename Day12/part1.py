#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from utils import read_input

raw = read_input(__file__)
lines = raw.splitlines()
init_state = lines[0].split()[2]
grow_rule = {
    pattern: result for pattern, result in map(lambda l: l.split(" => "), lines[2:])
}

left_most = 0
states = init_state
next_states = ""
left_most = 0
for generation in range(1, 21):
    states = "....." + states + "....."
    for i in range(len(states) - 4):
        next_states += grow_rule[states[i : i + 5]]

    states_len = len(next_states)
    next_states = next_states.lstrip(".")
    delta = states_len - len(next_states)
    left_most -= 3 - delta
    states = next_states.rstrip(".")
    next_states = ""

sum = 0
for pot in states:
    if pot == "#":
        sum += left_most
    left_most += 1

print(sum)

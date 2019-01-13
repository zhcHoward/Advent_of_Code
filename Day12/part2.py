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
sum = 0
for g in range(1, 101):
    states = "".join((".....", states, "....."))
    new_generation = "".join(
        (grow_rule[states[i : i + 5]] for i in range(len(states) - 4))
    )
    left_most -= 3 - len(new_generation) + len(new_generation.lstrip("."))
    states = new_generation.strip(".")

    new_sum = 0
    left = left_most
    for pot in states:
        if pot == "#":
            new_sum += left
        left += 1

    print(g, new_sum, new_sum - sum)
    sum = new_sum

print(sum + (50000000000 - 100) * 91)

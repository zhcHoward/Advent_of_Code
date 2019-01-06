#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from collections import defaultdict
from typing import Dict, List

from utils import read_input

raw = read_input(__file__)
steps: Dict[str, List[str]] = defaultdict(list)
for line in raw.splitlines():
    words = line.split()
    step = words[7]
    require = words[1]
    if require not in steps:
        steps[require] = []
    steps[step].append(require)

steps_done: List[str] = []
available_steps = sorted(
    [step for step, requires in steps.items() if not requires], reverse=True
)
while available_steps:
    step_done = available_steps.pop()
    steps_done.append(step_done)
    for requires in steps.values():
        if step_done in requires:
            requires.remove(step_done)

    steps.pop(step_done)
    available_steps = sorted(
        [step for step, requires in steps.items() if not requires], reverse=True
    )

print("".join(steps_done))

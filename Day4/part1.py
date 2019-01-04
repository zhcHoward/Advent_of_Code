#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
from datetime import datetime, timedelta
from collections import defaultdict

from utils import read_input


raw = read_input(__file__)
inputs = raw.split("\n")

pattern = re.compile(r"\[(.+)\] (.+)")
timeline = []
for i in inputs:
    time_str, action = pattern.match(i).groups()
    time = datetime.strptime(time_str, "%Y-%m-%d %H:%M")
    timeline.append((time, action))

timeline.sort(key=lambda x: x[0])
guard_sleep = defaultdict(list)
start_time = timeline[0][0]
for time, action in timeline:
    if action.startswith("Guard"):
        guard_id = action.split()[1][1:]
        continue

    if action == "falls asleep":
        start_time = time
        continue

    guard_sleep[guard_id].append((time - start_time).seconds / 60)

max_id = ""
longest_asleep = 0

for guard_id, sleep_time in guard_sleep.items():
    asleep_time = sum(sleep_time)
    if asleep_time > longest_asleep:
        max_id = guard_id
        longest_asleep = asleep_time

sleep_minute = [0 for _ in range(60)]
for time, action in timeline:
    if action.startswith("Guard #401"):
        skip = False
    else:
        if action.startswith('Guard'):
            skip = True
        else:
            if not skip:
                if action == 'falls asleep':
                    start = time.minute
                else:
                    for i in range(start, time.minute):
                        sleep_minute[i] += 1
            else:
                continue

print(max_id)
print(int(max_id) * max(sleep_minute))

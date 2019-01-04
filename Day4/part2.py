# -*- coding: utf-8 -*-

import re
from datetime import datetime
from collections import defaultdict
from operator import itemgetter

from utils import read_input


raw = read_input(__file__)
inputs = raw.splitlines()

timeline = []
pattern = re.compile(r'\[(.+)\] (.+)')
for line in inputs:
    time_str, action = pattern.match(line).groups()
    time = datetime.strptime(time_str, "%Y-%m-%d %H:%M")
    timeline.append((time, action))

timeline.sort(key=itemgetter(0))

sum_sleep = defaultdict(lambda: [0 for _ in range(60)])
for time, action in timeline:
    if action.startswith('Guard #'):
        guard_id = action.split()[1][1:]
        continue
    
    if action == 'falls asleep':
        start = time.minute
        continue
    
    if action == 'wakes up':
        for i in range(start, time.minute):
            sum_sleep[guard_id][i] += 1

max_guard_id = None
longest_minute = None
max_sleep_time = 0
for guard_id, sleep_times in sum_sleep.items():
    current_max_sleep_time = max(sleep_times)
    if current_max_sleep_time > max_sleep_time:
        max_guard_id = guard_id
        longest_minute = sleep_times.index(current_max_sleep_time)
        max_sleep_time = current_max_sleep_time

print(int(max_guard_id) * longest_minute)

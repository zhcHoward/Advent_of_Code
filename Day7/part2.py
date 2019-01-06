#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from __future__ import annotations

import string
from typing import Dict, List, Sequence, Optional, Set
from mypy_extensions import TypedDict

from utils import read_input

Task = TypedDict("Task", {"name": str, "time": int, "pre_tasks": Set[str]})


class Worker(object):
    def __init__(self, id: int) -> None:
        self.id = id
        self.task: Optional[Task] = None
        self.time_left: Optional[int] = None

    def add_task(self, task: Task) -> None:
        self.task = task
        self.time_left = task["time"]

    def do_task(self) -> None:
        if self.is_idle:
            return
        self.time_left -= 1

    def complete(self) -> Task:
        task = self.task
        self.task = None
        self.time_left = None
        return task

    @property
    def is_done(self) -> bool:
        return self.time_left <= 0

    @property
    def is_idle(self) -> bool:
        return self.task is None

    def __hash__(self):
        return hash(self.id)


class Workers(object):
    def __init__(self, worker_num: int = 5) -> None:
        self.idle_workers = [Worker(i) for i in range(worker_num)]
        self.busy_workers: List[Worker] = []

    def do_task(self) -> Set[str]:
        done_tasks: Set[str] = set()
        done_workers: List[Worker] = []
        for worker in self.busy_workers:
            worker.do_task()
            if worker.is_done:
                done_workers.append(worker)
                done_task = worker.complete()
                done_tasks.add(done_task["name"])

        for worker in done_workers:
            self.busy_workers.remove(worker)
            self.idle_workers.append(worker)
        return done_tasks

    def add_task(self, task: Task) -> bool:
        try:
            worker = self.idle_workers.pop()
        except IndexError:
            return False

        worker.add_task(task)
        self.busy_workers.append(worker)
        return True

    def add_tasks(self, tasks: Sequence[Task]) -> List[Task]:
        added_tasks = []
        for task in tasks:
            if self.add_task(task):
                added_tasks.append(task)
            else:
                break
        return added_tasks

    def are_working(self) -> bool:
        return bool(self.busy_workers)


raw = read_input(__file__)
tasks: Dict[str, Task] = {}
for line in raw.splitlines():
    words = line.split()
    task_name = words[7]
    pre_task_name = words[1]
    for name in (task_name, pre_task_name):
        if name not in tasks:
            tasks[name] = {
                "name": name,
                "time": 60 + string.ascii_uppercase.index(name) + 1,
                "pre_tasks": set(),
            }
    tasks[task_name]["pre_tasks"].add(pre_task_name)


workers = Workers(5)

time = 0
while tasks or workers.are_working():
    available_tasks = sorted(
        [task for task in tasks.values() if not task["pre_tasks"]],
        key=lambda t: t["name"],
    )
    added_tasks = workers.add_tasks(available_tasks)
    done_task_names = workers.do_task()
    for task in added_tasks:
        tasks.pop(task["name"])

    if done_task_names:
        for task in tasks.values():
            task["pre_tasks"] -= done_task_names

    time += 1


print(time)

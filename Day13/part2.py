#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from collections import deque
from operator import attrgetter
from typing import Deque

from utils import read_input


class Direction:
    UP = "^"
    DOWN = "v"
    LEFT = "<"
    RIGHT = ">"


def turn_left(direction):
    if direction == Direction.DOWN:
        return Direction.RIGHT
    if direction == Direction.RIGHT:
        return Direction.UP
    if direction == Direction.UP:
        return Direction.LEFT
    return Direction.DOWN


def turn_right(direction):
    if direction == Direction.DOWN:
        return Direction.LEFT
    if direction == Direction.RIGHT:
        return Direction.DOWN
    if direction == Direction.UP:
        return Direction.RIGHT
    return Direction.UP


class Cart(object):
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction
        self.num_cross = 0

    def move(self):
        if self.direction == Direction.UP:
            self.y -= 1
        elif self.direction == Direction.DOWN:
            self.y += 1
        elif self.direction == Direction.LEFT:
            self.x -= 1
        else:
            self.x += 1

        if road_map[self.y][self.x] in ("|", "-"):
            return
        elif road_map[self.y][self.x] == "/":
            if self.direction in (Direction.UP, Direction.DOWN):
                self.direction = turn_right(self.direction)
            else:
                self.direction = turn_left(self.direction)
        elif road_map[self.y][self.x] == "\\":
            if self.direction in (Direction.UP, Direction.DOWN):
                self.direction = turn_left(self.direction)
            else:
                self.direction = turn_right(self.direction)
        else:  # road_map[self.y][self.x] == '+'
            if self.num_cross == 0:
                self.direction = turn_left(self.direction)
            elif self.num_cross == 1:
                pass
            else:
                self.direction = turn_right(self.direction)
            self.num_cross = (self.num_cross + 1) % 3

    def __eq__(self, other):  # for in operator
        return isinstance(other, Cart) and self.x == other.x and self.y == other.y

    def __repr__(self):
        return f"Cart({self.x}, {self.y}, {self.direction})"


raw = read_input(__file__)
road_map = []
carts: Deque[Cart] = deque([])
for y, line in enumerate(raw.splitlines()):
    row = []
    for x, char in enumerate(line):
        if char in (Direction.UP, Direction.DOWN):
            row.append("|")
            carts.append(Cart(x, y, char))
        elif char in (Direction.LEFT, Direction.RIGHT):
            row.append("-")
            carts.append(Cart(x, y, char))
        else:
            row.append(char)
    road_map.append(row)


new_carts: Deque[Cart] = deque([])
while len(carts) + len(new_carts) > 1:
    while carts:
        cart = carts.popleft()
        cart.move()
        if cart in carts:
            carts.remove(cart)
        elif cart in new_carts:
            new_carts.remove(cart)
        else:
            new_carts.append(cart)
    else:
        if len(new_carts) == 1:
            break
        carts = deque(sorted(new_carts, key=attrgetter("y", "x")))
        new_carts = deque([])


print(new_carts[0])

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from typing import List

from utils import read_input


class Node(object):
    def __init__(
        self, id: int, child_no: int = 0, meta_no: int = 0, parent: "Node" = None
    ) -> None:
        self.children: List["Node"] = []
        self.metadata: List[int] = []
        self.child_no = child_no
        self.meta_no = meta_no
        self.parent = parent
        self.id = id
        self.visited = False

    def add_child(self, node: "Node") -> None:
        self.children.append(node)

    @property
    def children_full(self):
        return len(self.children) >= self.child_no

    @property
    def metadata_full(self):
        return len(self.metadata) >= self.meta_no

    def __hash__(self):
        return self.id

    def __repr__(self):
        return f"Node({self.id}, {self.metadata}, {self.children})"


raw = read_input(__file__)
numbers = [int(i) for i in raw.split()]
node_id = 0
root = Node(node_id, 1, 0, None)
node_id += 1


class State(object):
    def __init__(self):
        self.node = root
        self.parent = None
        self.is_meta = False
        self.is_child = False
        self.is_child_no = True
        self.is_meta_no = False

    def update(self):
        if self.is_child_no:
            self.is_meta_no = True
            self.is_child_no = False
        elif self.is_meta_no:
            self.is_meta_no = False
            if self.node.children_full:
                self.is_meta = True
            else:
                self.is_child_no = True
        else:  # is_meta
            if self.node.metadata_full:
                if not self.parent.children_full:
                    self.is_meta = False
                    self.is_child_no = True
                    self.node = self.parent  # current node is done, go back to parent
                else:
                    while self.node.metadata_full and self.parent.children_full:
                        self.node = self.parent
                        self.parent = self.node.parent
                        if not self.parent:
                            break


s = State()
for num in numbers:
    if s.is_child_no:
        s.parent = s.node
        node = Node(node_id, num, parent=s.parent)
        node_id += 1
        s.node = node
        s.parent.children.append(node)
        s.update()
    elif s.is_meta_no:
        s.node.meta_no = num
        s.update()
    else:
        s.node.metadata.append(num)
        s.update()


summary = 0
node = root.children[0]
while node:
    if not node.visited:
        summary += sum(node.metadata)
        node.visited = True

    for n in node.children:
        if not n.visited:
            node = n
            break
    else:
        node = node.parent

print(summary)

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pathlib import Path


def read_input(location: str, input_file_name: str = "input") -> str:
    folder = Path(location).parent
    input_path = folder / input_file_name
    with open(input_path) as reader:
        content = reader.read()
    return content

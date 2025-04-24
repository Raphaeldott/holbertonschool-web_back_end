#!/usr/bin/env python3
"""
Complex types annotation - list of floats
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    type-annotated function sum_list which takes a list input_list of floats
    as argument and returns their sum as a float.
    Remark from Python 3.9+, can replace typing.List by just list[]
    """
    sum: float = 0.0
    for number in input_list:
        sum += number
    return sum

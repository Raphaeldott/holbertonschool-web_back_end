#!/usr/bin/env python3
"""
This module serves as basic example for variable annotation for type string
"""


def concat(str1: str, str2: str) -> str:
    """
    type-annotated function concat that takes a string str1 and a string str2
    as arguments and returns a concatenated string
    """
    return str1 + str2

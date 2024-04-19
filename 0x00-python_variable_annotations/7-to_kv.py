#!/usr/bin/env python3
"""
contains function to_kv
"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    functiont that takes a string and a int or float
    and returns a tuple
    """
    return (k, v**2)

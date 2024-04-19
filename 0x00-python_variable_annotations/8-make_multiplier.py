#!/usr/bin/env python3
"""contains function make_multiplier"""


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    method to take a float multiplier
    and return a function that multiplies a float
    """
    return lambda x: x * multiplier

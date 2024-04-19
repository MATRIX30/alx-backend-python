#!/usr/bin/env python3
"""
contains sum_mixed_list function
"""
from typing import Union, List


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Takes a list of integers and floats and returns
    their sum
    """
    return sum(mxd_lst)

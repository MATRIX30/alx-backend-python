#!/usr/bin/env python3
"""
contains a function element_length
"""

from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    function to return a list of tuples
    """
    return [(i, len(i)) for i in lst]

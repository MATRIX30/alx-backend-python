#!/usr/bin/env python3
"""
contains safe_first_element function
"""

from typing import Any, Union, Sequence


# The types of the elements of the input are not know
def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    recieves and iteraable and returns
    an element in it  or None
    """
    if lst:
        return lst[0]
    else:
        return None

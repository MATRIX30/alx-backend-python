#!/usr/bin/env python3
"""
contains the function safely_get_value
"""

from typing import TypeVar, Mapping, Any, Union

T = TypeVar("T")


def safely_get_value(
    dct: Mapping, key: Any, default: Union[T, None] = None
) -> Union[Any, T]:
    """
    Method to get all the values
    """
    if key in dct:
        return dct[key]
    else:
        return default

#!/usr/bin/env python3
"""
contains async_generator function
"""


import random
import asyncio


async def async_generator() -> float:
    """
    coroutine to that returns a random number betwee 1-10
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)

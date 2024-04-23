#!/usr/bin/env python3
"""
contains async_generator function
"""


import random
import asyncio
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    coroutine to that returns a random number betwee 1-10
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)

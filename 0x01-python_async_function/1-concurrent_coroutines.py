#!/usr/bin/env python3
"""
contains wait_n coroutine function 
"""

wait_random = __import__('0-basic_async_syntax').wait_random
import asyncio
from typing import List

async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    method to spawn wait_random n times with a specified max_delay
    and returns the list of all delay values
    Args:
		n(int): number of times to spawn wait_random
		max_delay(int): maximum delay
	Returns:
		List(float): List of float of delay values
    """
    result = []
    for _ in range(n):
        delay = await wait_random(max_delay)
        result.append(delay)
    return result

#!/usr/bin/env python3
"""
contains wait_n coroutine function
"""


import asyncio
from typing import List

task_wait_random = __import__("3-tasks").task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    method to spawn wait_random n times with a specified max_delay
    and returns the list of all delay values
    Args:
                n(int): number of times to spawn wait_random
                max_delay(int): maximum delay
        Returns:
                List(float): List of float of delay values
    """
    result: List[float] = []
    # create a list of n task

    tasks = [task_wait_random(max_delay) for _ in range(n)]

    for task in asyncio.as_completed(tasks):
        delay = await task
        result.append(delay)
    return result

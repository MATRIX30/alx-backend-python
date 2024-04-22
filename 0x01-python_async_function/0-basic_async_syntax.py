#!/usr/bin/env python3
"""
contains an asynch coroutine wait_random
"""


import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """
    coroutine that takes an integer max delay and waits for
    delay between 0-max_delay and eventually returns the delay time
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay

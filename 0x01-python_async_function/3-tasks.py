#!/usr/bin/env python3
"""
contain task_wait_random function
"""


from typing import Any
import asyncio

wait_random = __import__("0-basic_async_syntax").wait_random


def task_wait_random(max_delay: int) -> Any:
    """
    function that takes int max_delay and returns
    asyncio Task
    Args:
                max_delay(int): maximum time to delay for a task
        Returns:
                Task(asyncio): an asyncio task
    """
    return asyncio.create_task(wait_random(max_delay))

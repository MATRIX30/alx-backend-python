#!/usr/bin/env python3
"""
contains function measure_time
"""


import asyncio
import time

wait_n = __import__("1-concurrent_coroutines").wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    function to measure the total execution time for wait_n
    and returns total_time /n
    Args:
                n (int): number of task to spawn
                max_delay (int): maximum delay time per task
        Returns:
                float: the average time for a taks to execute
    """
    start_time: float = time.time()
    # enables you to run code in asynch fashion
    asyncio.run(wait_n(n, max_delay))
    stop_time: float = time.time()

    total_time: float = stop_time - start_time
    return total_time / n

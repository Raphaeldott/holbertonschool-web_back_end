#!/usr/bin/env python3
""" asyncio.gather """

import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """ executes comprehension func 4 times in parallel, returns runtime """

    start = time.perf_counter()
    await asyncio.gather(*(async_comprehension() for i in range(4)))
    stop = time.perf_counter()
    return stop - start

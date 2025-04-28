#!/usr/bin/env python3
""" Coroutine with async """

from typing import AsyncGenerator
import asyncio
import random


async def async_generator() -> AsyncGenerator[float, None]:
    """ Loops 10 times asyncronously, yields random num """

    for i in range(10):
        yield random.uniform(0, 10)
        await asyncio.sleep(1)

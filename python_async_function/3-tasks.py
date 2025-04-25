#!/usr/bin/env python3
"""
Write a function (do not create an async function, use the regular
function syntax to do this) task_wait_random that takes an intege
 max_delay and returns a asyncio.Task.
"""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    return asyncio.Task
    """
    return asyncio.create_task(wait_random(max_delay))

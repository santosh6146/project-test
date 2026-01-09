"""
Async task implementations.
Each task must return TaskResult.
"""

import asyncio
from app.models import TaskResult, TaskStatus


async def task1_fetch_data():
    await asyncio.sleep(1)  # Simulate I/O
    print("Fetching data...")
    return TaskResult(
        status=TaskStatus.SUCCESS,
        data={"value": 100}
    )


async def task2_process_data(data):
    await asyncio.sleep(1)
    print("Processing data...")

    if data and data.get("value", 0) > 0:
        data["processed"] = True
        return TaskResult(
            status=TaskStatus.SUCCESS,
            data=data
        )

    return TaskResult(status=TaskStatus.FAILURE)


async def task3_store_data(data):
    await asyncio.sleep(1)
    print("Storing data...")
    return TaskResult(status=TaskStatus.SUCCESS)


# Central task registry (easy extensibility)
TASK_REGISTRY = {
    "task1": task1_fetch_data,
    "task2": task2_process_data,
    "task3": task3_store_data,
}

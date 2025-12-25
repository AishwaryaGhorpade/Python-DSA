"""What is asyncio in Python?

asyncio is a Python library used to write concurrent code using the
async / await syntax.

It is designed for:

I/O-bound tasks (network, API calls, file I/O)

High-performance applications

Handling thousands of tasks without threads

📌 asyncio uses a single thread with an event loop."""

# 🔹 Why asyncio is Needed?
# ❌ Problem with normal (blocking) code
import time
def task():
    time.sleep(2)
    print("Task done")
task()
task()

# ⏱ Takes 4 seconds (blocking)

# With asyncio
# unning Multiple Coroutines
# asyncio.gather()

# Runs multiple coroutines together.

import asyncio

async def task():
    await asyncio.sleep(2)
    print("Task done")

async def main():
    await asyncio.gather(task(), task())

asyncio.run(main())

# ⏱ Takes 2 seconds (non-blocking)


# Tasks schedule coroutines to run concurrently.

# task = asyncio.create_task(coro())

# Example:
async def work():
    await asyncio.sleep(2)
    print("Done")

async def main():
    t1 = asyncio.create_task(work())
    t2 = asyncio.create_task(work())
    await t1
    await t2

asyncio.run(main())


"""asyncio.sleep() vs time.sleep()
| Function          | Blocking? |
| ----------------- | --------- |
| `time.sleep()`    | ❌ Yes     |
| `asyncio.sleep()` | ✅ No      |"""


async def fetch_data(id):
    print(f"Fetching {id}")
    await asyncio.sleep(2)
    return f"Data {id}"

async def main():
    results = await asyncio.gather(
        fetch_data(1),
        fetch_data(2),
        fetch_data(3)
    )
    print(results)

asyncio.run(main())
# Output:
# Fetching 1
# Fetching 2
# Fetching 3. 
# ( 2 seconds later...)
# ['Data 1', 'Data 2', 'Data 3']

import asyncio

async def long_operation(n):
    print(f"Starting long operation {n}")
    await asyncio.sleep(n)
    print(f"Finished long operation {n}")


async def main():
    task1 = asyncio.create_task(long_operation(2))
    task2 = asyncio.create_task(long_operation(3))

    # Wait for tasks to complete
    await task1
    await task2


if __name__ == "__main__":
    asyncio.run(main())
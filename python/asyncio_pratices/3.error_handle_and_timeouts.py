import asyncio

async def might_fail():
    try:
        await asyncio.sleep(2)
        print("Success!")
    except asyncio.CancelledError:
        print("Cancelled!")

async def main():
    task = asyncio.create_task(might_fail())

    try:
        await asyncio.wait_for(task, timeout=1)
    except asyncio.TimeoutError:
        print("Operation timed out!")
        task.cancel()
        await task

if __name__ == '__main__':
    asyncio.run(main())

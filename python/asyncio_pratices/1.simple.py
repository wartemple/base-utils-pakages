import asyncio

async def greet(name, delay):
    await asyncio.sleep(delay)
    print(f'Hello {name}!')

async def main():
    await asyncio.gather(
        greet('Alice', 1),
        greet('Bob', 2),
        greet('Charlie', 3),
    )

if __name__ == '__main__':
    asyncio.run(main())

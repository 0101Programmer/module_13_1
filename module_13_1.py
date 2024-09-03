import asyncio
import time

BALLS = [1, 2, 3, 4, 5]


async def start_strongman(name, power):
    print(f'Силач {name} начал соревнования.')
    for ball in BALLS:
        await asyncio.sleep(1 / power)
        print(f'Силач {name} поднял шар {ball}')
    print(f'Силач {name} закончил соревнования.')


async def start_tournament():
    task1 = asyncio.create_task(start_strongman('Арбузик', 3))
    task2 = asyncio.create_task(start_strongman('Dolphin', 4))
    task3 = asyncio.create_task(start_strongman('Саня', 5))

    await task1
    await task2
    await task3


asyncio.run(start_tournament())

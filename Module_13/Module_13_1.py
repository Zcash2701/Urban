import time
import asyncio


number_balls = 5

async def start_strongman(name, power):
    print(f'Силач {name} начал соревнование')
    for i in range(1, number_balls + 1):
        await  asyncio.sleep(number_balls/power)
        print(f'Силач {name} поднял {i} шар')
    print(f'Силач {name} закончил соревнование')

async def start_tournament():
    first_man = asyncio.create_task(start_strongman('Pasha', 3))
    second_man = asyncio.create_task(start_strongman('Denis', 4))
    third_man = asyncio.create_task(start_strongman('Apollon', 5))
    await first_man
    await second_man
    await third_man

asyncio.run(start_tournament())
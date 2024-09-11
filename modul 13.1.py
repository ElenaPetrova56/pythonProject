
import asyncio
async def start_strongman(name, power):
    print(f'Силач {name} начал соревнования.')

    for i in range(1, 6):
        # Задержка обратно пропорциональна силе
        delay = 1 / power
        await asyncio.sleep(delay)
        print(f'Силач {name} поднял {i} шар')

    print(f'Силач {name} закончил соревнования.')


async def start_tournament():
    # Определяем имена и силу силочей
    participants = [
        ("Иван", 10),
        ("Алексей", 20),
        ("Сергей", 15)
    ]

    # Создаём задачи для каждого силача
    tasks = [start_strongman(name, power) for name, power in participants]

    # Ожидаем завершения всех задач
    await asyncio.gather(*tasks)


# Запуск асинхронной функции
asyncio.run(start_tournament())

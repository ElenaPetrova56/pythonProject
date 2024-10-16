def calculate_structure_sum(data):
    total_sum = 0

    if isinstance(data, dict):
        for key, value in data.items():
            total_sum += len(str(key))  # добавляем длину ключа
            total_sum += calculate_structure_sum(value)  # рекурсивно вызываем для значения
    elif isinstance(data, (list, tuple)):
        for item in data:
            total_sum += calculate_structure_sum(item)  # рекурсивно для каждого элемента
    elif isinstance(data, str):
        total_sum += len(data)  # добавляем длину строки
    elif isinstance(data, (int, float)):
        total_sum += data  # добавляем число

    return total_sum


# Пример использования
data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)  # Ожидаемый результат: 99

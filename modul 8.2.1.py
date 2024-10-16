def personal_sum(numbers):
    result = 0
    incorrect_data = 0

    for item in numbers:
        try:
            result += item  # Попытка сложить значение
        except TypeError:
            incorrect_data += 1
            print(f'Некорректный тип данных для подсчёта суммы - {item}')

    return result, incorrect_data


def calculate_average(numbers):
    try:
        # Проверка, является ли numbers коллекцией
        if not isinstance(numbers, (list, tuple, set)):
            raise TypeError

        total_sum, incorrect_data = personal_sum(numbers)

        if len(numbers) - incorrect_data == 0:  # Если все данные некорректны
            return 0

        return total_sum / (len(numbers) - incorrect_data)

    except ZeroDivisionError:
        return 0
    except TypeError:
        print('В numbers записан некорректный тип данных')
        return None


# Пример вызова функции calculate_average с разными типами данных
print(f'Результат 1: {calculate_average("1, 2, 3")}')  # Строка
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')  # Список с некорректными данными
print(f'Результат 3: {calculate_average(567)}')  # Не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')  # Корректные данные

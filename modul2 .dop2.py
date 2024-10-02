def generate_password(n):
    result = ""
    pairs = []

    # Генерируем уникальные пары (a, b)
    for a in range(1, 21):
        for b in range(1, 21):
            if a != b and a + b <= n:
                pairs.append((a, b))

    # Проверяем, кратно ли число n сумме каждой пары и формируем пароль
    for a, b in pairs:
        pair_sum = a + b
        if n % pair_sum == 0:
            result += f"{a}{b}"

    return result

# Пример использования
if __name__ == "__main__":
    n = int(input("Введите число от 3 до 20: "))
    if 3 <= n <= 20:
        password = generate_password(n)
        print(f"Нужный пароль для числа {n}: {password}")
    else:
        print("Введите корректное число от 3 до 20.")
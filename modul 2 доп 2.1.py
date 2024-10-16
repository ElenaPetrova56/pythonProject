def generate_password(n):
    if n < 3 or n > 20:
        return "Число должно быть от 3 до 20."

    result = ""

    # Создаем пары чисел от 1 до n, где первое число не входит в пару
    for i in range(1, n):
        for j in range(i + 1, n + 1):
            pair_sum = i + j
            if n % pair_sum == 0:
                result += f"{i}{j}"

    return result


# Пример использования
if __name__ == "__main__":
    n = int(input("Введите число от 3 до 20: "))
    password = generate_password(n)
    print("Нужный пароль:", password)
def main():
    # Запрос ввода от пользователя
    input_expression = input("Input: ")

    # Разделение строки на части
    parts = input_expression.split()

    # Проверка на правильное количество элементов
    if len(parts) == 1:
        raise ValueError("Строка не является математической операцией")
    if len(parts) >= 4:
        raise ValueError("Формат математической операции не удовлетворяет заданию - два операнда и один оператор (+, -, /, *)")
    if len(parts) != 3:
        raise ValueError("Ошибка")

    # Парсинг чисел и операции
    try:
        a = int(parts[0])
        operator = parts[1]
        b = int(parts[2])
    except ValueError:
        raise ValueError("Вводите целые числа от 1 до 10")

    # Проверка диапазона для a и b
    if not (1 <= a <= 10) or not (1 <= b <= 10):
        raise ValueError("Числа должны быть от 1 до 10 включительно.")

    # Выполнение операции
    if operator == '+':
        result = a + b
    elif operator == '-':
        result = a - b
    elif operator == '*':
        result = a * b
    elif operator == '/':
        if b == 0:
            raise ZeroDivisionError("Деление на ноль.")
        result = a // b
    else:
        raise ValueError("Неправильная операция. Используйте +, -, * или /.")

    # Вывод результата
    print(f"Output: {result}")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Ошибка: {e}")
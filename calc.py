def main(user_input: str) -> str:

    parts = user_input.split()
    if len(parts) != 3:
        raise ValueError("Ошибка")

    try:
        a = int(parts[0])
        operator = parts[1]
        b = int(parts[2])
    except ValueError:
        raise ValueError("Вводите целые числа от 1 до 10")

    if not (1 <= a <= 10) or not (1 <= b <= 10):
        raise ValueError("Числа должны быть от 1 до 10 включительно.")

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
    return str(result)



if __name__ == "__main__":
    try:
        user_input = input("Input: ")
        result = main(user_input)
        print("Output:", result)
    except Exception as e:
        print(f"Ошибка: {e}")
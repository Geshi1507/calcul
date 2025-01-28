def main(user_input: str) -> str:

    parts = user_input.split()
    if len(parts) != 3:
        raise ValueError("Error")

    try:
        a = int(parts[0])
        operator = parts[1]
        b = int(parts[2])
    except ValueError:
        raise ValueError("Enter the numbers from 1 to 10")

    if not (1 <= a <= 10) or not (1 <= b <= 10):
        raise ValueError("Numbers must be between 1 and 10 inclusive.")

    if operator == '+':
        result = a + b
    elif operator == '-':
        result = a - b
    elif operator == '*':
        result = a * b
    elif operator == '/':
        if b == 0:
            raise ZeroDivisionError("Division by zero.")
        result = a // b

    else:
        raise ValueError("Invalid operation. Use +, -, * or /.")
    return str(result)



if __name__ == "__main__":
    try:
        user_input = input("Input: ")
        result = main(user_input)
        print("Output:", result)
    except Exception as e:
        print(f"Error: {e}")

def calculator():
    while True:
        try:
            # Ввод чисел
            num1 = float(input("Введите первое число: "))
            num2 = float(input("Введите второе число: "))

            # Выбор операции
            print("\nВыберите операцию:")
            print("1. Сложение (+)")
            print("2. Вычитание (-)")
            print("3. Умножение (*)")
            print("4. Деление (/)")
            print("5. Выход")

            choice = input("Ваш выбор (1/2/3/4/5): ")

            if choice == "1":
                result = num1 + num2
                print(f"Результат: {num1} + {num2} = {result}\n")

            elif choice == "2":
                result = num1 - num2
                print(f"Результат: {num1} - {num2} = {result}\n")

            elif choice == "3":
                result = num1 * num2
                print(f"Результат: {num1} * {num2} = {result}\n")

            elif choice == "4":
                try:
                    result = num1 / num2
                    print(f"Результат: {num1} / {num2} = {result}\n")
                except ZeroDivisionError:
                    print("Ошибка: деление на ноль невозможно!\n")

            elif choice == "5":
                print("Выход из программы. До свидания!")
                break

            else:
                print("Ошибка: некорректный выбор операции.\n")

        except ValueError:
            print("Ошибка: введите корректное число!\n")


if __name__ == "__main__":
    calculator()

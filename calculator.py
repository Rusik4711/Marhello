def calculator():
    while True:
        try:
            num1 = float(input("Введите первое число: "))
            num2 = float(input("Введите второе число: "))

            print("\nВыберите операцию:")
            print("1. Сложение (+)")
            print("2. Вычитание (-)")
            print("3. Умножение (*)")
            print("4. Деление (/)")
            print("5. Выход")

            choice = input("Ваш выбор (1/2/3/4/5): ")

            if choice == "1":
                print(f"Результат: {num1} + {num2} = {num1 + num2}\n")
            elif choice == "2":
                print(f"Результат: {num1} - {num2} = {num1 - num2}\n")
            elif choice == "3":
                print(f"Результат: {num1} * {num2} = {num1 * num2}\n")
            elif choice == "4":
                if num2 == 0:
                    print("Ошибка: деление на ноль!\n")
                else:
                    print(f"Результат: {num1} / {num2} = {num1 / num2}\n")
            elif choice == "5":
                print("Выход из программы.")
                break
            else:
                print("Некорректный выбор, попробуйте снова.\n")

        except ValueError:
            print("Ошибка: введите корректное число!\n")


if __name__ == "__main__":
    calculator()

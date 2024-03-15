numbers = [int(input("Введите число: ")) for _ in range(3)]
filtred_numbers = [num for num in numbers if 1 <= num <= 50]
print(f"Числа в интервале [1, 50]: {filtred_numbers}")
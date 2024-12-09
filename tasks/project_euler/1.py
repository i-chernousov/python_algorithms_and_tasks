"""
Если выписать все натуральные числа меньше 10, кратные 3 или 5, то получим 3, 5, 6 и 9. Сумма этих чисел равна 23.
Найдите сумму всех чисел меньше 1000, кратных 3 или 5.
"""

def result(multiple_number_one: int, multiple_number_two: int, natural_numbers: int) -> int:
    """
    Функция получает на вход значения и находит сумму кратных чисел
    """
    sum_number = 0

    for i in range(1, natural_numbers):
        if i % multiple_number_one == 0 or i % multiple_number_two == 0:
            sum_number += i
    else:
        return sum_number # 233168

if __name__ == "__main__":
    print(result(3, 5, 1000))


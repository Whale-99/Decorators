# Декоратор для проверки результата функции на простоту
def is_prime(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)

        # Функция для проверки, является ли число простым
        if result > 1:
            for i in range(2, int(result ** 0.5) + 1):
                if result % i == 0:
                    print("Составное")
                    break
            else:
                print("Простое")
        else:
            print("Составное")

        # Возвращаем результат работы декорируемой функции
        return result

    return wrapper


# Функция для суммирования трех чисел
@is_prime
def sum_three(a, b, c):
    return a + b + c


# Пример использования
result = sum_three(2, 3, 6)
print(result)

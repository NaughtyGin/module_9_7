def is_prime(func):
    def wrapper(a, b, c):
        result_ = func(a, b, c)
        for i in range(2, int(result_ ** 0.5) + 1):
            if result_ % i == 0:
                return f'Составное\n{result_}'
            return f'Простое\n{result_}'
    return wrapper


@is_prime
def sum_three(a, b, c):
    sum_ = a + b + c
    return sum_


result = sum_three(42, 64, 72)
print(result)

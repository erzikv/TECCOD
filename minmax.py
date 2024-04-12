def find_primes(min_num, max_num):
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
    return [n for n in range(min_num, max_num + 1) if is_prime(n)]

# Пример использования:
min_num = 10
max_num = 50
primes = find_primes(min_num, max_num)
print(f"Простые числа в диапазоне от {min_num} до {max_num}: {primes}")

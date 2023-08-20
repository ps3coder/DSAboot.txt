def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def count_prime_numbers(arr):
    count = 0
    for num in arr:
        if is_prime(num):
            count += 1
    return count

arr = [2, 3, 4, 5, 6, 7, 8, 9, 10]
result = count_prime_numbers(arr)
print(result)  # Output: 4 (2, 3, 5, 7 are prime)


print("##################################")
def is_prime(num):
    return num > 1 and all(num % i != 0 for i in range(2, int(num**0.5) +1))

Limit = 10000000
prime_tuple = tuple(num for num in range(2, limit) if is_prime(num))
print(f"so nguyen to nho hon {'Limit'}:")
print(prime_tuple)

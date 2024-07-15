def is_coprime(a, b):
    for i in range(2, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            return False
    return True

print(is_coprime(10, 27))
print(is_coprime(35, 63))
def is_prime(num):
    if num == 2 or num == 3:
        return True
    elif num % 3 == 0 or num % 2 == 0:
        return False
    elif num % 1 == 0 and num % num == 0:
        return True
    elif num % 1 == 0 and num % 2 == 0 or num % 4 == 0:
        return False
    
print(is_prime(7))
print(is_prime(4))
print(is_prime(73))
print(is_prime(75))
print(is_prime(2))
print(is_prime(3))
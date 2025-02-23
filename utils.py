def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

<<<<<<< Updated upstream
=======
def is_power_of_5(n):
    while n > 1:
        if n % 5 != 0:
            return False
        n //= 5
    return n == 1

def is_power_of_2(n):
    return n > 0 and (n & (n - 1)) == 0


>>>>>>> Stashed changes

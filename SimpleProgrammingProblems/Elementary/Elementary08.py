# Write a program that prints all prime numbers. (Note: if your programming language does not support arbitrary size numbers, printing all primes up to the largest number you can easily represent is fine too.)
def its_prime(n):

    i = 2
    if n == 1 or n == 0:
        return False
    for i in range(2, n - 1):
        if n % i == 0:
            return False
    return True


a = 100

for b in range(2, a):
    if its_prime(b):
        print(b)

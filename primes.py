"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    list = [2]
    n = 3
    while len(list) < number_of_primes:
        if n % 2 != 0:
            f = 3
            while f * f <= n:
                if n % f == 0:
                    break
                else:
                    f += 2
            else:
                list.append(n)
        n += 1
    return list

print(primes(2))
def is_prime(n):
    if n <= 1:
        return False
    elif n >= 1:
         for x in range (2, n):
            if n % x == 0:
                return False
    else:
        return True    

def primes_bellow (n):
    primes = []
    for x in range(2, n):
        if is_prime(x) == True:
            primes.append(x)
            return print(primes)

primes_bellow(18)

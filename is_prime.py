def is_prime(n):
    if n < 1:
        return print("Number is not a prime because it is less than 1")
    elif n >= 1:
         for x in range (2, n):
            if n % x == 0:
                return False
    else:
        return True    





def is_prime(n):
    if n <= 1:
        return False
    elif n > 1:
         for x in range (2, n):
            if n % x == 0:
                return False
    else:
        return True 

def is_palindrome(n):
       reversed = 0
       x = n
       while(n > 0):
        dig=n % 10
        reversed = reversed * 10 + dig
        n = n // 10
       if x == reversed:
           return True
       else:
           return False


def palindrome_prime():
    palindrome = [] 
    for x in range(10000, 99999):
        if is_prime(x) == True and is_palindrome(x) == True:
            palindrome.append(x)
            return print(palindrome) 





    
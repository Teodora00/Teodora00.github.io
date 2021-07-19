
def big_fibonacci (n):
    a = 0
    b = 0
    x = 1
    while  len(str(x)) != n:
        b = a
        a = x
        x = a + b 
    print(x)
       

big_fibonacci(2)
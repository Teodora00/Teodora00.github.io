def fibonacci_list(l):
    a = 0
    b = 1
    while True:
        a, b = b, a+b
        l.append(b)

def big_fibonacci (n):
    l = []
    fibonacci_list(l)
    for x in l:
        if len(str(x)) == n:
            first = x
            return print(first)
       

big_fibonacci(2)

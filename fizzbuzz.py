def fizzbuzz():
    for n in range(1,1000):
        if n % 3 == 0 and n % 5 == 0:
            return print("FizzBuzz")
        elif n % 3 == 0:
            return print("Fizz")    
        elif  n % 5 == 0:
            return print("Buzz")
        else:
            print(n)


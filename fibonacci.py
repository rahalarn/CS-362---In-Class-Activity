def Fib(n):
    if n < 0:
        print("Invalid input!")
        return 0
    elif n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else: 
       return Fib(n - 1) + Fib(n - 2)


def Fac(n):
    if n < 0:
        print("Invalid input!")
        return 0
    elif n == 0 or n == 1:
        return 1
    else:
        return n * Fac(n - 1)

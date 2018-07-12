def fib_no(n):
    a = 1
    b = 0
    i = 1
    n = input ('Please enter the number of Fibonacci numbers:')
    N=int(n)
    while i != N :
        c = a + b
        i + 1
        a = b
        b = c
        i = i + 1
    return c

n = 0
print (fib_no(n))


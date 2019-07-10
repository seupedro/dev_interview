
def fib(n):
    a, b = 0, 1
    result = 0

    print(a)
    print(b)

    while result < n:
        result = a + b
        print(result)

        a = b
        b = result


fib(10)

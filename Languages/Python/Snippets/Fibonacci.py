#!/usr/bin/env python3

def fibonacci(number, display = False, returnAll = False):
    a = 0
    b = 1
    fib = 0
    result = [0, 1]
    if ((display) & (number >= 0)):
        print(a)
    if ((display) & (number >= 1)):
        print(b)
    for x in range(number - 1):
        fib = a + b
        if (display):
            print(fib)
        if (returnAll):
            result.append(fib)
        a = b
        b = fib
    if (returnAll):
        return result
    else:
        return [fib]

result = fibonacci(100, False, True)
for x in range(len(result)):
    print(result[x])
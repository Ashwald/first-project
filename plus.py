def sqr(c):
    return c**2

def plus(a=1, b=2):
    result = a + b

    return sqr(result)


plus(4, 6)
t = plus(4, 1) + 99
print(t)



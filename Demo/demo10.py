# 生成器

L = [x * x for x in range(10)]

g = (x * x for x in  range(11))

print(g)

def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        # print(b)
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'

fib(6)
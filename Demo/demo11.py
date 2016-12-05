# 高阶函数

# 这就叫高阶函数 ， 传进去一个方法
def add(x, y, f):
    return f(x) + f(y)

# 返回一个函数
def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum

print(lazy_sum)

# 我们调用lazy_sum()时，每次调用都会返回一个新的函数，即使传入相同的参数
f1 = lazy_sum(1, 3, 5, 7, 9)
f2 = lazy_sum(1, 3, 5, 7, 9)
print(f1==f2)

# 返回函数不要引用任何循环变量，或者后续会发生变化的变量
def count():
    fs = []
    for i in range(1, 4):
        def f():
             return i*i
        fs.append(f)
    return fs

f1, f2, f3 = count()
# 这里 f1 f2 f3 最后输出结果都是9
# 改进
def count():
    def f(j):
        def g():
            return j*j
        return g
    fs = []
    for i in range(1, 4):
        fs.append(f(i)) # f(i)立刻被执行，因此i的当前值被传入f()
    return fs

f1, f2, f3 = count()
print(f1(),f2(),f3())
# 小结

# 一个函数可以返回一个计算结果，也可以返回一个函数。

# 返回一个函数时，牢记该函数并未执行，返回函数中不要引用任何可能会变化的变量
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 利用递归函数计算阶乘
# N! = 1 * 2 * 3 * ... * N

def fact(n):
    if n==1:
        return 1
    return n * fact(n - 1)

# 尾递归优化
def fact(n):
    return fact_iter(n, 1)

def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)

# 利用递归函数移动汉诺塔:
def move(n, a, b, c):
    if n <= 0:
        return
    if n == 1:
        print('move', a, '-->', c)
        return
    move(n - 1, a, c, b)

    print('move', a, '-->', c)

    move(n - 1, b, a, c)

move(3, 'A', 'B', 'C')
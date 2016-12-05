# 循环便利
# Python叫迭代器

d = {'a': 'qq', 'b': 'bb', 'c': '3'}

for e in d :
    print(e + ',')


#  字符串也可以迭代
for c in 'ABCDEFG':
    print(c)

# 判断一个对象是否可以被迭代
from collections import Iterable
print(isinstance('abc', Iterable))

#  如何取下标
for i, value in enumerate(['A', 'B', 'C']):
    print(i, value)

for key, value in enumerate(d) :
    print(key , value)
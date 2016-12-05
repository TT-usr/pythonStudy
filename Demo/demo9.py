#  list
print(list(range(1, 11)))

# [1x1, 2x2, 3x3, ..., 10x10]
print([x * x for x in range(1, 11)])

# 打印偶数
print([x for x in range(1, 11) if x % 2 == 0])

# 两层循环
print([m + n for m in 'ABC' for n in 'XYZ'])

import os
# os.listdir可以列出文件和目录
# print([d for d in os.listdir(.)])

# 遍历字典
d = {'x': 'A', 'y': 'B', 'z': 'C' }
for k, v in d.items():
     print(k, '=', v)

# 同等
print([k + '=' + v for k, v in d.items()])

L = ['Hello', 'World', 'IBM', 'Apple']
# lower
print([s.lower() for s in L])

L = ['Hello', 'World', 18, 'Apple', None]
L2 = []
for item in L :
    if isinstance(item, str):
       L2.append(item)

print(L2)


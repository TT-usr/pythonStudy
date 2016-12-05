# 切片
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
# 取前三
print(L[0:3])
# 索引还可以是负数
# Python支持L[-1]取倒数第一个元素
print(L[-1:])
# 记住倒数第一个元素的索引是-1

# 这样可以创建0 ~ 99 的数组
L = list(range(100))

# 复制一个list
M = L[:]

print(M)

# 切片可以截取字符串
print('ABCDEFG'[:3])



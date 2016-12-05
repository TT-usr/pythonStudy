#dict
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print(d)

# 存储 提取 均和其他都一样

#判断dict里面是否有该key
# 1. in
print('Bob' in d)
#2. get 如果key不存在，默认返回None，或者自己指定的value
print(d.get('Tracy0' ,0))


d.pop('Bob')

print(d)

#set集合

# 要创建一个set，需要提供一个list作为输入集合：
# 重复元素在set中自动被过滤：
s = set([1, 2, 3, 1, 2, 12])
print(s)
# add(key)
# remove(key)

# 并集或者交集  & 或者 |
# 譬如 s & s1 并集

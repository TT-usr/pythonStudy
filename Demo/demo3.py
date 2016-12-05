#循环
names = ['Michael', 'Bob', 'Tracy']

for name in names:
    print(name)

#range(101)就可以生成0-100的整数序列
sum = 0
for x in range(101):
    sum = sum + x
print(sum)

#while
sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n - 2
print(sum)

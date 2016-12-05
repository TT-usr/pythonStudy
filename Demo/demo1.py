print('hello world')

#list
classMate = ['1' , '2', '3']
print(classMate)

#拼接
classMate.append('3')
print(len(classMate))
print(classMate[0])

#插入
classMate.insert(2,'34')
print(classMate)

#删除 如果（）为空，默认删除最后一位
classMate.pop()
print(classMate)

#tuple 初始化后不可更改
classmates = ('Michael', 'Bob', 'Tracy')
print(classmates)

#空的tuple
temp = ()

#tuple 内放list
temp1 = ('1','2' , ['3', '4'])
print(temp1)



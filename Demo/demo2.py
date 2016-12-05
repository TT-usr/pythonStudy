#if

a = 20
if a >= 20:
    print('20啦')
else:
    print('不到20')

if a >= 20:
    print("lalal")
    print("测试if")


# if <条件判断1>:
#     <执行1>
# elif <条件判断2>:
#     <执行2>
# elif <条件判断3>:
#     <执行3>
# else:
#     <执行4>

x = 0
if x:
    print('True')
# 只要x是非零数值、非空字符串、非空list等，就判断为True，否则为False。


#input 获取用户输入数据
s = input('birth: ')
# input返回的是string 需要转换int类型
birth = int(s)
if birth < 2000:
    print('00前')
else:
    print('00后')

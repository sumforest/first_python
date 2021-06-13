# 元组不可变指的是元组所指向的内存中的内容不可变
tup = (1,2,3,4,5)

# tup[0] = 100

'''
报错
Traceback (most recent call last):
  File "d:\codeHub\first_python\tupleDemo3.py", line 4, in <module>
    tup[0] = 100
TypeError: 'tuple' object does not support item assignment
'''
print(tup)
# tup内存地址： 1336677260800
print("tup内存地址：",id(tup))

tup = ('a','b','c')
# tup内存地址： 1336682018496
print("tup内存地址：",id(tup))
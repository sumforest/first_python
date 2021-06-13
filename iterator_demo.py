import sys

list = [1,2,3,4,5]
it = iter(list)
print(next(it))

print('*'*30)
# for循环遍历迭代器
list = ['a','b','c','d','e']
it = iter(list)
for x in it:
    print(x,end=',')

print('\n')
print('*'*30)
# while循环遍历迭代器
# list = [6,7,8,9,10]
# it = iter(list)
# while True:
#     try:
#         print(next(it),end=',')
#     except StopIteration:
#         sys.exit()

print('\n')
print('*'*30)
# 创建一个迭代器
class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        x = self.a
        self.a +=1
        return x

myclass = MyNumbers()
myit = iter(myclass)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))

print('\n')
print('*'*30)

# StopIteration
class MyNumbers2:
    def __iter__(self):
        self.a = 1
        return self
    
    def __next__(self):
        x = self.a
        if x <= 20:
            self.a += 1
            return x
        else:
            raise StopIteration

myclass2 = MyNumbers2()
myit2 = iter(myclass2)
for x in myit2:
    print(x,end=",")

print('\n')
print('*'*30)
# 以下实例使用 yield 实现斐波那契数列：
def fibonacci(n):
    a,b,count=0,1,0
    while True:
        if count > n:
            return
        yield a
        a,b=b,a+b
        count +=1
# f是一个迭代器对象有生成器返回
f = fibonacci(10)
while True:
    try:
        print(next(f),end=',')
    except:
        sys.exit()
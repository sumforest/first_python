def change(a):
    print('还没改变前a的地址：',id(a))
    a = 10
    print('改变后a的地址：',id(a))


a = 1
print('函数传递前a的地址：',id(a))
change(a)
# 由此可见不可改变类型在函数传递过程中传递的是同一个地址的值，
# 在函数中改变后的指向的是一个新的地址空间，不会影响函数外的值.

print('-'*50)

def changeme(myList):
    # 修改传进来的列表
    myList.append([4,5,6])
    print('修改后的列表:',myList)
    return

myList = [1,2,3]
print('修改前的list:',myList)
changeme(myList)
print('修改后的原参数list:',myList)
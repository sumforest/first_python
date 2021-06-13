# 输入一个立方表
for x in range(1,11):
    print(repr(x).rjust(2),repr(x*x).rjust(3),end=' ')
    print(repr(x*x*x).rjust(4))

for x in range(1,11):
    print('{0:2d} {1:3d} {2:4d}'.format(x,x*x,x*x*x))

# 在:后面跟数字可以保证宽度
table = {'Google':1,'Runoob':2,'Alibaba':3}

for k,v in table.items():
    print('{0:10}===>{1:10}'.format(k,v))

print('-'*10)
print('Google: {0[Google]:d}; Runoob: {0[Runoob]:d}; Alibaba:{0[Alibaba]:d}'.format(table))

print('-'*10)
print('Google:{Google:d};Runoob:{Runoob};Alibaba:{Alibaba}'.format(**table))

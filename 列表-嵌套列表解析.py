# 3行4列矩阵转换成4行3列矩阵
matrix = [
 [1, 2, 3, 4],
 [5, 6, 7, 8],
 [9, 10, 11, 12],
]
for i in range(4):
    print(i)
print('-'*10)
for i in range(1,4):
    print(i) 
# 外循环驱动内循环，右边是外循环，左边是内循环
print([[row[i] for row in matrix] for i in range(4)])
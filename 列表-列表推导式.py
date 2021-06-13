# 将列表中每个数值乘三，获得一个新的列表：
vec = [3,6,9]
print([x*3 for x in vec])

# 得到一个嵌套列表
print([[x,x*2] for x in vec])

# 对序列里每一个元素逐个调用某方法：
freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
print([fruit.strip() for fruit in freshfruit])

# 使用if做过滤条件
print([x for x in vec if x > 3])

# 循环和其它技巧的演示：
vec1 = [1,2,3]
vec2 = [2,-3,4]
print([x*y for x in vec1 for y in vec2])

# 使用复杂表达式或嵌套函数：
print([str(round(355/113,i)) for i in range(1,6)])
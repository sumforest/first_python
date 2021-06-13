knights = {'gallahad': 'the pure', 'robin': 'the brave'}

for k,v in knights.items():
    print(k,v)

# 在序列中遍历时，索引位置和对应值可以使用 enumerate() 函数同时得到：
for index,v in enumerate([4,5,6]):
    print(index,v)

# 同时遍历两个或更多的序列，可以使用 zip() 组合：
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q,a in zip(questions,answers):
    print(q,a)
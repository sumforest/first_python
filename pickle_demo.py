import pickle,pprint

# data1 = {'a': [1, 2.0, 3, 4+6j],
#          'b': ('string', u'Unicode string'),
#          'c': None}
# list = [1,2,3]
# list.append(list)

# # 以读写二进制的方式打开文件
# output = open('D:\codeHub\\first_python\\data.pkl','wb')

# # 序列化
# pickle.dump(data1,output)
# # 指定协议序列化
# pickle.dump(list,output,-1)

# output.close

# 反序列化
input = open('D:\codeHub\\first_python\\data.pkl','rb')

res1 = pickle.load(input)
pprint.pprint(res1)

resList = pickle.load(input)
pprint.pprint(resList)


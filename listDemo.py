list = ['aabb',3.14,'helloworld',288,2333]
tiny_list = ['lucky','新冠快滚']

print(list)
print(list[1])
print(list*2)
print(list[2:])
print(list+tiny_list)

print('\n','*'*50,'\n')
def reversWords(input):
    inputWords = input.split(' ')
    # 第一个参数表示最后一个元素
    # 第二个参数为空，表示移动到列表末尾
    # 第三个参数为步长，-1表示逆向
    inputWords = inputWords[-1::-1]

    # 重新组合字符串
    return ' '.join(inputWords)

input = 'I like Runoob'
print(reversWords(input))

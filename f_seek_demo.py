# 以二进制读写的方式打开文件
f = open('D:\codeHub\\first_python\\foo.txt','wb+')
content = b'0123456789abcdef'
print(f.write(content))
# 从开始位置移动5个字节
print(f.seek(5))
# 读取一个字节
print(f.read(1))
# 移动到倒数第三个字节
print(f.seek(-3,2))
# 读取一个字节
print(f.read(1))
f.close

f = open('test.txt', 'wb')
f.write("hello 你好".encode('utf-8'))
f.close()

f1 = open('test.txt', 'r')
print(f1.read())
print(type(f1.read()))
f1.close()
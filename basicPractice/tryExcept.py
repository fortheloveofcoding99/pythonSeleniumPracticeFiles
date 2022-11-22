
try:
    with open('nofile.txt','r') as reader:
        c1 = reader.readlines()
except Exception as e:
    print(e)


try:
    with open('nofile.txt','r') as reader:
        c2 = reader.readlines()
except:
    print("no such file custom message")
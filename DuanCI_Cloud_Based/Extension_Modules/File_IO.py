#coding=UTF-8
def inFile(FilePath):
    FilePath = str(FilePath).replace('\\', '/').replace('\"', '')
    with open(FilePath, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        # 删除空行并去除每行的首尾空白字符
        non_empty_lines = [line.strip() for line in lines if line.strip()]
    return '\n'.join(non_empty_lines)

def outFile(FilePath):
    print("outFile")

'''
filename = str(input())
outFile = open(filename, 'r')
index = outFile.read()
print(index)
'''

'''
filename = str(input())
outFile = open(filename, 'w')
outFile.write("Hello from python fstream\n")
outFile.flush()

try:
    while True:
        outFile.write(input())
        outFile.write('\n')
        outFile.flush()

except EOFError:
    pass

outFile.close()
'''
#coding=UTF-8
import os

def inFile(FilePath):
    FilePath = str(FilePath).replace('\\', '/').replace('\"', '')
    with open(FilePath, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        non_empty_lines = [line.strip() for line in lines if line.strip()]

    return '\n'.join(non_empty_lines)

def outFile(FilePath, index):
    FilePath = str(FilePath).replace('\\', '/').replace('\"', '')
    FilePath = list(FilePath.split('/'))
    
    FileName = FilePath[-1]
    base, ext = os.path.splitext(FileName)
    FileName = f"{base}_ADCI{ext}"

    DirPath = FilePath
    DirPath.pop()
    DirPath.append("AutoDCI_Document")
    
    DirPath = '/'.join(DirPath)
    NewFilePath = DirPath + f"/{FileName}"

    if not(os.path.isdir(DirPath)):
        os.mkdir(DirPath)

    print(DirPath)
    print(NewFilePath)

    with open(NewFilePath, 'w', encoding='utf-8') as file:
        file.write(index)

# print(inFile(input()))
# outFile(input())

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
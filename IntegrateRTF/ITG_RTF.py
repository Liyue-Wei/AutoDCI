import os
from spire.doc import *
from spire.doc.common import *

def RTF_to_DOCX(folderPATH, fileLIST, NewFolder):
    print("Converting RTF to DOCX...")
    print(folderPATH)
    print(fileLIST)
    print(NewFolder)
    for file in fileLIST:
        filePATH = f"{folderPATH}/{file}" if ".rtf" in file else None
        print(filePATH)
        
        if filePATH != None:
            fileNAME = filePATH.split("/")[-1].split(".")[0]
            print(fileNAME)
            Function(NewFolder, filePATH, fileNAME)

def Function(NewFolder, filePATH, fileNAME):
    doc = Document()
    doc.LoadFromFile(filePATH)
    doc.SaveToFile(f"{NewFolder}/{fileNAME}.docx", FileFormat.Docx)
    doc.Close()

def readFolder(folderPATH):
    global fileLIST, NewFolder
    fileLIST = []
    print("Reading folder...")
    # print(folderPATH)
    if not os.path.isdir(folderPATH):
        print("The folder does not exist.")
        return None
    
    else:
        try:
            NewFolder = f"{folderPATH}/ITG_RTF_Documents"
            os.mkdir(NewFolder)

        except:
            None

        for file in os.listdir(folderPATH):
            fileLIST.append(file)

    return NewFolder, fileLIST

def main():
    print("IntegrateRTF: RTF to DOCX")
    folderPATH = input("Please input the path of the folder: ").replace("\\", "/").replace('"', '')
    readFolder(folderPATH)
    RTF_to_DOCX(folderPATH, fileLIST, NewFolder)

if __name__ == "__main__":
    main()  

'''
filePATH = input("Please input the path of the RTF file: ").replace("\\", "/").replace('"', '')
fileNAME = filePATH.split("/")[-1].split(".")[0].split('-')
fileNAME = ''.join(fileNAME) + ".docx"

doc = Document()
doc.LoadFromFile(filePATH)
doc.SaveToFile(fileNAME, FileFormat.Docx)
doc.Close()
'''
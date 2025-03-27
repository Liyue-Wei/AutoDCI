from Extension_Modules import file_directory as fd
from Extension_Modules import File_IO as fio
from spire.doc import *
from spire.doc.common import *

filePATH = input("Please input the path of the RTF file: ").replace("\\", "/").replace('"', '')
fileNAME = filePATH.split("/")[-1].split(".")[0].split('-')
fileNAME = ''.join(fileNAME) + ".docx"

doc = Document()
doc.LoadFromFile(filePATH)
doc.SaveToFile(fileNAME, FileFormat.Docx)
doc.Close()
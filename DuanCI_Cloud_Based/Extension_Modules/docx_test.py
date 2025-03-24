from docx import Document

def Read_Docx(filePath):
    try:
        filePath = str(filePath).replace('\\', '/').replace('\"', '')
        document = Document(filePath)
        text = []
        for paragraph in document.paragraphs:
            text.append(paragraph.text)

        for item in text:
            if item == '':
                text.remove(item)

        return text

    except Exception as e:
        return e
    
print(Read_Docx(input()))
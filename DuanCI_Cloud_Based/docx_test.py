import docx

def read_word_file_by_paragraph(file_path):
    """逐段落讀取 Word 檔案並返回段落列表"""
    try:
        doc = docx.Document(file_path)
        paragraphs = [para.text for para in doc.paragraphs if para.text.strip()]  # 過濾空段落
        return paragraphs
    except FileNotFoundError:
        return ["檔案未找到"]
    except Exception as e:
        return [f"發生錯誤：{e}"]

def remove_extra_blank_lines_from_paragraphs(paragraphs):
    """移除段落中的多餘空行，保留最多一行空行"""
    cleaned_paragraphs = []
    for paragraph in paragraphs:
        lines = paragraph.splitlines()
        cleaned_lines = []
        blank_count = 0

        for line in lines:
            if line.strip() == "":  # 判斷是否為空行
                blank_count += 1
            else:
                blank_count = 0  # 重置空行計數

            # 只允許最多一行空行
            if blank_count <= 1:
                cleaned_lines.append(line)

        cleaned_paragraphs.append('\n'.join(cleaned_lines))  # 清理後的段落
    return cleaned_paragraphs

# 替換成您的 Word 檔案路徑
file_path = "C:/Users/eric2/Downloads/drive-download-20250321T032103Z-001/黃元辰.docx"
paragraphs = read_word_file_by_paragraph(file_path)

# 移除每個段落中的多餘空行
cleaned_paragraphs = remove_extra_blank_lines_from_paragraphs(paragraphs)

# 將每個段落逐段寫入 test.txt
output_file = "test.txt"
with open(output_file, "w", encoding="utf-8") as f:
    for paragraph in cleaned_paragraphs:
        f.write(paragraph + "\n\n")  # 每個段落之間保留一個空行

# 確保 cleaned_paragraphs 是單一變數
def IO():
    return "\n\n".join(cleaned_paragraphs)
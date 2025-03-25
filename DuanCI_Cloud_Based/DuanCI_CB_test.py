#coding=UTF-8
start = False
while(start==False):
    try:
        import os
        import docx
        from selenium import webdriver
        from selenium.webdriver.common.by import By
        from selenium.webdriver.chrome.options import Options
        from selenium.webdriver.chrome.service import Service
        start = True

    except ImportError:
        print("ERROR : Essential modules not found")
        from Extension_Modules import install
        install.main()  
        os.system("PAUSE") 

from Extension_Modules import file_directory as fd
import time
import threading

from Extension_Modules import File_IO

opt = Options()
# opt.add_experimental_option("detach", True)
# opt.add_argument("--headless")

path = fd.path_function("\chromedriver-win64\chromedriver.exe")

print(path)
driver = webdriver.Chrome(service=Service(path), options=opt)
driver.get("https://ckip.iis.sinica.edu.tw/service/ckiptagger/")

element_strIN = driver.find_element(By.XPATH, "/html/body/textarea[4]")
element_strOUT = driver.find_element(By.XPATH, "/html/body/textarea[5]")
element_unSEL_1 = driver.find_element(By.XPATH, "/html/body/label[4]/input").click()
element_unSEL_2 = driver.find_element(By.XPATH, "/html/body/label[5]/input").click()
element_button = driver.find_element(By.XPATH, "/html/body/button")

def strIO(fileIN):
    element_strIN.clear()
    element_strOUT.clear()

    element_strIN.send_keys(str(fileIN))
    element_button.click()

    fileOUT = element_strOUT.get_attribute("value")
    start_time = time.time()
    while fileOUT == '':
        timer = time.time() - start_time
        # print(timer)
        if timer > 10:
            raise TimeoutError("Error: Time OUT")

        fileOUT = element_strOUT.get_attribute("value")
    
    return fileOUT

def split_into_parts(text, parts):
    """
    将文本分成指定数量的部分。
    :param text: 要分割的文本
    :param parts: 分割的部分数量
    :return: 分割后的文本列表
    """
    length = len(text)
    part_size = length // parts
    split_text = [text[i * part_size:(i + 1) * part_size] for i in range(parts - 1)]
    split_text.append(text[(parts - 1) * part_size:])  # 添加最后一部分
    return split_text

def save_to_file(original_path, content):
    """
    将处理后的内容存储到新文件中，文件名加上 "ADCI"。
    :param original_path: 原始文件路径
    :param content: 处理后的内容
    """
    import os
    # 去除路径中的多余引号
    original_path = original_path.strip('"')
    base, ext = os.path.splitext(original_path)
    new_file_path = f"{base}_ADCI{ext}"

    # 将内容写入新文件
    with open(new_file_path, 'w', encoding='utf-8') as file:
        file.write(content)
    print(f"处理后的内容已保存到文件：{new_file_path}")

def main():
    # 读取文件内容并删除空行
    file_path = input("请输入文件路径：")
    index = File_IO.inFile(file_path)
    print("原始内容：")
    print(index)

    # 动态分段并处理
    parts = 8  # 分成的部分数量
    length = len(index)
    part_size = length // parts

    print("\n动态分段处理内容：")
    processed_content = ""  # 用于存储处理后的所有内容
    for i in range(parts):
        # 计算当前段的内容
        start = i * part_size
        end = (i + 1) * part_size if i < parts - 1 else length
        part = index[start:end]

        print(f"处理第 {i + 1} 部分：")
        print(part)
        print("-" * 20)

        # 将当前段传递给 strIO
        result = strIO(part)
        print(result)

        # 将处理后的结果拼接到总内容中
        processed_content += result + "\n"

    # 保存处理后的内容到新文件
    save_to_file(file_path, processed_content)

if __name__ == "__main__":
    main()
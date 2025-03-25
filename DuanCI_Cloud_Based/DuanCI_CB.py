#coding=UTF-8
start = False
while(start==False):
    try:
        import os
        import pyautogui
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
from Extension_Modules import File_IO as fio
import time

opt = Options()
# opt.add_experimental_option("detach", True)
# opt.add_argument("--headless")

path = fd.path_function("\chromedriver-win64\chromedriver.exe")

print(path)
driver = webdriver.Chrome(service=Service(path), options=opt)
driver.get("https://ckip.iis.sinica.edu.tw/service/ckiptagger/")

element_strIN = driver.find_element(By.XPATH, "/html/body/textarea[4]")
element_strOUT = driver.find_element(By.XPATH, "/html/body/textarea[5]")
element_button = driver.find_element(By.XPATH, "/html/body/button")

def initialize():
    global element_strIN, element_strOUT, element_button
    driver.find_element(By.XPATH, "/html/body/label[4]/input").click()
    driver.find_element(By.XPATH, "/html/body/label[5]/input").click()
    element_strIN = driver.find_element(By.XPATH, "/html/body/textarea[4]")
    element_strOUT = driver.find_element(By.XPATH, "/html/body/textarea[5]")
    element_button = driver.find_element(By.XPATH, "/html/body/button")

def strIO(fileIN):
    print("strIO")
    element_strIN.clear()
    element_strOUT.clear()

    element_strIN.send_keys(str(fileIN))
    element_button.click()

    fileOUT = element_strOUT.get_attribute("value")
    start_time = time.time()
    while fileOUT == '':
        timer = time.time() - start_time
        # print(timer)
        if timer > 15:
            raise TimeoutError("Error: Time OUT")

        fileOUT = element_strOUT.get_attribute("value")
    
    return fileOUT

def OpenFolder(file_folder):
    print("Open Folder")
    global Files_List

    try:
        Files_List = [f for f in os.listdir(file_folder) if os.path.isfile(os.path.join(file_folder, f))]
    
    except Exception as e:
        print(f"An error occurred: {e}")
        os.system("PAUSE")

def split_into_parts(fileIN):
    fileLength = len(fileIN)
    print(fileLength)
    if fileLength < 40000:
        parts = 8
        partSize = fileLength // parts

    else:
        parts = 8 * int(fileLength / 40000)
        partSize = fileLength // parts
        print(parts)
        print(partSize)
        
    split_text = [fileIN[i * partSize:(i + 1) * partSize] for i in range(parts - 1)]
    split_text.append(fileIN[(parts - 1) * partSize:])
    return split_text

def main():
    initialize()
    file_folder = input("Please input the file folder: ")
    OpenFolder(file_folder)
    for file in Files_List:
        print(file)
        fileIN = fio.inFile(f"{file_folder}/{file}")
        # partition(fileIN)
        index = split_into_parts(fileIN)
        fileOUT = []

        for i in range(len(index)):
            print(i)
            if (i % 15 == 0 and i != 0):
                print("Refreshing")
                driver.refresh()
                initialize()
                
            # print(index[i])
            fileOUT.append(strIO(index[i]))

        fileOUT = '\n'.join(fileOUT)
        fio.outFile(f"{file_folder}/{file}", fileOUT)

if __name__ == "__main__":
    main()
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

def main():
    # print(strIO("這是一份測試文件"))
    index = File_IO.inFile(input())
    print(index)
    print(len(index))
    # print(strIO(index))

if __name__ == "__main__":
    main()
from Extension_Modules import file_directory as fd
import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

opt = Options()
# opt.add_experimental_option("detach", True)
opt.add_argument("--headless")

path = fd.path_function("\chromedriver-win64\chromedriver.exe")
print(path)
driver = webdriver.Chrome(service=Service(path), options=opt)
driver.get("https://ckip.iis.sinica.edu.tw/service/ckiptagger/")

element_strIN = driver.find_element(By.XPATH, "/html/body/textarea[4]")
element_strOUT = driver.find_element(By.XPATH, "/html/body/textarea[5]")
element_unSEL_1 = driver.find_element(By.XPATH, "/html/body/label[4]/input")
element_unSEL_2 = driver.find_element(By.XPATH, "/html/body/label[5]/input")
element_button = driver.find_element(By.XPATH, "/html/body/button")

element_strIN.clear()
element_unSEL_1.click()
element_unSEL_2.click()

element_strIN.send_keys("餐廳評論分析系統 輸入一則關於餐廳的中文評論，系統會根據菜名及情緒字典等語彙庫偵測出評論對象和內容，再透過依存句法分析找出評論對象與內容的組合，判斷每一組評價內容的正負面。")
element_button.click()
time.sleep(1)
TEXT = element_strOUT.get_attribute("value")
print(TEXT)
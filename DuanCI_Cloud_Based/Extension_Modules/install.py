import os

def main():  
    modules = ["selenium", "python-docx", "pyautogui"]  
    print("preparing to install {}".format(modules))
    for i in range(0, len(modules)):
        os.system("pip install "+modules[i])

if __name__ == "__main__":
    main()
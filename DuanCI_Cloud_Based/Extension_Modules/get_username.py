import os 

def main():
    dir_path = os.path.dirname(__file__)
    path_list = dir_path.split("\\")
    return(path_list[2])

if __name__ == "__main__":
    main()
import os

def rename_all_child_files(path : str):
    if not os.path.isdir(path):
        return
    files = os.listdir(path)
    for i in files:
        if os.path.isdir(path+"/"+i):
            rename_all_child_files(path+"/"+i)
        os.rename(path+"/"+i , path + "/"+i.replace(" ","_"))

while True:
    path_to_serach = input("Enter the path to the parent folder")
    if os.path.isdir(path_to_serach):
        break

rename_all_child_files(path_to_serach)

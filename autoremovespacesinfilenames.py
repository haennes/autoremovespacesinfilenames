import os

def rename_all_child_files(path : str):
    if not os.path.isdir(path):
        return
    files = os.listdir(path)
    for i in files:
        if os.path.isdir(path+"/"+i):
            rename_all_child_files(path+"/"+i)
        os.rename(path+"/"+i , path + "/"+i.replace(" ","_"))

rename_all_child_files("/home/hannes/Documents")

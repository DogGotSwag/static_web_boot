import os
import shutil

def copy_files_and_dir_recursive(source, destination):
    files_and_dirs = os.listdir(source)
    for file_or_dir in files_and_dirs:
        curr = os.path.join(source, file_or_dir)
        if os.path.isfile(curr):
            shutil.copy(curr, destination)
        else:
            path = os.path.join(destination, file_or_dir)
            os.mkdir(path)
            copy_files_and_dir_recursive(curr,path)

def src_dir_to_des_dir():
    destination = './public'
    if os.path.exists(destination):
        shutil.rmtree(destination)
    os.mkdir(destination)
    copy_files_and_dir_recursive('./static', './public')

src_dir_to_des_dir()
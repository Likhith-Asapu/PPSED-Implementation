import glob
import os
import shutil

files = glob.glob('server/*')
for file_name in files:
    os.remove(file_name)

files = glob.glob('user/*')
for file_name in files:
    os.remove(file_name)

files = glob.glob('user copy/*')
for file_name in files:
    shutil.copyfile(file_name,"user/"+file_name[10:])


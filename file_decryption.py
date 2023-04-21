from one_time_pad import *
import os

def decrypt_file(file_name,user_dir):
    if os.path.isfile(user_dir+file_name):
        file_read = open(user_dir+file_name,"r")
        string = file_read.read()

        file_key = open(user_dir+file_name[:-4]+".key","r")
        key = file_key.read()

        text = decrypt_string(string,key)
        
        file_write = open(user_dir+file_name[:-4]+".txt","w")
        file_write.write(text)
        file_write.close()
        file_read.close()
        file_key.close()
        file_read.close()
    else:
        print("File not found")
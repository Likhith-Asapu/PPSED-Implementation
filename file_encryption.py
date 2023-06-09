from one_time_pad import *
import os
# Code for Encrypting a file and sending it to the server

def encrypt_file(file_name,mobile=False):
    if os.path.isfile("user/"+file_name):
        file_read = open("user/"+file_name,"r")
        string = file_read.read()
        encrypted_string,key = encrypt_string(string)
        file_write = open("server/"+file_name[:-4]+".enc","w")
        file_write.write(encrypted_string)
        file_write.close()

        file_write = open("user/"+file_name[:-4]+".key","w")
        file_write.write(key)
        file_write.close()

        if mobile:
            file_write = open("user_mobile/"+file_name[:-4]+".key","w")
            file_write.write(key)
            file_write.close()

        file_read.close()

        os.remove("user/"+file_name)
    else:
        print("File not found")
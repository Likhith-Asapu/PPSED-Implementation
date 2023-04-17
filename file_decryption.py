from imports_and_libraries import *

def decrypt_file(file_name):
    if os.path.isfile("user/"+file_name):
        file_read = open("user/"+file_name,"r")
        string = file_read.read()

        file_key = open("user/"+file_name[:-4]+".key","r")
        key = file_key.read()

        text = decrypt_string(string,key)
        
        file_write = open("user/"+file_name[:-4]+".txt","w")
        file_write.write(text)
        file_write.close()
        file_read.close()
        file_key.close()
        file_read.close()
    else:
        print("File not found")

if __name__ == "__main__":

    print("Enter name of the file for decryption: ",end="")
    file_name = input()
    decrypt_file(file_name)

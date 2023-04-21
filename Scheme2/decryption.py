import sys
sys.path.append('../')
from file_decryption import *

if __name__ == "__main__":

    print("Enter name of the file for decryption: ",end="")
    file_name = input()
    decrypt_file(file_name,"user_mobile/")
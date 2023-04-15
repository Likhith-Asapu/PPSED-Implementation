from imports_and_libraries import *

def user_retrieve_files(keyword):
    try:
        index = word_indices['word_to_index'][keyword]
    except:
        print("Keyword not found in Dictionary")
        return None,None
    p = pseudo_random_permutation(s,index,d)
    f = pseudo_random_function(r,p,d,t)
    return p,f

def server_retrieve_files(p,f,number_of_files):

    length = 2 ** d
    for j in range(number_of_files):
        file_read = open("server/{}.enc".format(j + 1),"r")
        text = file_read.read()
        M = text[-2 ** d:]
        if int(M[p]) ^ pseudo_random_bit(f,j):
            file_write = open("user/{}.enc".format(j + 1),"w")
            file_write.write(text[:-2 ** d])
            file_write.close()
            print("Retrieved file {}.enc".format(j + 1))
        file_read.close()

def retrieve_files(keyword):
    p,f = user_retrieve_files(keyword)
    if p != None and f != None:
        server_retrieve_files(p,f,NUMBER_OF_FILES)

if __name__ == "__main__":
    file_read = open("user/s.txt","r")
    s = file_read.read()
    file_read.close()
    file_read = open("user/r.txt","r")
    r = file_read.read()
    file_read.close()
    
    print("Enter keyword: ",end="")
    keyword = input()
    retrieve_files(keyword)

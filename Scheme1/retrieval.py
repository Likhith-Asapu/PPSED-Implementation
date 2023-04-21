from imports_and_libraries import *
import glob

def user_retrieve_files(keyword):
    file_open = open('user/word_indices.json')
    word_indices = json.load(file_open)
    try:
        index = word_indices['word_to_index'][keyword]
    except:
        print("Keyword not found in Dictionary")
        return None,None
    p = pseudo_random_permutation(s,index,d)
    f = pseudo_random_function(r,p,d,t)
    return p,f

def server_retrieve_files(p,f):

    length = 2 ** d
    # read json file
    files = glob.glob('server/*.enc')
    for file_name in files:
        file_read = open(file_name,"r")
        text = file_read.read()
        j = int(text[-NUMBER_OF_FILE_BITS:],2)
        M = text[-(2 ** d + NUMBER_OF_FILE_BITS): -NUMBER_OF_FILE_BITS]
        if int(M[p]) ^ pseudo_random_bit(f,j,t):
            file_write = open("user/{}".format(file_name[7:]),"w")
            file_write.write(text[:-(2 ** d + NUMBER_OF_FILE_BITS)])
            file_write.close()
            print("Retrieved file {}".format(format(file_name[7:])))
        file_read.close()

def retrieve_files(keyword):
    p,f = user_retrieve_files(keyword)
    if p != None and f != None:
        server_retrieve_files(p,f)

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

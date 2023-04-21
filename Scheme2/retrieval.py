from imports_and_libraries import *
import glob

def server_retrieve_phi(phi):

    length = 2 ** d
    # read json file 
    
    f = open('server/phi.json')
    words = json.load(f)
    found = False
    for p in range(len(words["phi_values"])):
        if phi == words["phi_values"][p]:
            found = True
            break
    if found:
        return p
    else:
        print("Keyword not found")

    return None

def server_retrieve_files(f,p):
    
    files = glob.glob('server/*.enc')
    for file_name in files:
        file_read = open(file_name,"r")
        text = file_read.read()
        j = int(text[-NUMBER_OF_FILE_BITS:],2)
        M = text[-(2 ** d + NUMBER_OF_FILE_BITS): -NUMBER_OF_FILE_BITS]
        if int(M[p]) ^ pseudo_random_bit(f, j, t):
            file_write = open("user_mobile/{}".format(file_name[7:]),"w")
            file_write.write(text[:-(2 ** d + NUMBER_OF_FILE_BITS)])
            file_write.close()
            print("Retrieved file {}".format(format(file_name[7:])))
        file_read.close()

def retrieve_files(keyword):
    file_read = open("user_mobile/word_maxlength.txt","r")
    maxlen = int(file_read.read())
    word_max = lengthen_word(keyword,maxlen)
    bin_word = string_to_binary(word_max)
    phi = pseudo_random_permutation(tou,int(bin_word,2),len(bin_word))
    phi = number_to_binary(phi,len(bin_word))
    p = server_retrieve_phi(phi)
    if p is not None:
        binary_p = number_to_binary(p,maxlen)
    
        f = pseudo_random_function(r, int(binary_p + phi, 2), d + maxlen, t)
        server_retrieve_files(f,p)

if __name__ == "__main__":
    file_read = open("user_mobile/s.txt","r")
    s = file_read.read()
    file_read.close()
    file_read = open("user_mobile/r.txt","r")
    r = file_read.read()
    file_read.close()
    file_read = open("user_mobile/tou.txt","r")
    tou = file_read.read()
    file_read.close()
    
    print("Enter keyword: ",end="")
    keyword = input()
    retrieve_files(keyword)

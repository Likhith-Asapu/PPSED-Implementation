from imports_and_libraries import *

def server_retrieve_phi(phi):

    length = 2 ** d
    # read json file 
    f = open('server/file_indices.json')
    file_indices = json.load(f)
    
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
    
    length = 2 ** d
    # read json file 
    file_open = open('server/file_indices.json')
    file_indices = json.load(file_open)
    for file_name in file_indices["file_index"].keys():
        j = file_indices["file_index"][file_name]
        file_read = open("server/{}.enc".format(file_name[:-4]),"r")
        text = file_read.read()
        M = text[-2 ** d:]
        if int(M[p]) ^ pseudo_random_bit(f, j, t):
            file_write = open("user_mobile/{}.enc".format(file_name[:-4]),"w")
            file_write.write(text[:-2 ** d])
            file_write.close()
            print("Retrieved file {}.enc".format(file_name[:-4]))
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

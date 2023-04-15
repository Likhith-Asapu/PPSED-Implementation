from imports_and_libraries import *
from file_encryption import *

def generate_index_string(number_of_words,file_num,word_indices):
    I = [0 for i in range(number_of_words)]

    
    file = open("user/{}.txt".format(file_num),'r')
    text = file.read().lower()
    text_list = word_tokenize(text)
    for i in range(number_of_words):
        if word_indices['index_to_word'][i] in text_list:
            I[pseudo_random_permutation(s,i,d)] = 1
    file.close()
    
    R = []
    for i in range(2 ** d):
        R.append(pseudo_random_function(r,i,d,t))

    M = []
    for i in range(2 ** d):
        M.append(I[i] ^ pseudo_random_bit(R[i],file_num - 1))
    
    final_string = ""
    for i in range(len(M)):
        final_string += str(M[i])
    
    return final_string

def pass_to_server(number_of_files,word_indices):
    for i in range(number_of_files):
        file_name = '{}.txt'.format(i + 1)
        data = generate_index_string(NUMBER_OF_WORDS,i + 1,word_indices)
        encrypt_file(file_name)
        # print(data)
        file_write = open("server/"+file_name[:-4]+".enc","a")
        file_write.write(data)
        file_write.close()

if __name__ == "__main__":
    s = generate_pad(t)
    file_write = open("user/s.txt","w")
    file_write.write(s)
    file_write.close()
    r = generate_pad(t)
    file_write = open("user/r.txt","w")
    file_write.write(r)
    file_write.close()

    pass_to_server(NUMBER_OF_FILES ,word_indices)



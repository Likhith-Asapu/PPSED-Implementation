from imports_and_libraries import *
from file_encryption import *
from choose_r_value import *
f = open('user/word_indices.json')
word_indices = json.load(f)

def generate_index_string(file_name,number_of_words,file_num,word_indices,r,s):
    I = [0 for i in range(number_of_words)]
    
    file = open("user/{}.txt".format(file_name[:-4]),'r')
    text = file.read().lower()
    text_list = word_tokenize(text)
    for i in range(number_of_words):
        if word_indices['index_to_word'][i] in text_list:
            I[pseudo_random_permutation(s,i,d)] = 1
    file.close()
    
    r = choose_r(r,file_name,t)
    R = []
    for i in range(2 ** d):
        R.append(pseudo_random_function(r,i,d,t))

    M = []
    for i in range(2 ** d):
        M.append(I[i] ^ pseudo_random_bit(R[i],file_num - 1,t))
    
    final_string = ""
    for i in range(len(M)):
        final_string += str(M[i])
    
    return final_string

def pass_to_server(file_name,word_indices,r,s):
    
    if os.path.isfile('user/number_of_files.txt'):
        file_read = open('user/number_of_files.txt','r')
        index = int(file_read.read()) + 1
        file_read.close()
    else:
        index = 1
    
    data = generate_index_string(file_name,NUMBER_OF_WORDS,index,word_indices,r,s)
    encrypt_file(file_name)
    # print(data)

    binary_index = number_to_binary(index,NUMBER_OF_FILE_BITS)

    file_write = open("server/"+file_name[:-4]+".enc","a")
    file_write.write(data+binary_index)
    file_write.close()

    file_write = open('user/number_of_files.txt','w')
    file_write.write(str(index))

if __name__ == "__main__":
    if not os.path.isfile("user/s.txt"):
        s = generate_pad_random(t)
        file_write = open("user/s.txt","w")
        file_write.write(s)
        file_write.close()
    else:
        file_read = open("user/s.txt","r")
        s = file_read.read()
        file_read.close()
    
    if not os.path.isfile("user/r.txt"):
        r = generate_pad_random(t)
        file_write = open("user/r.txt","w")
        file_write.write(r)
        file_write.close()
    else:
        file_read = open("user/r.txt","r")
        r = file_read.read()
        file_read.close()

    print("Enter File Name for Encryption: ",end="")
    file_name = input()
    if os.path.isfile("user/{}".format(file_name)):
        pass_to_server(file_name ,word_indices,r,s)
    else:
        print("File Not Found")



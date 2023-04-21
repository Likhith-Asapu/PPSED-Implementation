from imports_and_libraries import *
import glob

def user_retrieve_files(keyword,s,r):
    file_open = open('user/word_indices.json')
    word_indices = json.load(file_open)
    try:
        index = word_indices['word_to_index'][keyword]
    except:
        print("Keyword not found in Dictionary")
        return None,None
    p = pseudo_random_permutation(s,index,d)

    file_read = open('user/r_key.json','r')
    r_key = json.load(file_read)

    file_read.close()
    R = []
    F = []
    for r_values in list(r_key["r_value_file"].values()):
        if r_values not in R:
            F.append(pseudo_random_function(r_values,p,d,t))
    return p,F

def server_retrieve_files(p,F):

    length = 2 ** d
    # read json file
    files = glob.glob('server/*.enc')
    f = open('server/r_key.json')
    data = json.load(f)
    f.close()

    for file_name in files:

        f = F[data["rvalues"][file_name[7:]] - 1]
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

def retrieve_files(keyword,s,r):
    p,F = user_retrieve_files(keyword,s,r)
    if p != None and F != None:
        server_retrieve_files(p,F)
        if os.path.isfile('user/r_key.json'):
            file_read = open('user/r_key.json','r+')
            r_key = json.load(file_read)
            r_key["current_seed"] += 1
            with open('user/r_key.json','w') as f:
                json.dump(r_key,f)
            file_read.close()

if __name__ == "__main__":
    file_read = open("user/s.txt","r")
    s = file_read.read()
    file_read.close()
    file_read = open("user/r.txt","r")
    r = file_read.read()
    file_read.close()
    
    print("Enter keyword: ",end="")
    keyword = input()
    retrieve_files(keyword,s,r)

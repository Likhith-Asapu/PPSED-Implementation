class PRG:
    def __init__(self, security_parameter: int, generator: int,
                 prime_field: int, expansion_factor: int):

        self.n = security_parameter
        self.g = generator
        self.p = prime_field
        self.ln = expansion_factor

    def generate(self, seed: int) -> str:
        out = ""

        for i in range(0, self.ln):
            dlp = pow(self.g, seed, self.p)
            if seed < (self.p - 1) / 2:
                out += "0"
            else:
                out += "1"

            seed = dlp

        return out
    
class PRF:
    def __init__(self, security_parameter: int, generator: int,
                 prime_field: int, key: int, expansion_factor:int):

        self.n = security_parameter
        self.g = generator
        self.p = prime_field
        self.k = key
        self.ln = expansion_factor

    def evaluate(self, x: int) -> int:
        k = self.k

        if len(bin(x)) > 2 + self.n:
            x_bin = bin(x)[-self.n:]
        else:
            x_bin = f'{x:0{self.n}b}'

        for i in range(0, len(x_bin)):
            prg_prf = PRG(self.n, self.g, self.p, 2 * self.ln)
            out_str = prg_prf.generate(k)

            if x_bin[i] == "0":
                k = int(out_str[:int(self.ln)], 2)
            else:
                k = int(out_str[-int(self.ln):], 2)

        out = k
        return out
    

class PRP:
    def __init__(self, security_parameter: int, generator: int,
                 prime_field: int, key: list[int]):

        self.n = int(security_parameter/2)
        self.g = generator
        self.p = prime_field
        self.k = key

    def evaluate(self, x: int) -> int:
        if len(bin(x)) > 2 + (2 * self.n):
            x_bin = bin(x)[-(2 * self.n):]
        else:
            x_bin = f'{x:0{(2 * self.n)}b}'

        x_bin_l = x_bin[0:self.n]
        x_bin_r = x_bin[self.n:]

        for i in range(0, 4):
            prf_prp = PRF(self.n, self.g, self.p, self.k[i], self.n)
            y_bin_l = x_bin_r
            y_bin_r = f'{(prf_prp.evaluate(int(x_bin_r, 2)) ^ int(x_bin_l, 2)):0{self.n}b}'
            x_bin_l = y_bin_l
            x_bin_r = y_bin_r

        y = int(x_bin_r + x_bin_l, 2)

        return y

def pseudo_random_permutation(seed,number,length):
    n = len(seed)
    binary_keys = [seed[:int(n/4)], seed[int(n/4):int(2*n/4)], seed[int(2*n/4):int(3*n/4)], seed[int(3*n/4):],]
    keys = [int(key,2) for key in binary_keys]
    prp = PRP(length, 44, 107, keys)
    return prp.evaluate(number)

def pseudo_random_function(seed,number,input_length,output_length):
    prf = PRF(input_length, 44, 107, int(seed,2), output_length)
    return prf.evaluate(number)
    

def pseudo_random_bit(seed,number,input_length):
    prf = PRF(input_length, 44, 107, seed, 1)
    return prf.evaluate(number)

def lengthen_word(word,maxlen):
    while len(word) < maxlen:
        word += '\0'

    return word
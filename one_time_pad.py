import secrets
class PRG:
    def __init__(self, security_parameter: int, generator: int,
                 prime_field: int, expansion_factor: int):
       
       
        self.security_parameter = security_parameter
        self.generator = generator
        self.prime_field = prime_field
        self.expansion_factor = expansion_factor
        
       

    def generate(self, seed: int) -> str:

        ans=""

        for i in range(0, self.expansion_factor):
            if(seed<(self.prime_field-1)/2):
                ans+='0'
            else:
                ans+='1'
            new_seed = pow(self.generator, seed, self.prime_field)
            seed=new_seed

        return ans

# A function to convert a string to binary
def string_to_binary(string):
  binary = ""
  for char in string:
    binary += format(ord(char), "08b") # Convert each character to 8-bit binary
  return binary

def binary_to_string(string):
  text = ""
  for i in range(0, len(string), 8):
    text += chr(int(string[i:i+8], 2)) # Convert each 8-bit binary to a character
  return text

def number_to_binary(number,length):
  binary = format(number, "0128b")
  return binary[-length:]

def generate_pad_random(length):
  pad = ""
  for i in range(length):
    pad += str(secrets.randbits(1))

  return pad

# A function to generate a one time pad of a given length
def generate_pad(length):

  # creating seed of length 16
  pad_seed = ""
  for i in range(16):
    pad_seed += str(secrets.randbits(1)) # Generate a random bit
    
  # converting binary seed to decimal
  decimal_pad_seed = int(pad_seed, 2)
    
  # feeding to PRG with security parameter and a large prime field to get a binary string of the desired length
  prg=PRG(7,13,999999937,length)
  pad=prg.generate(decimal_pad_seed)
    
  return pad,pad_seed

def generate_pad_seed_given(pad_seed,length):
  decimal_pad_seed = int(pad_seed, 2)  
  prg=PRG(7,13,999999937,length)
  pad=prg.generate(decimal_pad_seed)
  return pad

# A function to xor two binary strings of equal length
def xor_binary(binary1, binary2):
  xor = ""
  for i in range(len(binary1)):
    xor += str(int(binary1[i]) ^ int(binary2[i])) # Perform bitwise xor
  return xor

# A function to perform the whole task
def encrypt_string(string):
  
  binary = string_to_binary(string) # Convert the string to binary
  pad,seed = generate_pad(len(binary)) # Generate a one time pad of the same length
  encrypted = xor_binary(binary, pad) # Xor the binary and the pad
  return encrypted, seed

def decrypt_string(string, seed):    
    pad = generate_pad_seed_given(seed,len(string))
    decrypted = xor_binary(string, pad) # Xor the binary and the pad
    decrypted = binary_to_string(decrypted) # Convert the binary to string
    return decrypted
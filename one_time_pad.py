
# A function to convert a string to binary
def string_to_binary(string):
  binary = ""
  for char in string:
    binary += format(ord(char), "08b") # Convert each character to 8-bit binary
  return binary

def binary_to_string(binary):
  string = ""
  for i in range(0, len(binary), 8):
    string += chr(int(binary[i:i+8], 2)) # Convert each 8-bit binary to a character
  return string

# A function to generate a one time pad of a given length
def generate_pad(length):
  import secrets

  pad = ""
  for i in range(length):
    pad += str(secrets.randbits(1)) # Generate a random bit
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
  # print("Binary of the input string: "+binary)
  pad = generate_pad(len(binary)) # Generate a one time pad of the same length
  # print("One time pad: "+pad)
  encrypted = xor_binary(binary, pad) # Xor the binary and the pad
  return encrypted,pad

def decrypt_string(string,key):
  decrypted = xor_binary(string,key)
  return binary_to_string(decrypted)

# Example usage
# string = "Hello world"
# encrypted,key = encrypt_string(string)
# print("Output: "+encrypted)
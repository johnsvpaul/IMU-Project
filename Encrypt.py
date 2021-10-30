import hashlib
from Crypto import Random
from Crypto.Cipher import AES
from base64 import b64encode, b64decode
import zipfile


#def __init__(key):
code = "1234567891234567"
block_size = AES.block_size
key = hashlib.sha256(code.encode()).digest()

def encrypt(plain_text):
        plain_text = __pad(plain_text)
        iv = Random.new().read(block_size)
        cipher = AES.new(key, AES.MODE_CBC, iv)
        encrypted_text = cipher.encrypt(plain_text.encode())
        return b64encode(iv + encrypted_text).decode("utf-8")

def decrypt(encrypted_text):
        encrypted_text = b64decode(encrypted_text)
        iv = encrypted_text[:block_size]
        cipher = AES.new(key, AES.MODE_CBC, iv)
        plain_text = cipher.decrypt(encrypted_text[block_size:]).decode("utf-8")
        return __unpad(plain_text)

def __pad(plain_text):
        number_of_bytes_to_pad = block_size - len(plain_text) % block_size
        ascii_string = chr(number_of_bytes_to_pad)
        padding_str = number_of_bytes_to_pad * ascii_string
        padded_plain_text = plain_text + padding_str
        return padded_plain_text

#@staticmethod
def __unpad(plain_text):
        last_character = plain_text[len(plain_text) - 1:]
        bytes_to_remove = ord(last_character)
        return plain_text[:-bytes_to_remove]




# Using readlines()
file1 = open('output1.csv.bz2', 'r+b')
Lines = file1.readlines()

# writing to file
file2 = open('Zippedfile1.txt', 'w')
 
count = 0
# Strips the newline character
for line in Lines:
        count += 1
        S = "{}".format(line.strip())
        S1 = str(encrypt(S)) + "\n"
        file2.writelines(S1)
        
       
        
file1.close()
file2.close()


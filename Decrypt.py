import hashlib
from Crypto import Random
from Crypto.Cipher import AES
from base64 import b64encode, b64decode
import zipfile
import sys


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


parameter = sys.argv[1]



# Using readlines()
file3 = open(parameter, 'r+b')
Lines2 = file3.readlines()
# Append to file
file4 = open('Decryptedfile3.csv', 'a')

c = 0
# Strips the newline character
for line1 in Lines2:
        c += 1
        Str = "{}".format(line1.strip())
        #print(c)
        file4.writelines(decrypt(Str)+"\n")
        
        
file3.close()
file4.close()
print("Decryption complete")




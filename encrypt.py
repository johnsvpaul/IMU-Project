
import cryptography
#class Encryption():
from cryptography.fernet import Fernet

#    def key_create:
e_key = Fernet.generate_key()
#        return e_key

#    def key_write(key, key_name):
with open('mykey.e_key','wb') as mykey:
    mykey.write(e_key)

f = Fernet(e_key)

with open('test.csv.bz2','rb') as zipped_file:
    zipped = zipped_file.read()

encrypted_file = f.encrypt(zipped)

with open('finalEncrypt.csv.tar.gz','wb') as finalEncrypt:
    finalEncrypt.write(encrypted_file)

#with open('finalEncrypt.csv.tar.gz','rb') as e:  
    #encrypted = e.read()

#decrypted_file = f.decrypt(encrypted)

#with open('finalDecrypt.csv.tar.gz','wb') as finalDecrypt:
    #finalDecrypt.write(decrypted_file)
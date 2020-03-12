import Crypto
from Crypto.PublicKey import RSA
from Crypto import Random
import ast
import sys
import time
 
inputfiledir = sys.argv[1]
timefiledir = sys.argv[2]
 
random_generator = Random.new().read
key = RSA.generate(2048, random_generator)
 
publickey = key.publickey()
 
print('='*100)
 
input = open(inputfiledir,"r")
plain_text = input.read()
 
encrypt_start = time.time()
cipher_text = publickey.encrypt(plain_text, 32)
encrypt_end = time.time()
 
print ('Plaintext encrypted using Public Key is:', cipher_text)
print
#decrypted code below
decrypt_start = time.time()
decrypted = key.decrypt(ast.literal_eval(str(cipher_text)))
decrypt_end = time.time()
print ('Ciphertext decrypted with Private key is', decrypted)
print ('='*100)
 
with open(timefiledir, 'a') as timefile:
    timefile.write("encrypt time = ")
    timefile.write(str((encrypt_end - encrypt_start)*1000000))
    timefile.write("\n")
    timefile.write("decrypt time = ")
    timefile.write(str((decrypt_end - decrypt_start)*1000000))
    timefile.write("\n")

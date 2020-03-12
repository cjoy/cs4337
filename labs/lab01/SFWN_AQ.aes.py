from Crypto.Cipher import AES
import sys
import time

iv = bytes.fromhex(sys.argv[1])
key = bytes.fromhex(sys.argv[2])
inputfiledir = sys.argv[3]
outputfiledir = sys.argv[4]

print('='*100)
print('Key used: ', [x for x in key])
print("IV used: ",[x for x in iv])
print('='*100)

aes1 = AES.new(key, AES.MODE_CBC, iv)
aes2 = AES.new(key, AES.MODE_CBC, iv)

with open(inputfiledir, 'rb') as infile:
    plain_text = infile.read()
    # pad to make last block length a multiple of 16
    padded_text = plain_text
    remainder = len(plain_text) % 16
    if remainder > 0:
        length = 16 - remainder
        padded_text += b'\x00'*length
    # encrypt padded text
    start_time = time.time()
    cipher_text = aes1.encrypt(padded_text)
    encryption_time = time.time() - start_time

with open(outputfiledir, 'wb') as outfile:
    outfile.write(cipher_text)
    outfile.close()

print('Plaintext is:', plain_text)
print('Ciphertext is:', cipher_text)
start_time = time.time()
original_msg = aes2.decrypt(cipher_text)
decryption_time = time.time() - start_time
print('Original Message:', original_msg.decode('utf-8'))
print('='*100)
print('Encryption time:', encryption_time * 1000000)
print('Decryption time:', decryption_time * 1000000)

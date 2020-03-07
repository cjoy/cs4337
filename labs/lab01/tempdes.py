from Crypto.Cipher import DES
import sys

iv = bytes.fromhex(sys.argv[1])
key = bytes.fromhex(sys.argv[2])
inputfiledir = sys.argv[3]
outputfiledir = sys.argv[4]

print(iv, type(iv), len(iv))
print(key, type(key), len(key))

print('='*100)
print('Key used: ', [x for x in key])
print("IV used: ",[x for x in iv])
print('='*100)

des1 = DES.new(key, DES.MODE_CBC, iv)
des2 = DES.new(key, DES.MODE_CBC, iv)

with open(inputfiledir, 'rb') as infile:
    plain_text = infile.read()
    # pad to make last block length a multiple of 8
    padded_text = plain_text
    remainder = len(plain_text) % 8
    if remainder > 0:
        length = 8 - remainder
        padded_text += b'\x00'*length
    # encypt padded text
    cipher_text = des1.encrypt(padded_text)


with open(outputfiledir, 'wb') as outfile:
    outfile.write(cipher_text)
    outfile.close()

print('Plaintext is:', plain_text)
print('Ciphertext is:', cipher_text)
original_msg = des2.decrypt(cipher_text)
print('Original Message:', original_msg.decode('utf-8'))
print('='*100)
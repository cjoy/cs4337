from Crypto.Cipher import DES
from Crypto import Random
from Crypto.Util.Padding import pad, unpad
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
    cipher_text = des1.encrypt(pad(plain_text, DES.block_size))

with open(outputfiledir, 'wb') as outfile:
    outfile.write(cipher_text)
    outfile.close()

with open('test3.des', 'rb') as infile:
    cipher_text_file = infile.read()
print(bytearray(des2.decrypt(cipher_text_file)))

print('Plaintext is:', plain_text)
print('Ciphertext is:', cipher_text)
msg = unpad(des2.decrypt(cipher_text_file), DES.block_size)
print('Original Message:', msg.decode('utf-8'))
print('='*100)


# print '='*100                    
# print 'Key used: ', [x for x in key]

# print "IV used: ",[x for x in iv]
# print '='*100

# des1 = DES.new(key, DES.MODE_CBC, bytes(iv, 'utf-8'))
# des2 = DES.new(key, DES.MODE_CBC, bytes(iv, 'utf-8'))

# plain_text = "abcdefgh"
# print "Plaintext is: ", plain_text

# cipher_text = des1.encrypt(plain_text)
# print "Ciphertext is: ",cipher_text
# msg=des2.decrypt(cipher_text)
# print "Original Message", msg
# print '='*100















# cbc_key = "\x40\xfe\xdf\x38\x6d\xa1\x3d\x57"
# print '='*100                    
# print 'Key used: ', [x for x in cbc_key]

# iv = Random.get_random_bytes(8)
# print "IV used: ",[x for x in iv]
# print '='*100

# des1 = DES.new(cbc_key, DES.MODE_CBC, iv)
# des2 = DES.new(cbc_key, DES.MODE_CBC, iv)

# plain_text = "abcdefgh"
# print "Plaintext is: ", plain_text

# cipher_text = des1.encrypt(plain_text)
# print "Ciphertext is: ",cipher_text
# msg=des2.decrypt(cipher_text)
# print "Original Message", msg
# print '='*100


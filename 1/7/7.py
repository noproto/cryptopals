import base64
from Crypto.Cipher import AES

encrypted_file_bytes = base64.b64decode(open("7.txt").read().replace("\n",""))

key = b"YELLOW SUBMARINE"
# Create an AES ECB cipher object
cipher = AES.new(key, AES.MODE_ECB)
# Decrypt the ciphertext
plaintext = cipher.decrypt(encrypted_file_bytes)

print(plaintext)

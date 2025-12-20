import base64
from Crypto.Cipher import AES

def xor_two_equal_len_byte_arrays(first, second):
    return bytes([first[i] ^ second[i] for i in range(0, len(first))])

encrypted_file_bytes = base64.b64decode(open("10.txt").read().replace("\n",""))
block_size = 16

key = b"YELLOW SUBMARINE"
iv = bytes(block_size) # Initializes to 0
# Create an AES ECB cipher object
cipher = AES.new(key, AES.MODE_ECB)

# Decrypt the ciphertext, block by block, by xoring in the previous block
previous_ciphertext_block = iv
idx = 0
plaintext = b""
while True:
    if len(encrypted_file_bytes[idx:(idx+block_size)]) == 0:
        break
    plaintext += xor_two_equal_len_byte_arrays(cipher.decrypt(encrypted_file_bytes[idx:(idx+block_size)]), previous_ciphertext_block)
    previous_ciphertext_block = encrypted_file_bytes[idx:(idx+block_size)]
    idx += block_size

print(plaintext)

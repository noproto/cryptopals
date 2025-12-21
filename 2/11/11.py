import random
import sys
from Crypto.Cipher import AES

def generate_random_16_bytes():
    return bytes([random.randint(0,255) for x in range(0,16)])

def encryption_oracle(inputdata):
    block_size = 16
    random_aes_key = generate_random_16_bytes()
    # Doesn't specify whether these should be random, maybe zero is fine?
    random_pre_pad = bytes(random.randint(5,10))
    random_post_pad = bytes(random.randint(5,10))
    concatenated_input = random_pre_pad + inputdata + random_post_pad
    # Use PKCS#7 padding
    # Ternary expression to calculate padding length
    padding_len = (block_size - (len(concatenated_input) % block_size)) if ((len(concatenated_input) % block_size) != 0) else 0
    # Pad with a byte value that is equal to the padding length, repeated padding_len times
    padding_bytes = bytes([padding_len]) * padding_len
    is_cbc_mode = (random.randint(0,1) == 1)
    if is_cbc_mode:
        iv = generate_random_16_bytes()
        cipher = AES.new(generate_random_16_bytes(), AES.MODE_CBC, iv)
    else:
        cipher = AES.new(generate_random_16_bytes(), AES.MODE_ECB)
    return cipher.encrypt(concatenated_input+padding_bytes)


print(encryption_oracle(bytes(sys.argv[1],"ascii")).hex())

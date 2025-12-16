import string

def xor_two_equal_len_byte_arrays(first, second):
    return bytes([first[i] ^ second[i] for i in range(0, len(first))])

def score_printable(attempt):
    return sum([1 for x in attempt if x in bytes(string.ascii_letters, "ascii")])

ciphertext=bytes.fromhex("1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736")
high_score = 0
solution = None
for i in range(0,255):
    xor_key = bytes([i]*len(ciphertext))
    attempt = xor_two_equal_len_byte_arrays(ciphertext, xor_key)
    score = score_printable(attempt)
    if score > high_score:
        high_score = score
        solution = attempt

print(solution.decode("ascii"))

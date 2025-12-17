import base64
import string

encrypted_file_bytes = base64.b64decode(open("6.txt").read().replace("\n",""))

def to_bits(byte_string):
    return "".join([bin(b)[2:].zfill(8) for b in byte_string])

def hamming_distance(str_one, str_two):
    str_one_bits = list(to_bits(str_one))
    str_two_bits = list(to_bits(str_two))
    different_bits = sum([1 for x in zip(str_one_bits, str_two_bits) if x[0] != x[1]])
    return different_bits

def xor_two_equal_len_byte_arrays(first, second):
    return bytes([first[i] ^ second[i] for i in range(0, len(first))])

def score_printable(attempt):
    return sum([1 for x in attempt if x in bytes(string.ascii_letters, "ascii")])

def repeating_key_xor(plaintext, xor_key):
    ciphertext = b""
    idx = 0
    for i in plaintext:
        ciphertext += bytes([i ^ xor_key[idx % len(xor_key)]])
        idx += 1
    return ciphertext

assert hamming_distance(b"this is a test", b"wokka wokka!!!") == 37

min_keysize = 2
max_keysize = 40
ks_edit_distance = []
for ks in range(min_keysize, max_keysize + 1):
    edit_distance = hamming_distance(encrypted_file_bytes[0:ks], encrypted_file_bytes[ks:ks*2])
    normal_edit_distance = float(edit_distance) / float(ks) # hopefully we don't get burned here by floating point math
    ks_edit_distance.append((normal_edit_distance, ks)) # first element of the tuple is the edit distance so we can just run sorted() on it
sorted_ks_edit_distance = sorted(ks_edit_distance)
sorted_ks_edit_distances = [d[1] for d in sorted_ks_edit_distance[0:3]] # "You could proceed perhaps with the smallest 2-3 KEYSIZE values"
print("Most likely key sizes:", (", ".join([str(s) for s in sorted_ks_edit_distances])))
# Result: Most likely key sizes: 5, 3, 2

"""
for ks in sorted_ks_edit_distances:
    blocks = [b"" for blk in range(0, ks)]
    idx = 0
    for c in encrypted_file_bytes:
        blocks[idx % ks] += bytes(c)
        idx += 1
    final_key = []
    for blk in blocks:
        high_score = 0
        solution = None
        solution_key = None
        for i in range(0,255):
            xor_key = bytes([i]*len(blk))
            attempt = xor_two_equal_len_byte_arrays(blk, xor_key)
            score = score_printable(attempt)
            if score > high_score:
                high_score = score
                solution = attempt
                solution_key = i
        final_key.append(solution_key)
    print(f"Key at key size {ks}:", "".join([chr(c) for c in final_key]))
"""
# Result:
# Most likely key sizes: 5, 3, 2
# Key at key size 5: AAAAA
# Key at key size 3: AAA
# Key at key size 2: AA

# Use the identified key to decrypt encrypted_file_bytes
plaintext = repeating_key_xor(encrypted_file_bytes, b"AAAAA")
print(plaintext)

# Remaining steps (probably doing this wrong):
# For each block, the single-byte XOR key that produces the best looking histogram is the repeating-key XOR key byte for that block. Put them together and you have the key.

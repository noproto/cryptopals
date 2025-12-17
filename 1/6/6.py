import base64

encrypted_file_bytes = base64.b64decode(open("6.txt").read().replace("\n",""))

def to_bits(byte_string):
    return "".join([bin(b)[2:].zfill(8) for b in byte_string])

def hamming_distance(str_one, str_two):
    str_one_bits = list(to_bits(str_one))
    str_two_bits = list(to_bits(str_two))
    different_bits = sum([1 for x in zip(str_one_bits, str_two_bits) if x[0] != x[1]])
    return different_bits

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

# Remaining steps:
# Now that you probably know the KEYSIZE: break the ciphertext into blocks of KEYSIZE length.
# Now transpose the blocks: make a block that is the first byte of every block, and a block that is the second byte of every block, and so on.
# Solve each block as if it was single-character XOR. You already have code to do this.
# For each block, the single-byte XOR key that produces the best looking histogram is the repeating-key XOR key byte for that block. Put them together and you have the key.

import string

def xor_single_byte_against_byte_arrays(xor_key, second):
    return bytes([xor_key ^ second[i] for i in range(0, len(second))])

def score_printable(attempt):
    return sum([1 for x in attempt if x in bytes(string.ascii_letters, "ascii")]) + sum([2 for x in attempt if x in b" "])

challenge_file = open("4.txt").read().splitlines()
high_score = 0
solution = None
for line in challenge_file:
    ciphertext=bytes.fromhex(line)
    for i in range(0,255):
        attempt = xor_single_byte_against_byte_arrays(i, ciphertext)
        score = score_printable(attempt)
        if score > high_score:
            high_score = score
            solution = attempt

print(solution.decode("ascii"))

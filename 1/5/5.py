def repeating_key_xor(plaintext, xor_key):
    ciphertext = b""
    idx = 0
    for i in plaintext:
        ciphertext += bytes([i ^ xor_key[idx % len(xor_key)]])
        idx += 1
    return ciphertext

stanza = b"Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"
ciphertext = repeating_key_xor(stanza, b"ICE")
solution = bytes.fromhex("0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f")
assert ciphertext == solution
print("Solved")

def xor_two_equal_len_byte_arrays(first, second):
    return bytes([first[i] ^ second[i] for i in range(0, len(first))])

in_bytes = bytes.fromhex("1c0111001f010100061a024b53535009181c")
xor_bytes = bytes.fromhex("686974207468652062756c6c277320657965")

print(xor_two_equal_len_byte_arrays(in_bytes, xor_bytes).hex())

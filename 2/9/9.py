import argparse

parser = argparse.ArgumentParser("chal9")
parser.add_argument("blocksize", help="The size of the block to pad to", type=int)
parser.add_argument("inputdata", help="The unpadded input data", type=str)
args = parser.parse_args()
blocksize = args.blocksize
unpadded = bytes(args.inputdata, "ascii")
assert 0 < blocksize <= 127

# Ternary expression to calculate padding length
padding_len = (blocksize - (len(unpadded) % blocksize)) if ((len(unpadded) % blocksize) != 0) else 0
# Pad with a byte value that is equal to the padding length, repeated padding_len times
padding_bytes = bytes([padding_len]) * padding_len
# Print padded output
print((unpadded+padding_bytes).decode("ascii"), end="")

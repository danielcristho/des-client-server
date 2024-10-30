key = "1110"

s0 = [[1, 0, 3, 2],
      [3, 2, 1, 0],
      [0, 2, 1, 3],
      [3, 1, 3, 2]]

def getSboxEntry(binary, sbox):
    # Determine row and column for S-box lookup
    row = int(binary[0] + binary[3], 2)
    col = int(binary[1] + binary[2], 2)
    binary = bin(s0[row][col])[2:]
    return "0" + binary if len(binary) == 1 else binary

def fFunction(key, k):
    XOR = padding(bin(int(key, 2) ^ int(k, 2))[2:], 4)
    return getSboxEntry(XOR, s0)

def padding(string, length):
    # Ensures binary strings are padded to required length
    return string.zfill(length)

# Step 1-2: Generate plaintext pairs for XOR result 7 and compute S-box outputs
values = [(i, i ^ 7) for i in range(16)]
print(values)

# Step 3: Create distribution table by XORing S-box outputs of pairs
results = []
for (a, b) in values:
    output1 = int(getSboxEntry(padding(bin(a)[2:], 4), s0), 2)
    output2 = int(getSboxEntry(padding(bin(b)[2:], 4), s0), 2)
    results.append(output1 ^ output2)
print(results)

# Step 4: Use S-box outputs to narrow down key possibilities
output1 = fFunction(key, padding(bin(8)[2:], 4))
output2 = fFunction(key, padding(bin(15)[2:], 4))
int1 = int(output1, 2)
int2 = int(output2, 2)
XOR = int1 ^ int2

# Finding potential keys based on observed XOR values
keys = set(val ^ 8 for val in [0, 1, 2, 3, 4, 5, 6, 7, 10, 13])
print(keys)

# Use a second pair to further reduce possible keys
output1 = fFunction(key, padding(bin(6)[2:], 4))
output2 = fFunction(key, padding(bin(1)[2:], 4))
int1 = int(output1, 2)
int2 = int(output2, 2)
XOR = int1 ^ int2

# Narrow down key possibilities with intersection
keys2 = set(val ^ 6 for val in [0, 1, 2, 3, 4, 5, 6, 7, 10, 13])
intersection = keys.intersection(keys2)
print(intersection)  # Final narrowed set of possible keys

# Result analysis
# Key is determined based on known relationships in S-box patterns
# Final possible key is likely either 6 ^ 8 or 6 ^ 15
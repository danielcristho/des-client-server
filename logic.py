key = "1110"

s0 = [[1, 0, 3, 2],
	[3, 2, 1, 0],
	[0, 2, 1, 3],
	[3, 1, 3, 2]]

def getSboxEntry(binary,sbox):
		row = binary[0] + binary[3]
		col = binary[1] + binary[2]
		row = int(row,2)
		col = int(col,2)
		binary = bin(s0[row][col])[2:]
		if len(binary) == 1:
			binary = "0" + binary
		return binary

def fFunction(key, k):
		XOR = bin((int(key,2)^int(k,2)))[2:]
		XOR = padding(XOR,4)
		S0 = getSboxEntry(XOR, s0)
		return S0

def padding(string,length):
	if len(string) == length:
		return string
	while(len(string) < length):
		string = "0" + string
	return string

#Step 1: Pick a random number between 0 and 15 (we have 4 bit numbers) (preferably not 0). Let's use 7 for our example.
#Step 2: Find plaintext pairs that when XORd together yield 7
#a ^ b = 7 -> a ^ 7 = b
values = []
for i in range(0,16):
	temp = i ^ 7
	values.append((i,temp))
print(values)

#Step 3: create distribution table
results = []
for (a,b) in values:
	binary = padding(bin(a)[2:],4)
	binary2 = padding(bin(b)[2:],4)
	output1 = int(getSboxEntry(binary, s0),2)
	output2 = int(getSboxEntry(binary2, s0),2)
	result = output1 ^ output2
	results.append(result)
print(results) #THESE SHOULD NO LONGER BE RANDOM. PEEP THE PATTERN
#[1, 1, 1, 1, 1, 1, 1, 1, 2, 0, 1, 0, 0, 1, 0, 2]

#Distrubution table
# 0 -> 9,11,12,14
# 1 -> 0,1,2,3,4,5,6,7,10,13
# 2 -> 8,15

#Step 4: pick a random pair (I picked (8,15))
#Now we are gonna use the fbox and known cipher text to guess the key

output1 = fFunction(key, padding(bin(8)[2:],4))
output2 = fFunction(key, padding(bin(15)[2:],4))
int1 = int(output1,2)
int2 = int(output2,2)
XOR = int1^int2
# 8 ^ key, 15 ^ key
# (8 ^ key) ^ (15 ^ key) = 8 ^ key ^ key ^ 15 = 8 ^ 15 = 7
# a ^ b = 7
# (a,b) is one of the pairs we've already generated
# s_box(a) ^ s_box(b) = 1
# (a,b) = 0,1,2,3,4,5,6,7,10,13

# now we know that a ^ 8 = key
keys =set()
As =  [0,1,2,3,4,5,6,7,10,13]
for val in As:
	XOR = val ^ 8
	keys.add(XOR)
print(keys)
#possible keys = [8, 9, 10, 11, 12, 13, 14, 15, 2, 5]

# now we try it again with a second pair so we can "intersection" the sets and reduce the # of possible keys
#let's use (11,12)
output1 = fFunction(key, padding(bin(6)[2:],4))
output2 = fFunction(key, padding(bin(1)[2:],4))
print(output1)
print(output2)
int1 = int(output1,2)
int2 = int(output2,2)
XOR = int1^int2
print(XOR)
# 11 ^ key, 12 ^ key
# (12 ^ key) ^ (12 ^ key) = 11^ key ^ key ^ 12 =11 ^ 12 = 7
# a, b
# 11 ^ 12 = 7
# (a,b) is one of the pairs we've already generated
# s_box(11) ^ s_box(12) = 1
# (a,b) =
keys2 = set()
Bs =  [0,1,2,3,4,5,6,7,10,13]
for val in Bs:
	XOR = val ^ 6
	keys2.add(XOR)
print(keys2)

intersection = keys.intersection(keys2)
print(intersection)
#{2, 11, 12, 5}

#(a,b) is one of the pairs that we'ce already generated
# a ^ 6 = key
# b ^ 1 = key
#BUT
#sbox(a) ^ sbox(b)  = 2
# THEREFORE key is either 6 ^ 8 or 6 ^ 15
# 6 ^ 8 =  14 (THIS WAS THE KEY WHOA)
# 6 ^ 15 = 9
#however if you didn't know this to be true ahead of time, you would just run this last round twice and narrow it down
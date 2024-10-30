class DES:
    def __init__(self):
        self.key = "1001100111"  # 10-bit key used for encryption/decryption
        # Provided S-Boxes for the DES algorithm
        self.s0 = [[1, 0, 3, 2],
                    [3, 2, 1, 0],
                    [0, 2, 1, 3],
                    [3, 1, 3, 2]]
        self.s1 = [[0, 1, 2, 3],
                    [2, 0, 1, 3],
                    [3, 0, 1, 0],
                    [2, 1, 0, 3]]

    """
    Get S-Box entry based on a 4-bit binary input and the specified S-Box.
    The first and last bits determine the row, while the middle bits determine the column.
    """
    def getSboxEntry(self, binary, sbox):
        row = binary[0] + binary[3]  # Calculate row index
        col = binary[1] + binary[2]  # Calculate column index
        row = int(row, 2)  # Convert binary to integer for row
        col = int(col, 2)  # Convert binary to integer for column
        # Select the appropriate S-Box and retrieve the value
        if sbox == 0:
            binary = bin(self.s0[row][col])[2:]
        else:
            binary = bin(self.s1[row][col])[2:]
        # Ensure the binary output is 2 bits long
        return binary.zfill(2)

    # Expands a 4-bit key to 8 bits for further processing
    def fFunction(self, key, k):
        expansion = key[3] + key[0] + key[1] + key[2] + key[1] + key[2] + key[3] + key[0]  # Expansion step
        XOR = bin((int(expansion, 2) ^ int(k, 2)))[2:]  # XOR with the generated key
        XOR = self.padding(XOR, 8)  # Ensure the result is 8 bits long

        left = XOR[:4]  # Split into left and right halves
        right = XOR[4:]

        # Retrieve entries from the S-Boxes
        S0 = self.getSboxEntry(left, 0)
        S1 = self.getSboxEntry(right, 1)

        p4 = S0 + S1  # Concatenate results from S-Boxes
        p4 = p4[1] + p4[3] + p4[2] + p4[0]  # Permute the result

        return p4

    """
    Generates two subkeys (k1, k2) from the initial 10-bit key.
    This involves permutations, left shifts, and further permutations.
    """
    def kValueGenerator(self, key):
        newKey = key[2] + key[4] + key[1] + key[6] + key[3] + key[9] + key[0] + key[8] + key[7] + key[5]  # Initial permutation
        left = newKey[0:5]  # Split the key
        right = newKey[5:]

        # Perform left shifts for k1
        leftShift = left[1:] + left[0]
        rightShift = right[1:] + right[0]
        k1 = leftShift + rightShift  # Combine and permute to create k1
        k1Permuted = k1[5] + k1[2] + k1[6] + k1[3] + k1[7] + k1[4] + k1[9] + k1[8]

        # Perform second left shifts for k2
        leftShiftTwice = leftShift[1:] + leftShift[0]
        rightShiftTwice = rightShift[1:] + rightShift[0]
        k2 = leftShiftTwice + rightShiftTwice  # Combine to create k2
        k2Permuted = k2[5] + k2[2] + k2[6] + k2[3] + k2[7] + k2[4] + k2[9] + k2[8]

        return (k1Permuted, k2Permuted)

    # Performs the initial permutation on the input key
    def initialPermutation(self, key):
        return key[1] + key[5] + key[2] + key[0] + key[3] + key[7] + key[4] + key[6]

    # Reverses the initial permutation
    def reversePermutation(self, key):
        return key[3] + key[0] + key[2] + key[4] + key[6] + key[1] + key[7] + key[5]

    """
    Adds padding to ensure the binary string is of the specified length.
    For example, it pads '101' to '0101' if 4 bits are required.
    """
    def padding(self, string, length):
        return string.zfill(length)  # Pad with zeros to the left

    """
    Encrypts an 8-bit string using the DES algorithm.
    Involves initial permutation, rounds of transformation, and final permutation.
    """
    def Encryption(self, string):
        permString = self.initialPermutation(string)  # Initial permutation
        left = permString[0:4]  # Split into two halves
        right = permString[4:]
        k1, k2 = self.kValueGenerator(self.key)  # Generate subkeys

        firstFOutput = self.fFunction(right, k1)  # Apply F function
        firstXOR = bin((int(left, 2) ^ int(firstFOutput, 2)))[2:]  # XOR with left half
        firstXOR = self.padding(firstXOR, 4)
        secondFOutput = self.fFunction(firstXOR, k2)  # Apply F function with k2

        secondXOR = bin((int(right, 2) ^ int(secondFOutput, 2)))[2:]  # XOR with right half
        secondXOR = self.padding(secondXOR, 4)
        output = secondXOR + firstXOR  # Concatenate results

        return self.reversePermutation(output)  # Final permutation

    """
    Decrypts an 8-bit string using the DES algorithm.
    The process is similar to encryption but uses the subkeys in reverse order.
    """
    def Decryption(self, string):
        permString = self.initialPermutation(string)  # Initial permutation
        left = permString[0:4]  # Split into two halves
        right = permString[4:]
        k1, k2 = self.kValueGenerator(self.key)  # Generate subkeys

        firstFOutput = self.fFunction(right, k2)  # Apply F function with k2
        firstXOR = bin((int(left, 2) ^ int(firstFOutput, 2)))[2:]  # XOR with left half
        firstXOR = self.padding(firstXOR, 4)
        secondFOutput = self.fFunction(firstXOR, k1)  # Apply F function with k1

        secondXOR = bin((int(right, 2) ^ int(secondFOutput, 2)))[2:]  # XOR with right half
        secondXOR = self.padding(secondXOR, 4)
        output = secondXOR + firstXOR  # Concatenate results

        return self.reversePermutation(output)  # Final permutation

class DESManual:
    # Initial Permutation (IP)
    IP = [58, 50, 42, 34, 26, 18, 10, 2,
          60, 52, 44, 36, 28, 20, 12, 4,
          62, 54, 46, 38, 30, 22, 14, 6,
          64, 56, 48, 40, 32, 24, 16, 8,
          57, 49, 41, 33, 25, 17, 9, 1,
          59, 51, 43, 35, 27, 19, 11, 3,
          61, 53, 45, 37, 29, 21, 13, 5,
          63, 55, 47, 39, 31, 23, 15, 7]

    # Final Permutation (FP) = IP^(-1)
    FP = [40, 8, 48, 16, 56, 24, 64, 32,
          39, 7, 47, 15, 55, 23, 63, 31,
          38, 6, 46, 14, 54, 22, 62, 30,
          37, 5, 45, 13, 53, 21, 61, 29,
          36, 4, 44, 12, 52, 20, 60, 28,
          35, 3, 43, 11, 51, 19, 59, 27,
          34, 2, 42, 10, 50, 18, 58, 26,
          33, 1, 41, 9, 49, 17, 57, 25]

    # Expansion Table (E)
    E = [32, 1, 2, 3, 4, 5,
         4, 5, 6, 7, 8, 9,
         8, 9, 10, 11, 12, 13,
         12, 13, 14, 15, 16, 17,
         16, 17, 18, 19, 20, 21,
         20, 21, 22, 23, 24, 25,
         24, 25, 26, 27, 28, 29,
         28, 29, 30, 31, 32, 1]

    # Permutation (P)
    P = [16, 7, 20, 21,
         29, 12, 28, 17,
         1, 15, 23, 26,
         5, 18, 31, 10,
         2, 8, 24, 14,
         32, 27, 3, 9,
         19, 13, 30, 6,
         22, 11, 4, 25]

    # S-Boxes
    S_BOX = [
        # S1
        [
            [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
            [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
            [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
            [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]
        ],
        # S2
        [
            [15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
            [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
            [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
            [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]
        ],
        # S3
        [
            [10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
            [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
            [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
            [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]
        ],
        # S4
        [
            [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
            [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
            [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
            [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]
        ],
        # S5
        [
            [2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
            [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
            [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
            [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]
        ],
        # S6
        [
            [12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
            [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
            [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
            [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]
        ],
        # S7
        [
            [4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
            [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
            [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
            [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]
        ],
        # S8
        [
            [13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
            [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
            [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
            [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]
        ]
    ]

    # PC1 Permutation
    PC1 = [57, 49, 41, 33, 25, 17, 9,
           1, 58, 50, 42, 34, 26, 18,
           10, 2, 59, 51, 43, 35, 27,
           19, 11, 3, 60, 52, 44, 36,
           63, 55, 47, 39, 31, 23, 15,
           7, 62, 54, 46, 38, 30, 22,
           14, 6, 61, 53, 45, 37, 29,
           21, 13, 5, 28, 20, 12, 4]

    # PC2 Permutation
    PC2 = [14, 17, 11, 24, 1, 5,
           3, 28, 15, 6, 21, 10,
           23, 19, 12, 4, 26, 8,
           16, 7, 27, 20, 13, 2,
           41, 52, 31, 37, 47, 55,
           30, 40, 51, 45, 33, 48,
           44, 49, 39, 56, 34, 53,
           46, 42, 50, 36, 29, 32]

    # Number of left shifts per round
    SHIFTS = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]

    def __init__(self):
        pass

    def _hex_to_bin(self, hex_str):
        # Pad with 0s to ensure full length depending on context (e.g., 64 bits)
        # But for arbitrary length:
        scale = 16 # equals to hexadecimal
        num_of_bits = len(hex_str) * 4
        return bin(int(hex_str, scale))[2:].zfill(num_of_bits)

    def _bin_to_hex(self, bin_str):
        return hex(int(bin_str, 2))[2:].upper()
    
    def _str_to_bin(self, s):
        return ''.join(format(ord(c), '08b') for c in s)
    
    def _bin_to_str(self, b):
        # Split into blocks of 8
        chars = [b[i:i+8] for i in range(0, len(b), 8)]
        return ''.join(chr(int(c, 2)) for c in chars)

    def _permute(self, bits, table):
        return ''.join([bits[x - 1] for x in table])

    def _xor(self, bits1, bits2):
        return ''.join(['1' if b1 != b2 else '0' for b1, b2 in zip(bits1, bits2)])

    def _left_shift(self, bits, n):
        return bits[n:] + bits[:n]

    def _generate_keys(self, key_hex):
        # 1. Convert to binary (64 bits)
        key_bin = self._hex_to_bin(key_hex).zfill(64)
        
        # 2. PC1 permutation -> 56 bits
        key_permuted = self._permute(key_bin, self.PC1)
        
        # 3. Split into C and D (28 bits each)
        c = key_permuted[:28]
        d = key_permuted[28:]
        
        round_keys = []
        for shift in self.SHIFTS:
            # 4. Left shift
            c = self._left_shift(c, shift)
            d = self._left_shift(d, shift)
            
            # 5. Concatenate and PC2 permuation -> 48 bits
            cd = c + d
            k = self._permute(cd, self.PC2)
            round_keys.append(k)
            
        return round_keys

    def _f_function(self, right_block, round_key):
        # 1. Expansion (32 -> 48 bits)
        expanded = self._permute(right_block, self.E)
        
        # 2. XOR with round key
        xored = self._xor(expanded, round_key)
        
        # 3. S-Boxes
        s_box_output = ""
        # Split into 8 groups of 6 bits
        for i in range(8):
            block = xored[i*6 : (i+1)*6]
            # Row: 1st and last bit
            row = int(block[0] + block[-1], 2)
            # Col: middle 4 bits
            col = int(block[1:5], 2)
            
            val = self.S_BOX[i][row][col]
            # Convert to 4-bit binary
            s_box_output += format(val, '04b')
            
        # 4. Permutation P
        final = self._permute(s_box_output, self.P)
        return final

    def encrypt_block(self, plaintext_hex, key_hex):
        """
        Encrypts a single 64-bit block (16 hex chars) with a 64-bit key.
        """
        # Ensure correct length
        pt_bin = self._hex_to_bin(plaintext_hex).zfill(64)
        
        # 1. Initial Permutation
        pt_permuted = self._permute(pt_bin, self.IP)
        
        # 2. Split L0, R0
        l = pt_permuted[:32]
        r = pt_permuted[32:]
        
        # 3. Generate Keys
        round_keys = self._generate_keys(key_hex)
        
        # 4. 16 Rounds
        for i in range(16):
            l_prev = l
            r_prev = r
            
            l = r_prev
            # L_new = R_old
            # R_new = L_old XOR f(R_old, K)
            r = self._xor(l_prev, self._f_function(r_prev, round_keys[i]))
            
        # 5. Swap (R16, L16)
        final_rl = r + l
        
        # 6. Final Permutation
        cipher_bin = self._permute(final_rl, self.FP)
        
        return self._bin_to_hex(cipher_bin).zfill(16)

    def decrypt_block(self, ciphertext_hex, key_hex):
        """
        Decrypts a single 64-bit block. Same as encrypt but keys reversed.
        """
        ct_bin = self._hex_to_bin(ciphertext_hex).zfill(64)
        
        ct_permuted = self._permute(ct_bin, self.IP)
        
        l = ct_permuted[:32]
        r = ct_permuted[32:]
        
        round_keys = self._generate_keys(key_hex)
        round_keys_reversed = round_keys[::-1]
        
        for i in range(16):
            l_prev = l
            r_prev = r
            
            l = r_prev
            r = self._xor(l_prev, self._f_function(r_prev, round_keys_reversed[i]))
            
        final_rl = r + l
        plain_bin = self._permute(final_rl, self.FP)
        
        return self._bin_to_hex(plain_bin).zfill(16)

    def pad(self, text):
        # PKCS5/7 padding for blocks of 8 bytes (64 bits)
        pad_len = 8 - (len(text) % 8)
        return text + chr(pad_len) * pad_len

    def unpad(self, text):
        pad_len = ord(text[-1])
        return text[:-pad_len]

    def encrypt(self, plaintext, key):
        # Helper for handling string input/output
        # Key should be hex string (16 chars = 64 bits) or converted to it.
        # Here assuming key is a 8-byte string, convert to hex
        key_hex = ''.join(format(ord(c), '02x') for c in key)
        
        # Pad plaintext
        padded_text = self.pad(plaintext)
        
        encrypted_hex = ""
        # Process in 8-byte blocks
        for i in range(0, len(padded_text), 8):
            block = padded_text[i:i+8]
            # Convert block to hex
            block_hex = ''.join(format(ord(c), '02x') for c in block)
            enc_block = self.encrypt_block(block_hex, key_hex)
            encrypted_hex += enc_block
            
        return encrypted_hex

    def decrypt(self, ciphertext_hex, key):
        key_hex = ''.join(format(ord(c), '02x') for c in key)
        
        decrypted_text = ""
        # Process in 16-hex-char blocks (64 bits)
        for i in range(0, len(ciphertext_hex), 16):
            block_hex = ciphertext_hex[i:i+16]
            dec_block_hex = self.decrypt_block(block_hex, key_hex)
            
            # Convert hex to chars
            # Careful with length (must be even)
            for j in range(0, len(dec_block_hex), 2):
                char_code = int(dec_block_hex[j:j+2], 16)
                decrypted_text += chr(char_code)
                
        return self.unpad(decrypted_text)

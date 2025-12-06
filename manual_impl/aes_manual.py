
class AESManual:
    # S-Box
    S_BOX = (
        0x63, 0x7C, 0x77, 0x7B, 0xF2, 0x6B, 0x6F, 0xC5, 0x30, 0x01, 0x67, 0x2B, 0xFE, 0xD7, 0xAB, 0x76,
        0xCA, 0x82, 0xC9, 0x7D, 0xFA, 0x59, 0x47, 0xF0, 0xAD, 0xD4, 0xA2, 0xAF, 0x9C, 0xA4, 0x72, 0xC0,
        0xB7, 0xFD, 0x93, 0x26, 0x36, 0x3F, 0xF7, 0xCC, 0x34, 0xA5, 0xE5, 0xF1, 0x71, 0xD8, 0x31, 0x15,
        0x04, 0xC7, 0x23, 0xC3, 0x18, 0x96, 0x05, 0x9A, 0x07, 0x12, 0x80, 0xE2, 0xEB, 0x27, 0xB2, 0x75,
        0x09, 0x83, 0x2C, 0x1A, 0x1B, 0x6E, 0x5A, 0xA0, 0x52, 0x3B, 0xD6, 0xB3, 0x29, 0xE3, 0x2F, 0x84,
        0x53, 0xD1, 0x00, 0xED, 0x20, 0xFC, 0xB1, 0x5B, 0x6A, 0xCB, 0xBE, 0x39, 0x4A, 0x4C, 0x58, 0xCF,
        0xD0, 0xEF, 0xAA, 0xFB, 0x43, 0x4D, 0x33, 0x85, 0x45, 0xF9, 0x02, 0x7F, 0x50, 0x3C, 0x9F, 0xA8,
        0x51, 0xA3, 0x40, 0x8F, 0x92, 0x9D, 0x38, 0xF5, 0xBC, 0xB6, 0xDA, 0x21, 0x10, 0xFF, 0xF3, 0xD2,
        0xCD, 0x0C, 0x13, 0xEC, 0x5F, 0x97, 0x44, 0x17, 0xC4, 0xA7, 0x7E, 0x3D, 0x64, 0x5D, 0x19, 0x73,
        0x60, 0x81, 0x4F, 0xDC, 0x22, 0x2A, 0x90, 0x88, 0x46, 0xEE, 0xB8, 0x14, 0xDE, 0x5E, 0x0B, 0xDB,
        0xE0, 0x32, 0x3A, 0x0A, 0x49, 0x06, 0x24, 0x5C, 0xC2, 0xD3, 0xAC, 0x62, 0x91, 0x95, 0xE4, 0x79,
        0xE7, 0xC8, 0x37, 0x6D, 0x8D, 0xD5, 0x4E, 0xA9, 0x6C, 0x56, 0xF4, 0xEA, 0x65, 0x7A, 0xAE, 0x08,
        0xBA, 0x78, 0x25, 0x2E, 0x1C, 0xA6, 0xB4, 0xC6, 0xE8, 0xDD, 0x74, 0x1F, 0x4B, 0xBD, 0x8B, 0x8A,
        0x70, 0x3E, 0xB5, 0x66, 0x48, 0x03, 0xF6, 0x0E, 0x61, 0x35, 0x57, 0xB9, 0x86, 0xC1, 0x1D, 0x9E,
        0xE1, 0xF8, 0x98, 0x11, 0x69, 0xD9, 0x8E, 0x94, 0x9B, 0x1E, 0x87, 0xE9, 0xCE, 0x55, 0x28, 0xDF,
        0x8C, 0xA1, 0x89, 0x0D, 0xBF, 0xE6, 0x42, 0x68, 0x41, 0x99, 0x2D, 0x0F, 0xB0, 0x54, 0xBB, 0x16,
    )

    # Inverse S-Box (INV_S_BOX)
    INV_S_BOX = (
        0x52, 0x09, 0x6A, 0xD5, 0x30, 0x36, 0xA5, 0x38, 0xBF, 0x40, 0xA3, 0x9E, 0x81, 0xF3, 0xD7, 0xFB,
        0x7C, 0xE3, 0x39, 0x82, 0x9B, 0x2F, 0xFF, 0x87, 0x34, 0x8E, 0x43, 0x44, 0xC4, 0xDE, 0xE9, 0xCB,
        0x54, 0x7B, 0x94, 0x32, 0xA6, 0xC2, 0x23, 0x3D, 0xEE, 0x4C, 0x95, 0x0B, 0x42, 0xFA, 0xC3, 0x4E,
        0x08, 0x2E, 0xA1, 0x66, 0x28, 0xD9, 0x24, 0xB2, 0x76, 0x5B, 0xA2, 0x49, 0x6D, 0x8B, 0xD1, 0x25,
        0x72, 0xF8, 0xF6, 0x64, 0x86, 0x68, 0x98, 0x16, 0xD4, 0xA4, 0x5C, 0xCC, 0x5D, 0x65, 0xB6, 0x92,
        0x6C, 0x70, 0x48, 0x50, 0xFD, 0xED, 0xB9, 0xDA, 0x5E, 0x15, 0x46, 0x57, 0xA7, 0x8D, 0x9D, 0x84,
        0x90, 0xD8, 0xAB, 0x00, 0x8C, 0xBC, 0xD3, 0x0A, 0xF7, 0xE4, 0x58, 0x05, 0xB8, 0xB3, 0x45, 0x06,
        0xD0, 0x2C, 0x1E, 0x8F, 0xCA, 0x3F, 0x0F, 0x02, 0xC1, 0xAF, 0xBD, 0x03, 0x01, 0x13, 0x8A, 0x6B,
        0x3A, 0x91, 0x11, 0x41, 0x4F, 0x67, 0xDC, 0xEA, 0x97, 0xF2, 0xCF, 0xCE, 0xF0, 0xB4, 0xE6, 0x73,
        0x96, 0xAC, 0x74, 0x22, 0xE7, 0xAD, 0x35, 0x85, 0xE2, 0xF9, 0x37, 0xE8, 0x1C, 0x75, 0xDF, 0x6E,
        0x47, 0xF1, 0x1A, 0x71, 0x1D, 0x29, 0xC5, 0x89, 0x6F, 0xB7, 0x62, 0x0E, 0xAA, 0x18, 0xBE, 0x1B,
        0xFC, 0x56, 0x3E, 0x4B, 0xC6, 0xD2, 0x79, 0x20, 0x9A, 0xDB, 0xC0, 0xFE, 0x78, 0xCD, 0x5A, 0xF4,
        0x1F, 0xDD, 0xA8, 0x33, 0x88, 0x07, 0xC7, 0x31, 0xB1, 0x12, 0x10, 0x59, 0x27, 0x80, 0xEC, 0x5F,
        0x60, 0x51, 0x7F, 0xA9, 0x19, 0xB5, 0x4A, 0x0D, 0x2D, 0xE5, 0x7A, 0x9F, 0x93, 0xC9, 0x9C, 0xEF,
        0xA0, 0xE0, 0x3B, 0x4D, 0xAE, 0x2A, 0xF5, 0xB0, 0xC8, 0xEB, 0xBB, 0x3C, 0x83, 0x53, 0x99, 0x61,
        0x17, 0x2B, 0x04, 0x7E, 0xBA, 0x77, 0xD6, 0x26, 0xE1, 0x69, 0x14, 0x63, 0x55, 0x21, 0x0C, 0x7D,
    )

    # Round Constant (Rcon)
    RCON = (
        0x00, 0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40,
        0x80, 0x1B, 0x36, 0x6C, 0xD8, 0xAB, 0x4D, 0x9A,
        0x2F, 0x5E, 0xBC, 0x63, 0xC6, 0x97, 0x35, 0x6A,
        0xD4, 0xB3, 0x7D, 0xFA, 0xEF, 0xC5, 0x91, 0x39,
    )

    def __init__(self, key):
        """
        Initializes AES with a 128-bit key (16 bytes).
        Does not support 192 or 256 for simplicity in this demo.
        """
        if len(key) != 16:
            raise ValueError("Key size must be 16 bytes for this implementation")
        # Ensure key is list of integers (bytes)
        self.key = [ord(c) for c in key] if isinstance(key, str) else list(key)
        self.n_rounds = 10
        self._expand_key()

    def _expand_key(self):
        self.round_keys = self.key[:]
        for i in range(4, 4 * (self.n_rounds + 1)):
            temp = self.round_keys[(i-1)*4 : i*4]
            if i % 4 == 0:
                # RotWord
                temp = temp[1:] + temp[:1]
                # SubWord
                temp = [self.S_BOX[b] for b in temp]
                # XOR with Rcon
                temp[0] ^= self.RCON[i // 4]
            
            prev_key_chunk = self.round_keys[(i-4)*4 : (i-3)*4]
            new_key_chunk = [a ^ b for a, b in zip(prev_key_chunk, temp)]
            self.round_keys.extend(new_key_chunk)

    def _add_round_key(self, state, round_key):
        return [s ^ k for s, k in zip(state, round_key)]

    def _sub_bytes(self, state):
        return [self.S_BOX[b] for b in state]

    def _inv_sub_bytes(self, state):
        return [self.INV_S_BOX[b] for b in state]

    def _shift_rows(self, state):
        # State is 16 bytes (4x4 column major, but let's treat as row major for simplicity if consistent)
        # Standard AES uses column-major order.
        # Let's verify standard: 
        # In:  0  4  8 12
        #      1  5  9 13
        #      2  6 10 14
        #      3  7 11 15
        
        # But a linear array [0..15] is usually row by row in simple impl,
        # OR we can just implement the shifting logic on the linear array assuming it's row-major 
        # (0 1 2 3 is row 0)
        # Let's stick to row-major [0,1,2,3] is row 0.
        
        s = list(state)
        # Row 1 (Shift 1)
        s[4:8] = s[5:8] + s[4:5]
        # Row 2 (Shift 2)
        s[8:12] = s[10:12] + s[8:10]
        # Row 3 (Shift 3)
        s[12:16] = s[15:16] + s[12:15]
        return s

    def _inv_shift_rows(self, state):
        s = list(state)
        # Row 1 (Inv Shift 1 = Right Shift 1)
        s[4:8] = s[7:8] + s[4:7]
        # Row 2 (Inv Shift 2 = Right Shift 2)
        s[8:12] = s[10:12] + s[8:10] # same as left 2
        # Row 3 (Inv Shift 3 = Right Shift 3)
        s[12:16] = s[13:16] + s[12:13]
        return s

    def _xtime(self, a):
        # Multiply by 2 in GF(2^8)
        return ((a << 1) ^ 0x1B) & 0xFF if (a & 0x80) else (a << 1) & 0xFF

    def _mix_single_column(self, a):
        # a is list of 4 bytes
        t = a[0] ^ a[1] ^ a[2] ^ a[3]
        u = a[0]
        a[0] ^= t ^ self._xtime(a[0] ^ a[1])
        a[1] ^= t ^ self._xtime(a[1] ^ a[2])
        a[2] ^= t ^ self._xtime(a[2] ^ a[3])
        a[3] ^= t ^ self._xtime(a[3] ^ u)
        return a

    def _mix_columns(self, state):
        # Works on columns. Since we used row-major, we need to extract cols[0,4,8,12] etc
        s = list(state)
        for i in range(4):
            # Construct column
            col = [s[i], s[i+4], s[i+8], s[i+12]]
            col = self._mix_single_column(col)
            # Put back
            s[i] = col[0]
            s[i+4] = col[1]
            s[i+8] = col[2]
            s[i+12] = col[3]
        return s

    def _inv_mix_columns(self, state):
        # Unmix is slightly different logic, effectively multiplying by inverse matrix
        # Multiply by 0e, 0b, 0d, 09
        # This is complex to implement with just xtime. 
        # A simpler trick: InvMixColumns(s) == MixColumns(s) using different coeffs
        # Or... InvMixColumns is applied to the keys in efficient implementations.
        # Let's do standard multiplication.
        
        def gmul(a, b):
            p = 0
            for _ in range(8):
                if b & 1:
                    p ^= a
                a = self._xtime(a)
                b >>= 1
            return p

        s = list(state)
        for i in range(4):
            c = [s[i], s[i+4], s[i+8], s[i+12]]
            # 0e 0b 0d 09
            s[i]    = gmul(c[0],14) ^ gmul(c[1],11) ^ gmul(c[2],13) ^ gmul(c[3],9)
            s[i+4]  = gmul(c[0],9)  ^ gmul(c[1],14) ^ gmul(c[2],11) ^ gmul(c[3],13)
            s[i+8]  = gmul(c[0],13) ^ gmul(c[1],9)  ^ gmul(c[2],14) ^ gmul(c[3],11)
            s[i+12] = gmul(c[0],11) ^ gmul(c[1],13) ^ gmul(c[2],9)  ^ gmul(c[3],14)
        return s

    def encrypt_block(self, plaintext):
        # Plaintext is list of 16 bytes
        state = list(plaintext)
        
        # Initial Round Key Add
        initial_key = self.round_keys[:16]
        state = self._add_round_key(state, initial_key)
        
        # Rounds 1 to 9
        for i in range(1, self.n_rounds):
            state = self._sub_bytes(state)
            state = self._shift_rows(state)
            state = self._mix_columns(state)
            
            round_key = self.round_keys[i*16 : (i+1)*16]
            state = self._add_round_key(state, round_key)
            
        # Round 10 (No MixColumns)
        state = self._sub_bytes(state)
        state = self._shift_rows(state)
        final_key = self.round_keys[self.n_rounds*16 : (self.n_rounds+1)*16]
        state = self._add_round_key(state, final_key)
        
        return state

    def decrypt_block(self, ciphertext):
        state = list(ciphertext)
        
        final_key = self.round_keys[self.n_rounds*16 : (self.n_rounds+1)*16]
        state = self._add_round_key(state, final_key)
        state = self._inv_shift_rows(state)
        state = self._inv_sub_bytes(state)
        
        for i in range(self.n_rounds - 1, 0, -1):
            round_key = self.round_keys[i*16 : (i+1)*16]
            state = self._add_round_key(state, round_key)
            state = self._inv_mix_columns(state)
            state = self._inv_shift_rows(state)
            state = self._inv_sub_bytes(state)
            
        initial_key = self.round_keys[:16]
        state = self._add_round_key(state, initial_key)
        return state

    def pad(self, text):
        pad_len = 16 - (len(text) % 16)
        return text + chr(pad_len) * pad_len

    def unpad(self, text):
        pad_len = ord(text[-1])
        return text[:-pad_len]

    def encrypt(self, plaintext):
        # Helper for hex output
        padded = self.pad(plaintext)
        encrypted_bytes = []
        for i in range(0, len(padded), 16):
            block = [ord(c) for c in padded[i:i+16]]
            enc_block = self.encrypt_block(block)
            encrypted_bytes.extend(enc_block)
            
        return ''.join(format(b, '02x') for b in encrypted_bytes)

    def decrypt(self, ciphertext_hex):
        encrypted_bytes = []
        for i in range(0, len(ciphertext_hex), 2):
            encrypted_bytes.append(int(ciphertext_hex[i:i+2], 16))
            
        decrypted_chars = []
        for i in range(0, len(encrypted_bytes), 16):
            block = encrypted_bytes[i:i+16]
            dec_block = self.decrypt_block(block)
            decrypted_chars.extend(chr(b) for b in dec_block)
            
        return self.unpad(''.join(decrypted_chars))

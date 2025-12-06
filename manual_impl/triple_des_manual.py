from des_manual import DESManual

class TripleDESManual:
    def __init__(self):
        self.des = DESManual()

    def encrypt(self, plaintext, key):
        """
        3DES Encryption (EDE mode): Encrypt(K1) -> Decrypt(K2) -> Encrypt(K3)
        Key: 16 bytes (K1=K3) or 24 bytes (K1, K2, K3)
        """
        # Key management
        if len(key) == 16:
            k1 = key[:8]
            k2 = key[8:16]
            k3 = k1
        elif len(key) == 24:
            k1 = key[:8]
            k2 = key[8:16]
            k3 = key[16:24]
        else:
            raise ValueError("Key must be 16 or 24 bytes")

        # 1. Encrypt with K1
        # process block by block manually below
        
        # 2. Decrypt with K2
        # des decrypt takes hex string and returns plaintext (utf-8)
        # BUT here we need to keep it as raw bytes/hex for the next stage
        # So we cannot use self.des.decrypt directly because it unpads and decodes chars
        # We need block-level operations
        
        # We need to manually handle the blocks to avoid padding/unpadding in the middle
        # Let's refactor to process block by block
        
        # Convert plaintext to padded blocks first
        padded_text = self.des.pad(plaintext)
        
        # Prepare keys in hex
        if isinstance(key, str):
            k1_hex = ''.join(format(ord(c), '02x') for c in k1)
            k2_hex = ''.join(format(ord(c), '02x') for c in k2)
            k3_hex = ''.join(format(ord(c), '02x') for c in k3)
        else:
            k1_hex = ''.join(format(c, '02x') for c in k1)
            k2_hex = ''.join(format(c, '02x') for c in k2)
            k3_hex = ''.join(format(c, '02x') for c in k3)
        
        final_hex = ""
        
        for i in range(0, len(padded_text), 8):
            block = padded_text[i:i+8]
            block_hex = ''.join(format(ord(c), '02x') for c in block)
            
            # Encrypt K1
            e1 = self.des.encrypt_block(block_hex, k1_hex)
            
            # Decrypt K2
            d2 = self.des.decrypt_block(e1, k2_hex)
            
            # Encrypt K3
            e3 = self.des.encrypt_block(d2, k3_hex)
            
            final_hex += e3
            
        return final_hex

    def decrypt(self, ciphertext_hex, key):
        """
        3DES Decryption: Decrypt(K3) -> Encrypt(K2) -> Decrypt(K1)
        """
        if len(key) == 16:
            k1 = key[:8]
            k2 = key[8:16]
            k3 = k1
        elif len(key) == 24:
            k1 = key[:8]
            k2 = key[8:16]
            k3 = key[16:24]
        else:
            raise ValueError("Key must be 16 or 24 bytes")
            
        if isinstance(key, str):
             k1_hex = ''.join(format(ord(c), '02x') for c in k1)
             k2_hex = ''.join(format(ord(c), '02x') for c in k2)
             k3_hex = ''.join(format(ord(c), '02x') for c in k3)
        else:
             # If key was bytes/list of ints
             k1_hex = ''.join(format(c, '02x') for c in k1)
             k2_hex = ''.join(format(c, '02x') for c in k2)
             k3_hex = ''.join(format(c, '02x') for c in k3)
        
        decrypted_text = ""
        
        # Process 16-char hex blocks (64 bits)
        for i in range(0, len(ciphertext_hex), 16):
            block_hex = ciphertext_hex[i:i+16]
            
            # Decrypt K3
            d3 = self.des.decrypt_block(block_hex, k3_hex)
            
            # Encrypt K2
            e2 = self.des.encrypt_block(d3, k2_hex)
            
            # Decrypt K1
            d1 = self.des.decrypt_block(e2, k1_hex)
            
            # Convert hex to chars
            for j in range(0, len(d1), 2):
                char_code = int(d1[j:j+2], 16)
                decrypted_text += chr(char_code)
                
        return self.des.unpad(decrypted_text)

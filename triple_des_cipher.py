from Crypto.Cipher import DES3
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
import base64

class TripleDESCipher:
    def __init__(self, key):
        """
        Initialize 3DES Cipher with a key.
        Key length must be 16 or 24 bytes.
        """
        self.key = key

    def encrypt(self, plaintext):
        """
        Encrypts plaintext using 3DES-CBC mode with PKCS7 padding.
        Returns base64 encoded string containing IV + Ciphertext.
        """
        iv = get_random_bytes(DES3.block_size)
        cipher = DES3.new(self.key, DES3.MODE_CBC, iv)
        padded_data = pad(plaintext.encode('utf-8'), DES3.block_size)
        encrypted_data = cipher.encrypt(padded_data)
        return base64.b64encode(iv + encrypted_data).decode('utf-8')

    def decrypt(self, encrypted_text):
        """
        Decrypts base64 encoded string containing IV + Ciphertext.
        """
        encrypted_data = base64.b64decode(encrypted_text)
        iv = encrypted_data[:DES3.block_size]
        cipher = DES3.new(self.key, DES3.MODE_CBC, iv)
        ciphertext = encrypted_data[DES3.block_size:]
        original_data = unpad(cipher.decrypt(ciphertext), DES3.block_size)
        return original_data.decode('utf-8')

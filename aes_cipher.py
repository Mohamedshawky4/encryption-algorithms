from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
import base64

class AESCipher:
    def __init__(self, key):
        """
        Initialize AithES Cipher w a key.
        Key length must be 16 (AES-128), 24 (AES-192), or 32 (AES-256) bytes.
        """
        self.key = key

    def encrypt(self, plaintext):
        """
        Encrypts plaintext using AES-CBC mode with PKCS7 padding.
        Returns base64 encoded string containing IV + Ciphertext.
        """
        iv = get_random_bytes(AES.block_size)
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        padded_data = pad(plaintext.encode('utf-8'), AES.block_size)
        encrypted_data = cipher.encrypt(padded_data)
        return base64.b64encode(iv + encrypted_data).decode('utf-8')

    def decrypt(self, encrypted_text):
        """
        Decrypts base64 encoded string containing IV + Ciphertext.
        """
        encrypted_data = base64.b64decode(encrypted_text)
        iv = encrypted_data[:AES.block_size]
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        ciphertext = encrypted_data[AES.block_size:]
        original_data = unpad(cipher.decrypt(ciphertext), AES.block_size)
        return original_data.decode('utf-8')

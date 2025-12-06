import os
from aes_cipher import AESCipher
from des_cipher import DESCipher
from triple_des_cipher import TripleDESCipher

def main():
    print("=== Data Security Project - Encryption Demo ===")
    
    # 1. AES Demo
    print("\n--- AES Encryption ---")
    aes_key = os.urandom(16) # 16 bytes for AES-128
    aes = AESCipher(aes_key)
    text = "Confidential Data"
    encrypted = aes.encrypt(text)
    decrypted = aes.decrypt(encrypted)
    print(f"Original: {text}")
    print(f"Encrypted: {encrypted}")
    print(f"Decrypted: {decrypted}")
    assert text == decrypted, "AES Encryption/Decryption failed!"

    # 2. DES Demo
    print("\n--- DES Encryption ---")
    des_key = os.urandom(8) # 8 bytes for DES
    des = DESCipher(des_key)
    text = "Secret!!"
    encrypted = des.encrypt(text)
    decrypted = des.decrypt(encrypted)
    print(f"Original: {text}")
    print(f"Encrypted: {encrypted}")
    print(f"Decrypted: {decrypted}")
    assert text == decrypted, "DES Encryption/Decryption failed!"

    # 3. 3DES Demo
    print("\n--- 3DES Encryption ---")
    tdes_key = os.urandom(16) # 16 bytes for 3DES (Option 2) or 24 bytes (Option 3)
    # Note: 3DES key can be 16 or 24 bytes. 
    tdes = TripleDESCipher(tdes_key)
    text = "Top Secret Data!"
    encrypted = tdes.encrypt(text)
    decrypted = tdes.decrypt(encrypted)
    print(f"Original: {text}")
    print(f"Encrypted: {encrypted}")
    print(f"Decrypted: {decrypted}")
    assert text == decrypted, "3DES Encryption/Decryption failed!"

    print("\n=== All Tests Passed Successfully ===")

if __name__ == "__main__":
    main()

import os
from aes_manual import AESManual
from des_manual import DESManual
from triple_des_manual import TripleDESManual

def main():
    print("=== Manual Encryption Implementation Demo (Pure Python) ===")
    print("WARNING: Educational use only. Not side-channel resistant.\n")
    
    # 1. AES Manual Demo
    print("--- AES Manual Encryption ---")
    key_str = "Thats my Kung Fu" # 16 bytes
    print(f"Key: {key_str}")
    aes = AESManual(key_str)
    
    text = "Two One Nine Two" # 16 bytes
    print(f"Original: {text}")
    
    encrypted = aes.encrypt(text)
    print(f"Encrypted (Hex): {encrypted}")
    
    decrypted = aes.decrypt(encrypted)
    print(f"Decrypted: {decrypted}")
    
    assert text == decrypted, "Manual AES Failed!"
    print("AES Check: PASS")

    # 2. DES Manual Demo
    print("\n--- DES Manual Encryption ---")
    des_key = "secretk." # 8 bytes
    print(f"Key: {des_key}")
    des = DESManual()
    
    text_des = "HelloDES"
    print(f"Original: {text_des}")
    
    # Note: Our DESManual.encrypt takes text and key(str)
    encrypted_des = des.encrypt(text_des, des_key)
    print(f"Encrypted (Hex): {encrypted_des}")
    
    decrypted_des = des.decrypt(encrypted_des, des_key)
    print(f"Decrypted: {decrypted_des}")
    
    assert text_des == decrypted_des, "Manual DES Failed!"
    print("DES Check: PASS")

    # 3. 3DES Manual Demo
    print("\n--- 3DES Manual Encryption ---")
    tdes_key = "secretk.secretk." # 16 bytes (K1=K3)
    print(f"Key: {tdes_key}")
    tdes = TripleDESManual()
    
    text_tdes = "Hello3DESWorld!!"
    print(f"Original: {text_tdes}")
    
    encrypted_tdes = tdes.encrypt(text_tdes, tdes_key)
    print(f"Encrypted (Hex): {encrypted_tdes}")
    
    decrypted_tdes = tdes.decrypt(encrypted_tdes, tdes_key)
    print(f"Decrypted: '{decrypted_tdes}'")
    
    if text_tdes != decrypted_tdes:
        print(f"MISMATCH! \nExpected: {list(text_tdes.encode())} \nGot: {list(decrypted_tdes.encode())}")
        print(f"Decrypted Hex Chars: {[hex(ord(c)) for c in decrypted_tdes]}")
    
    assert text_tdes == decrypted_tdes, "Manual 3DES Failed!"
    print("3DES Check: PASS")
    
    print("\n=== All Manual Tests Passed ===")

if __name__ == "__main__":
    main()

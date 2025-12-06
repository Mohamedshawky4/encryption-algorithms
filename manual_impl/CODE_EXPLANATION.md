# Encryption Code Explanation

This document provides a detailed breakdown of the manual encryption implementations found in the `manual_impl` directory. These scripts implement AES, DES, and Triple DES algorithms from scratch in Python for educational purposes.

---

## 1. `aes_manual.py` (AES Implementation)

 This file implements the **Advanced Encryption Standard (AES)** algorithm. It supports 128-bit keys (16 bytes).

### **Class `AESManual`**

*   **Constants**:
    *   `S_BOX`: Substitution box for non-linearity during encryption.
    *   `INV_S_BOX`: Inverse S-Box for decryption.
    *   `RCON`: Round constants used in the Key Expansion phase.

*   **`__init__(self, key)`**:
    *   Initializes the class with a 16-byte key.
    *   Calls `_expand_key()` to generate the round keys needed for all 10 encryption rounds.

### **Core Key Operations**

*   **`_expand_key(self)`**:
    *   Expands the initial 16-byte key into 44 words (176 bytes) to provide a unique key for each round.
    *   Uses `RotWord` (rotate), `SubWord` (s-box substitution), and XORing with `RCON`.

### **Encryption Transformations**

*   **`_sub_bytes(self, state)`**: Replaces every byte in the state with a corresponding byte from the `S_BOX`.
*   **`_shift_rows(self, state)`**: Cyclically shifts rows of the state matrix to the left (Row 0: 0, Row 1: 1, Row 2: 2, Row 3: 3).
*   **`_mix_columns(self, state)`**: Mixes columns linearly used Galois Field multiplication to provide diffusion. It uses helper functions `_xtime` (multiply by 2) and `_mix_single_column`.
*   **`_add_round_key(self, state, round_key)`**: XORs the current state with the round key.

### **Decryption Transformations**
*   **`_inv_sub_bytes`**, **`_inv_shift_rows`**, **`_inv_mix_columns`**: The mathematical inverses of the encryption steps.

### **Main Logic**

*   **`encrypt_block(self, plaintext)`**:
    *   Takes a 16-byte block.
    *   **Round 0**: Add Round Key.
    *   **Rounds 1-9**: SubBytes -> ShiftRows -> MixColumns -> AddRoundKey.
    *   **Round 10**: SubBytes -> ShiftRows -> AddRoundKey (No MixColumns).
    
*   **`decrypt_block(self, ciphertext)`**:
    *   Reverses the operations. Order is: AddRoundKey -> InvShiftRows -> InvSubBytes -> (Loop [AddRoundKey -> InvMixColumns -> InvShiftRows -> InvSubBytes]) -> AddRoundKey.

*   **`encrypt(self, plaintext)`** / **`decrypt(self, ciphertext_hex)`**:
    *   Handles **PKCS#7 Padding** (`pad`/`unpad`) to ensure text length is a multiple of 16 bytes.
    *   Process the text in 16-byte chunks.
    *   Returns the result as a Hexadecimal string.

---

## 2. `des_manual.py` (DES Implementation)

This file implements the **Data Encryption Standard (DES)** algorithm. It operates on 64-bit blocks using a 56-bit key (supplied as 64 bits/8 bytes).

### **Class `DESManual`**

*   **Constants**:
    *   `IP` & `FP`: Initial and Final Permutation tables.
    *   `E`: Expansion table (expand 32 bits to 48).
    *   `P`: Permutation table for the Feistel function output.
    *   `S_BOX`: 8 Substitution boxes used to shrink 48 bits back to 32 bits.
    *   `PC1`, `PC2`, `SHIFTS`: Key schedule definitions.

### **Helper Functions**
*   `_hex_to_bin`, `_bin_to_hex`, `_xor`, `_permute`: Low-level bit manipulation helpers to handle binary strings and permutations.

### **Key Schedule**

*   **`_generate_keys(self, key_hex)`**:
    *   Converts hex key to binary.
    *   Applies `PC1` (drops parity bits, 64 -> 56 bits).
    *   Splits into C and D halves.
    *   Loops 16 times: Left shifts C and D according to `SHIFTS`, then applies `PC2` (56 -> 48 bits) to get the subkey for that round.

### **Feistel Function (`_f_function`)**

*   This is the core of DES functionality, applied in every round:
    1.  **Expansion**: Expands right half (32 bits) to 48 bits using `E`.
    2.  **XOR**: XORs result with the 48-bit round key.
    3.  **S-Box**: Splits 48 bits into 8 chunks of 6. Each chunk uses an S-Box to output 4 bits. (48 bits -> 32 bits).
    4.  **Permutation**: Permutes the result using `P`.

### **Main Logic**

*   **`encrypt_block(self, plaintext_hex, key_hex)`**:
    *   Applies **Initial Permutation (IP)**.
    *   Splits into Left (L) and Right (R) halves.
    *   Runs 16 rounds of the Feistel structure: $L_{new} = R_{old}$, $R_{new} = L_{old} \oplus f(R_{old}, K_i)$.
    *   Swaps final L and R.
    *   Applies **Final Permutation (FP)**.

*   **`decrypt_block(self, ciphertext_hex, key_hex)`**:
    *   Identical to encryption but uses the round keys in **reverse order**.

---

## 3. `triple_des_manual.py` (3DES Implementation)

This file implements **Triple DES (3DES)**, which effectively runs DES three times to improve security.

### **Class `TripleDESManual`**

*   **Dependency**: Imports and uses `DESManual` for the underlying block operations.

### **Main Logic**

*   **`encrypt(self, plaintext, key)`**:
    *   Supports 16-byte (2 keys, K1=K3) or 24-byte (3 keys) inputs.
    *   Uses **EDE Mode** (Encrypt-Decrypt-Encrypt):
        1.  **Encrypt** block with Key 1.
        2.  **Decrypt** the result with Key 2.
        3.  **Encrypt** the result with Key 3.
    *   Handling is done block-by-block manually to avoid padding issues between the internal steps.

*   **`decrypt(self, ciphertext_hex, key)`**:
    *   Reverses the operation: **Decrypt-Encrypt-Decrypt**:
        1.  **Decrypt** with Key 3.
        2.  **Encrypt** with Key 2.
        3.  **Decrypt** with Key 1.

---

## 4. `manual_demo.py` (Demonstration)

This script runs a demonstration to verify that all algorithms work correctly.

*   **`main()`**:
    1.  **AES Demo**: Encrypts "Twice One Nine Two" with a sample key, prints hex output, decrypts it back, and asserts equality.
    2.  **DES Demo**: Encrypts "HelloDES" with an 8-byte key, verifies encryption and decryption.
    3.  **3DES Demo**: Encrypts "Hello3DESWorld!!" with a 16-byte key (using K1=K3 logic), verifies correctness.

# Data Security Project - Encryption Implementations

This project contains Python implementations of AES, DES, and 3DES encryption algorithms using the `pycryptodome` library.

## Installation & Setup

### 1. Verification
Ensure you have Python 3.x installed:
- **Windows**: `python --version`
- **Mac/Linux**: `python3 --version`

### 2. Set up Virtual Environment & Install Dependencies

#### Windows
```powershell
# Open Command Prompt or PowerShell
# Navigate to the project directory
cd "path\to\task-dataSec"

# Create virtual environment
python -m venv venv

# Activate virtual environment
.\venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

#### Mac / Linux
```bash
# Open Terminal
# Navigate to the project directory
cd /path/to/task-dataSec

# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

## Files

- `aes_cipher.py`: AES encryption (128/192/256-bit keys).
- `des_cipher.py`: DES encryption (64-bit key, effective 56-bit).
- `triple_des_cipher.py`: 3DES encryption (16 or 24 byte keys).
- `main_demo.py`: Run this to see a demo of all 3 algorithms.

## Code Usage Examples

### 1. AES Encryption
```python
from aes_cipher import AESCipher
import os

# Key must be 16, 24, or 32 bytes
key = os.urandom(16) 
aes = AESCipher(key)

ciphertext = aes.encrypt("Hello World")
print(f"Encrypted: {ciphertext}")

plaintext = aes.decrypt(ciphertext)
print(f"Decrypted: {plaintext}")
```

### 2. DES Encryption
```python
from des_cipher import DESCipher
import os

# Key must be 8 bytes
key = os.urandom(8)
des = DESCipher(key)

ciphertext = des.encrypt("Hello World")
plaintext = des.decrypt(ciphertext)
```

### 3. 3DES Encryption
```python
from triple_des_cipher import TripleDESCipher
import os

# Key must be 16 or 24 bytes
key = os.urandom(16)
tdes = TripleDESCipher(key)

ciphertext = tdes.encrypt("Hello World")
plaintext = tdes.decrypt(ciphertext)
```

## Running the Demos

### 1. Library-based Implementation (PyCryptodome)
This runs the demo using the optimized `pycryptodome` library.

**Windows:**
```powershell
python main_demo.py
```

**Mac / Linux:**
```bash
python3 main_demo.py
```

### 2. Manual Implementation (Educational)
This runs the demo using the algorithms implemented from scratch (for learning purposes).

**Windows:**
```powershell
python manual_impl/manual_demo.py
```

**Mac / Linux:**
```bash
python3 manual_impl/manual_demo.py
```

## Troubleshooting

**ModuleNotFoundError: No module named 'Crypto'**

If you see this error, it means `pycryptodome` is not installed in the Python environment you are using.

If you are using Anaconda, try running:
```bash
"C:/Users/Mohamed/anaconda3/python.exe" -m pip install pycryptodome
```

And then run the demo using the same python executable:
```bash
"C:/Users/Mohamed/anaconda3/python.exe" main_demo.py
```

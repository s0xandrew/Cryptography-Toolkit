# 🔐 Cryptography Toolkit

A Python-based cryptography toolkit covering classical ciphers, 
modern hashing algorithms, Base64 encoding, and password strength analysis.

Built as part of my self-taught cybersecurity sprint for 
IIT Kanpur B.Cyber application (Wadhwani School of AI and Intelligent Systems).

---

## ⚡ Features

- **Caesar Cipher** — Encrypt, decrypt, and brute force attack
- **Vigenère Cipher** — Keyword-based polyalphabetic encryption/decryption
- **Hashing** — MD5, SHA1, SHA256, SHA512 with security explanations
- **File Hashing** — SHA256 integrity verification for any file
- **Base64** — Encode and decode (common in malware and JWT tokens)
- **Password Analyzer** — Strength scoring + brute force crack time estimation
- **Interactive Menu** — Clean CLI interface for all operations

---

## 🛠️ Setup & Installation

**Requirements:** Python 3.x (zero external libraries)

```bash
# Clone the repository
git clone https://github.com/s0xandrew/cryptography-toolkit.git
cd cryptography-toolkit

# Run the toolkit
python crypto.py
```

---

## 📸 Sample Output
CRYPTOGRAPHY TOOLKIT

By Sourabh (s0xandrew) | Educational Use Only
[MENU]

Caesar Cipher — Encrypt
Caesar Cipher — Decrypt
Caesar Cipher — Brute Force Attack
Vigenère Cipher — Encrypt
Vigenère Cipher — Decrypt
Hash Text (MD5/SHA1/SHA256/SHA512)
Hash File
Base64 Encode
Base64 Decode
Password Strength Analyzer

--- Caesar Cipher ---

Input:  IT IS HERE  |  Shift: 3

Encrypted: LW LV KHUH

Decrypted: IT IS HERE
--- Password Analysis ---

Password: ********

Strength: WEAK 🔴 (Score: 2/7)

Estimated crack time: 3 seconds
--- SHA256 Hash ---

Input: 'hello world'

SHA256: b94d27b9934d3e08a52e52d7da7dabfa...
---

## 🧠 How It Works

### Caesar Cipher
Each letter is shifted by a fixed number in the alphabet.
With only 25 possible keys, it can be broken by brute force
in milliseconds — this is why modern encryption uses key spaces
of 2^128 or larger.

### Vigenère Cipher
Uses a repeating keyword where each letter defines a different
shift value. Polyalphabetic substitution — much stronger than
Caesar but broken by frequency analysis (Kasiski examination).

### Cryptographic Hashing
One-way functions that produce fixed-length fingerprints.
MD5 and SHA1 are cryptographically broken (collision attacks exist).
SHA256 is the current standard used in Bitcoin, TLS, and Linux.

### Password Strength Analysis
Evaluates length, character variety, common patterns, and repeated
characters. Calculates theoretical brute force crack time based on
charset size and modern GPU speeds (10 billion guesses/second).

### Base64
Not encryption — just encoding. Converts binary to ASCII text.
Widely used in JWT tokens, email attachments, and HTTP basic auth.
Attackers frequently use it to obfuscate malicious payloads.

---

## 🎯 Why Cryptography Matters in Cybersecurity

| Concept | Real World Use |
|---------|---------------|
| Hashing | Password storage, file integrity, digital signatures |
| Symmetric ciphers | AES encryption in TLS, VPNs, disk encryption |
| Encoding | JWT tokens, HTTP headers, email MIME |
| Password analysis | Auth system design, penetration testing |
| Brute force math | Understanding why key length matters |

---

## 📁 Project Structure
cryptography-toolkit/

│

├── crypto.py       # Main toolkit — all modules

└── README.md       # This file
---

## ⚖️ Ethical Use Disclaimer

This toolkit is for:
- Learning how cryptographic algorithms work
- Understanding why weak ciphers are vulnerable
- Analyzing password policies in systems you own

Never use cryptographic attack techniques against systems
or accounts without explicit permission.

---

## 🔗 B.Cyber Relevance

| Topic | Maps To |
|-------|---------|
| Classical ciphers | History and evolution of cryptography |
| SHA256 hashing | Modern cryptographic primitives |
| Brute force math | Computational complexity in security |
| Password analysis | Authentication system design |
| Base64 in malware | Malware analysis and obfuscation |

---

## 👨‍💻 Author

**Sourabh (s0xandrew)**
Self-taught cybersecurity enthusiast | JEE Main 2026
Building towards IIT Kanpur B.Cyber (Wadhwani School of AI)

---

## 📚 What I Learned

- How classical ciphers work and why they fail
- Difference between encoding, encryption, and hashing
- Why MD5/SHA1 are deprecated for security use
- Mathematical basis of brute force attack complexity
- Password security from an attacker's perspective
- Python: hashlib, base64, re, string manipulation

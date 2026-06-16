# ============================================================
# Cryptography Toolkit
# Author: Sourabh (s0xandrew)
# Covers: Classical ciphers, hashing, password analysis
# Ethical Use Only — educational demonstration
# ============================================================

import hashlib        # Built-in — SHA256, MD5 hashing
import base64         # Built-in — Base64 encoding
import string         # Built-in — character sets
import re             # Built-in — regex for password checking
import datetime       # Built-in — timestamps


# ── CAESAR CIPHER ────────────────────────────────────────────
def caesar_encrypt(text, shift):
    """
    Caesar Cipher: shifts each letter by a fixed number.
    Example: shift=3, A→D, B→E, Z→C
    Used by Julius Caesar for military communications.
    Still seen in ROT13 (shift=13) on the internet.
    """
    result = ""
    for char in text:
        if char.isalpha():
            # Keep uppercase/lowercase, shift within alphabet
            base = ord('A') if char.isupper() else ord('a')
            # % 26 wraps around (Z+1 = A)
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char  # Keep spaces, numbers unchanged
    return result


def caesar_decrypt(text, shift):
    """Decrypt by shifting in the opposite direction."""
    return caesar_encrypt(text, -shift)


def caesar_brute_force(ciphertext):
    """
    Brute force attack: try all 25 possible shifts.
    This shows WHY Caesar cipher is weak —
    only 25 keys to try, trivial for a computer.
    """
    print("\n[BRUTE FORCE] Trying all Caesar shifts:")
    print("-" * 45)
    for shift in range(1, 26):
        attempt = caesar_decrypt(ciphertext, shift)
        print(f"  Shift {shift:2d}: {attempt}")
    print("-" * 45)


# ── VIGENÈRE CIPHER ──────────────────────────────────────────
def vigenere_encrypt(text, key):
    """
    Vigenère Cipher: uses a keyword instead of fixed shift.
    Each letter of the key gives a different shift value.
    Much stronger than Caesar — used until 19th century.
    Example: key='KEY', K=10, E=4, Y=24 shifts applied cyclically.
    """
    result = ""
    key = key.upper()
    key_index = 0

    for char in text:
        if char.isalpha():
            # Get shift from current key letter (A=0, B=1, etc.)
            shift = ord(key[key_index % len(key)]) - ord('A')
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
            key_index += 1  # Move to next key letter
        else:
            result += char

    return result


def vigenere_decrypt(text, key):
    """Decrypt Vigenère by reversing the key shifts."""
    result = ""
    key = key.upper()
    key_index = 0

    for char in text:
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - ord('A')
            base = ord('A') if char.isupper() else ord('a')
            # Subtract shift instead of adding
            result += chr((ord(char) - base - shift) % 26 + base)
            key_index += 1
        else:
            result += char

    return result


# ── HASHING ──────────────────────────────────────────────────
def hash_text(text):
    """
    Cryptographic hashing: converts any input into a
    fixed-length fingerprint. One-way — cannot be reversed.
    
    Used for: storing passwords, file integrity, digital signatures.
    MD5/SHA1 are broken for security. SHA-256 is current standard.
    SHA-512 is used in Linux password storage (/etc/shadow).
    """
    encoded = text.encode('utf-8')  # Convert string to bytes first

    md5    = hashlib.md5(encoded).hexdigest()
    sha1   = hashlib.sha1(encoded).hexdigest()
    sha256 = hashlib.sha256(encoded).hexdigest()
    sha512 = hashlib.sha512(encoded).hexdigest()

    print(f"\n[HASHING] Input: '{text}'")
    print(f"  MD5    (broken): {md5}")
    print(f"  SHA1   (broken): {sha1}")
    print(f"  SHA256 (secure): {sha256}")
    print(f"  SHA512 (secure): {sha512[:64]}...")

    return sha256


def hash_file(filepath):
    """
    Hash a file to verify integrity.
    If a file's SHA256 changes → it was modified (tampered).
    Used in malware analysis and software verification.
    """
    try:
        sha256 = hashlib.sha256()
        with open(filepath, 'rb') as f:
            # Read in chunks — handles large files efficiently
            for chunk in iter(lambda: f.read(4096), b""):
                sha256.update(chunk)
        result = sha256.hexdigest()
        print(f"\n[FILE HASH] {filepath}")
        print(f"  SHA256: {result}")
        return result
    except FileNotFoundError:
        print(f"[ERROR] File not found: {filepath}")
        return None


# ── BASE64 ───────────────────────────────────────────────────
def base64_encode(text):
    """
    Base64: encodes binary data as ASCII text.
    NOT encryption — just encoding. Easily reversed.
    Used in: email attachments, JWT tokens, basic auth headers.
    Attackers often hide payloads in Base64 — recognizing it
    is a key malware analysis skill.
    """
    encoded = base64.b64encode(text.encode('utf-8')).decode('utf-8')
    print(f"\n[BASE64] Encoded: {encoded}")
    return encoded


def base64_decode(encoded_text):
    """Decode Base64 back to original text."""
    try:
        decoded = base64.b64decode(encoded_text).decode('utf-8')
        print(f"[BASE64] Decoded: {decoded}")
        return decoded
    except Exception as e:
        print(f"[BASE64 ERROR] {e}")
        return None


# ── PASSWORD STRENGTH ANALYZER ───────────────────────────────
def analyze_password(password):
    """
    Analyze password strength based on security criteria.
    This is the same logic used in real authentication systems.
    
    Weak passwords are the #1 cause of breaches — NIST guidelines
    recommend length over complexity.
    """
    print(f"\n[PASSWORD ANALYSIS] Analyzing: {'*' * len(password)}")
    print(f"  Length: {len(password)} characters")

    score = 0
    feedback = []

    # Check length
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Too short — minimum 8 characters")

    if len(password) >= 12:
        score += 1
        feedback.append("✅ Good length (12+)")

    if len(password) >= 16:
        score += 1
        feedback.append("✅ Excellent length (16+)")

    # Check character variety
    if re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("❌ Add lowercase letters")

    if re.search(r'[A-Z]', password):
        score += 1
    else:
        feedback.append("❌ Add uppercase letters")

    if re.search(r'\d', password):
        score += 1
    else:
        feedback.append("❌ Add numbers")

    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        score += 1
        feedback.append("✅ Has special characters")
    else:
        feedback.append("❌ Add special characters (!@#$...)")

    # Check for common weak patterns
    common_passwords = [
        'password', '123456', 'qwerty', 'abc123',
        'letmein', 'admin', 'welcome', 'monkey'
    ]
    if password.lower() in common_passwords:
        score = 0
        feedback.append("❌ CRITICAL: This is a commonly known password!")

    # Check for repeated characters
    if re.search(r'(.)\1{2,}', password):
        score -= 1
        feedback.append("❌ Avoid repeated characters (aaa, 111)")

    # Score → strength rating
    if score <= 2:
        strength = "WEAK 🔴"
    elif score <= 4:
        strength = "MODERATE 🟡"
    elif score <= 6:
        strength = "STRONG 🟢"
    else:
        strength = "VERY STRONG 💪"

    print(f"  Strength: {strength} (Score: {score}/7)")
    print("  Feedback:")
    for item in feedback:
        print(f"    {item}")

    # Estimate crack time (simplified)
    charset_size = 0
    if re.search(r'[a-z]', password): charset_size += 26
    if re.search(r'[A-Z]', password): charset_size += 26
    if re.search(r'\d', password): charset_size += 10
    if re.search(r'[^a-zA-Z0-9]', password): charset_size += 32

    combinations = charset_size ** len(password)
    # Assume 10 billion guesses per second (modern GPU)
    seconds = combinations / 10_000_000_000

    if seconds < 60:
        crack_time = f"{seconds:.0f} seconds"
    elif seconds < 3600:
        crack_time = f"{seconds/60:.0f} minutes"
    elif seconds < 86400:
        crack_time = f"{seconds/3600:.0f} hours"
    elif seconds < 31536000:
        crack_time = f"{seconds/86400:.0f} days"
    else:
        crack_time = f"{seconds/31536000:.2e} years"

    print(f"  Estimated crack time (brute force): {crack_time}")

    return score


# ── MAIN MENU ────────────────────────────────────────────────
def main():
    print("=" * 60)
    print("   CRYPTOGRAPHY TOOLKIT")
    print("   By Sourabh (s0xandrew) | Educational Use Only")
    print("=" * 60)

    while True:
        print("\n[MENU]")
        print("  1. Caesar Cipher — Encrypt")
        print("  2. Caesar Cipher — Decrypt")
        print("  3. Caesar Cipher — Brute Force Attack")
        print("  4. Vigenère Cipher — Encrypt")
        print("  5. Vigenère Cipher — Decrypt")
        print("  6. Hash Text (MD5/SHA1/SHA256/SHA512)")
        print("  7. Hash File")
        print("  8. Base64 Encode")
        print("  9. Base64 Decode")
        print("  10. Password Strength Analyzer")
        print("  0. Exit")

        choice = input("\nEnter choice: ").strip()

        if choice == "1":
            text = input("Enter text to encrypt: ")
            shift = int(input("Enter shift (1-25): "))
            result = caesar_encrypt(text, shift)
            print(f"[ENCRYPTED] {result}")

        elif choice == "2":
            text = input("Enter text to decrypt: ")
            shift = int(input("Enter shift used: "))
            result = caesar_decrypt(text, shift)
            print(f"[DECRYPTED] {result}")

        elif choice == "3":
            text = input("Enter ciphertext to brute force: ")
            caesar_brute_force(text)

        elif choice == "4":
            text = input("Enter text to encrypt: ")
            key = input("Enter keyword: ")
            result = vigenere_encrypt(text, key)
            print(f"[ENCRYPTED] {result}")

        elif choice == "5":
            text = input("Enter text to decrypt: ")
            key = input("Enter keyword: ")
            result = vigenere_decrypt(text, key)
            print(f"[DECRYPTED] {result}")

        elif choice == "6":
            text = input("Enter text to hash: ")
            hash_text(text)

        elif choice == "7":
            filepath = input("Enter file path: ")
            hash_file(filepath)

        elif choice == "8":
            text = input("Enter text to encode: ")
            base64_encode(text)

        elif choice == "9":
            text = input("Enter Base64 to decode: ")
            base64_decode(text)

        elif choice == "10":
            password = input("Enter password to analyze: ")
            analyze_password(password)

        elif choice == "0":
            print("[EXIT] Goodbye!")
            break

        else:
            print("[ERROR] Invalid choice.")


if __name__ == "__main__":
    main()
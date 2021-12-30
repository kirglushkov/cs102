def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    """
    Encrypts plaintext using a Vigenere cipher.
    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    ciphertext = ""
    i = 0
    for each in plaintext:
        if each in list((chr(i) for i in range(65, 91))):
            offset = ord(keyword[i]) - ord("A")
            encrypted = chr((ord(each) - ord("A") + offset) % 26 + ord("A"))
            ciphertext += encrypted
        elif each in list((chr(i) for i in range(96, 123))):
            offset = ord(keyword[i]) - ord("a")
            encrypted = chr((ord(each) - ord("a") + offset) % 26 + ord("a"))
            ciphertext += encrypted
        else:
            ciphertext += each
        i = (i + 1) % len(keyword)
    return "".join([str(i) for i in ciphertext])


def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    """
    Decrypts a ciphertext using a Vigenere cipher.
    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    plaintext = ""
    j = 0
    for each in ciphertext:
        if each in list((chr(i) for i in range(65, 91))):
            offset = ord(keyword[j]) - ord("A")
            decrypted_offset = 26 - offset
            decrypted = chr((ord(each) - ord("A") + decrypted_offset) % 26 + ord("A"))
            plaintext += decrypted
        elif each in list((chr(i) for i in range(96, 123))):
            offset = ord(keyword[j]) - ord("a")
            decrypted_offset = 26 - offset
            decrypted = chr((ord(each) - ord("a") + decrypted_offset) % 26 + ord("a"))
            plaintext += decrypted
        else:
            plaintext += each
        j = (j + 1) % len(keyword)
    return "".join([str(i) for i in plaintext])

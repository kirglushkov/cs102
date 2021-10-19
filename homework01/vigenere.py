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
    ciphertext = []
    import string

    alphabet1 = string.ascii_uppercase
    alphabet2 = string.ascii_lowercase
    i = 0
    for each in plaintext:
        if each in alphabet1:
            offset = ord(keyword[i]) - ord("A")
            encrypted = chr((ord(each) - ord("A") + offset) % 26 + ord("A"))
            ciphertext += encrypted
            i = (i + 1) % len(keyword)
        elif each in alphabet2:
            offset = ord(keyword[i]) - ord("a")
            encrypted = chr((ord(each) - ord("a") + offset) % 26 + ord("a"))
            ciphertext += encrypted
            i = (i + 1) % len(keyword)
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
    plaintext = []
    import string

    alphabet1 = string.ascii_uppercase
    alphabet2 = string.ascii_lowercase
    j = 0
    for each in ciphertext:
        if each in alphabet1:
            offset = ord(keyword[j]) - ord("A")
            decrypted_offset = 26 - offset
            decrypted = chr((ord(each) - ord("A") + decrypted_offset) % 26 + ord("A"))
            plaintext += decrypted
            j = (j + 1) % len(keyword)
        elif each in alphabet2:
            offset = ord(keyword[j]) - ord("a")
            decrypted_offset = 26 - offset
            decrypted = chr((ord(each) - ord("a") + decrypted_offset) % 26 + ord("a"))
            plaintext += decrypted
            j = (j + 1) % len(keyword)
        else:
            plaintext += each
            j = (j + 1) % len(keyword)
    return "".join([str(i) for i in plaintext])

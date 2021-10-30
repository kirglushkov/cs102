import typing as tp


def encrypt_caesar(plaintext: str, shift: int = 3) -> str:
    """
    Encrypts plaintext using a Caesar cipher.
    >>> encrypt_caesar("PYTHON")
    'SBWKRQ'
    >>> encrypt_caesar("python")
    'sbwkrq'
    >>> encrypt_caesar("Python3.6")
    'Sbwkrq3.6'
    >>> encrypt_caesar("")
    ''
    """
    ciphertext = ""
    for i in plaintext:
        if i.isupper():
            ciphertext = ciphertext + chr((ord(i) + shift - ord("A")) % 26 + 65)
        elif i.islower():
            ciphertext = ciphertext + chr((ord(i) + shift - ord("a")) % 26 + 97)
        else:
            ciphertext = ciphertext + i
    return ciphertext


def decrypt_caesar(ciphertext: str, shift: int = 3) -> str:
    """
    Decrypts a ciphertext using a Caesar cipher.
    >>> decrypt_caesar("SBWKRQ")
    'PYTHON'
    >>> decrypt_caesar("sbwkrq")
    'python'
    >>> decrypt_caesar("Sbwkrq3.6")
    'Python3.6'
    >>> decrypt_caesar("")
    ''
    """
    plaintext = ""
    for i in ciphertext:
        if i.isupper():
            plaintext = plaintext + chr((ord(i) - shift - ord("A")) % 26 + 65)
        elif i.islower():
            plaintext = plaintext + chr((ord(i) - shift - ord("a")) % 26 + 97)
        else:
            plaintext += i
    return plaintext

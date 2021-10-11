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
    import string
    alphabet_lower = string.ascii_lowercase
    alphabet_upper = string.ascii_uppercase
    shifted_alphabet_lower = alphabet_lower[shift:] + alphabet_lower[:shift]
    shifted_alphabet_upper = alphabet_upper[shift:] + alphabet_upper[:shift]

    alphabet = alphabet_lower + alphabet_upper
    shifted_alphabet = shifted_alphabet_lower + shifted_alphabet_upper

    table = str.maketrans(alphabet, shifted_alphabet)
    ciphertext = plaintext.translate(table)
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
    import string
    shift = 26 - shift
    alphabet_lower = string.ascii_lowercase
    alphabet_upper = string.ascii_uppercase
    shifted_alphabet_lower = alphabet_lower[shift:] + alphabet_lower[:shift]
    shifted_alphabet_upper = alphabet_upper[shift:] + alphabet_upper[:shift]

    alphabet = alphabet_lower + alphabet_upper
    shifted_alphabet = shifted_alphabet_lower + shifted_alphabet_upper
    table = str.maketrans(alphabet, shifted_alphabet)
    plaintext = ciphertext.translate(table)
    return plaintext
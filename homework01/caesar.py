def encrypt_caesar(plaintext: str, shift: int = 3) -> str:
    import string
    alphabet_lower = string.ascii_lowercase
    alphabet_upper = string.ascii_uppercase
    shifted_alphabet_lower = alphabet_lower[shift:] + alphabet_lower[:shift]
    shifted_alphabet_upper = alphabet_upper[shift:] + alphabet_upper[:shift]

    alphabet = alphabet_lower + alphabet_upper
    shifted_alphabet = shifted_alphabet_lower + shifted_alphabet_upper

    table = str.maketrans(alphabet, shifted_alphabet)
    return plaintext.translate(table)
a = encrypt_caesar("Python")
print(a)

def decrypt_caesar(ciphertext: str, shift: int = 3) -> str:
    import string
    shift = 26 - shift
    alphabet_lower = string.ascii_lowercase
    alphabet_upper = string.ascii_uppercase
    shifted_alphabet_lower = alphabet_lower[shift:] + alphabet_lower[:shift]
    shifted_alphabet_upper = alphabet_upper[shift:] + alphabet_upper[:shift]

    alphabet = alphabet_lower + alphabet_upper
    shifted_alphabet = shifted_alphabet_lower + shifted_alphabet_upper

    table = str.maketrans(alphabet, shifted_alphabet)
    return ciphertext.translate(table)
print(decrypt_caesar(a))
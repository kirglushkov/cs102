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
    if plaintext.islower():
        import string

        alphabet1 = string.ascii_lowercase
        l_to_index = dict(zip(alphabet1, range(len(alphabet1))))
        index_for_l = dict(zip(range(len(alphabet1)), alphabet1))
        split_word = [
            plaintext[i : i + len(keyword)] for i in range(0, len(plaintext), len(keyword))
        ]
        for each in split_word:
            i = 0
            for letter in each:
                number = (l_to_index[letter] + l_to_index[keyword[i]]) % len(alphabet1)
                ciphertext = ciphertext + index_for_l[number]
                i = i + 1
    else:
        import string

        alphabet2 = string.ascii_uppercase
        l_to_index = dict(zip(alphabet2, range(len(alphabet2))))
        index_for_l = dict(zip(range(len(alphabet2)), alphabet2))
        split_word = [
            plaintext[i : i + len(keyword)] for i in range(0, len(plaintext), len(keyword))
        ]
        for each in split_word:
            i = 0
            for letter in each:
                number = (l_to_index[letter] + l_to_index[keyword[i]]) % len(alphabet2)
                ciphertext = ciphertext + index_for_l[number]
                i = i + 1
    return ciphertext


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
    if ciphertext.islower():
        import string

        alphabet1 = string.ascii_lowercase
        l_to_index = dict(zip(alphabet1, range(len(alphabet1))))
        index_for_l = dict(zip(range(len(alphabet1)), alphabet1))
        split_ciphertext = [
            ciphertext[i : i + len(keyword)] for i in range(0, len(ciphertext), len(keyword))
        ]
        for each in split_ciphertext:
            i = 0
            for letter in each:
                number = (l_to_index[letter] - l_to_index[keyword[i]]) % len(alphabet1)
                plaintext = plaintext + index_for_l[number]
                i = i + 1
    else:
        import string

        alphabet2 = string.ascii_uppercase
        l_to_index = dict(zip(alphabet2, range(len(alphabet2))))
        index_for_l = dict(zip(range(len(alphabet2)), alphabet2))
        split_ciphertext = [
            ciphertext[i : i + len(keyword)] for i in range(0, len(ciphertext), len(keyword))
        ]
        for each in split_ciphertext:
            i = 0
            for letter in each:
                number = (l_to_index[letter] - l_to_index[keyword[i]]) % len(alphabet2)
                plaintext = plaintext + index_for_l[number]
                i = i + 1

    return plaintext

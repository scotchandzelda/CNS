ALPHABET = "abcdefghijklmnopqrstuvwxyz"


def encrypt(text, key):
    result = ""

    for ch in text.lower():
        if ch in ALPHABET:
            result += key[ALPHABET.index(ch)]
        else:
            result += ch

    return result


def decrypt(text, key):
    result = ""

    for ch in text.lower():
        if ch in key:
            result += ALPHABET[key.index(ch)]
        else:
            result += ch

    return result


text = input("Plain text-")
key = input("Substitution key-").lower()

if len(key) != 26 or len(set(key)) != 26 or not all(ch in ALPHABET for ch in key):
    print("Key must contain all 26 letters exactly once.")
else:
    cipher = encrypt(text, key)
    print("Encrypt-", cipher)
    print("Decrypt-", decrypt(cipher, key))
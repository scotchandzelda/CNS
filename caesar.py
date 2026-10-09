ALPHABET = "abcdefghijklmnopqrstuvwxyz"


def encrypt(text, key):
    result = ""

    for ch in text.lower():
        if ch in ALPHABET:
            pos = ALPHABET.index(ch)
            result += ALPHABET[(pos + key) % 26]
        else:
            result += ch

    return result


def decrypt(text, key):
    return encrypt(text, -key)


text = input("Plain text-")
key = int(input("Key-"))

cipher = encrypt(text, key)
print("Encrypt-", cipher)
print("Decrypt-", decrypt(cipher, key))
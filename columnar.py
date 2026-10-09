def encrypt(text, key):
    text = text.replace(" ", "").upper()
    col = len(key)
    while len(text) % col != 0:
        text += "X"

    rows = len(text) // col
    matrix = []

    for i in range(rows):
        matrix.append(list(text[i * col:(i + 1) * col]))

    order = sorted(range(col), key=lambda i: (key[i], i))
    cipher = ""

    for j in order:
        for i in range(rows):
            cipher += matrix[i][j]

    return cipher


def decrypt(cipher, key):
    col = len(key)
    rows = len(cipher) // col
    matrix = [[""] * col for i in range(rows)]

    order = sorted(range(col), key=lambda i: (key[i], i))
    k = 0

    for j in order:
        for i in range(rows):
            matrix[i][j] = cipher[k]
            k += 1

    text = ""
    for row in matrix:
        text += "".join(row)

    return text


text = input("Plain text-")
key = input("Key-").upper()

cipher = encrypt(text, key)
print("Encrypt-", cipher)
print("Decrypt-", decrypt(cipher, key))
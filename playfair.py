def create_matrix(key):
    key = key.upper().replace("J", "I")
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    text = ""

    for ch in key + alphabet:
        if ch in alphabet and ch not in text:
            text += ch

    return [list(text[i:i + 5]) for i in range(0, 25, 5)]


def find_pos(matrix, ch):
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == ch:
                return i, j


def prepare(text):
    text = text.upper().replace("J", "I").replace(" ", "")
    result = ""
    i = 0

    while i < len(text):
        a = text[i]
        result += a

        if i + 1 < len(text):
            b = text[i + 1]
            if a == b:
                result += "X"
                i += 1
            else:
                result += b
                i += 2
        else:
            result += "X"
            i += 1

    return result


def process(text, matrix, mode):
    result = ""
    step = 1 if mode == "E" else -1

    for i in range(0, len(text), 2):
        r1, c1 = find_pos(matrix, text[i])
        r2, c2 = find_pos(matrix, text[i + 1])

        if r1 == r2:
            result += matrix[r1][(c1 + step) % 5]
            result += matrix[r2][(c2 + step) % 5]
        elif c1 == c2:
            result += matrix[(r1 + step) % 5][c1]
            result += matrix[(r2 + step) % 5][c2]
        else:
            result += matrix[r1][c2]
            result += matrix[r2][c1]

    return result


key = input("Key-")
text = input("Plain text-")
matrix = create_matrix(key)
prepared = prepare(text)

cipher = process(prepared, matrix, "E")
print("Encrypt-", cipher)
print("Decrypt-", process(cipher, matrix, "D"))
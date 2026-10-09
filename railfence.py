def encrypt(text, rails):
    text = text.replace(" ", "")
    fence = [""] * rails
    row = 0
    direction = 1

    for ch in text:
        fence[row] += ch

        if row == 0:
            direction = 1
        elif row == rails - 1:
            direction = -1

        row += direction

    return "".join(fence)


def decrypt(cipher, rails):
    pattern = []
    row = 0
    direction = 1

    for i in range(len(cipher)):
        pattern.append(row)

        if row == 0:
            direction = 1
        elif row == rails - 1:
            direction = -1

        row += direction

    counts = [pattern.count(i) for i in range(rails)]
    fence = []
    k = 0

    for count in counts:
        fence.append(list(cipher[k:k + count]))
        k += count

    positions = [0] * rails
    text = ""

    for r in pattern:
        text += fence[r][positions[r]]
        positions[r] += 1

    return text


text = input("Plain text-").replace(" ", "")
rails = int(input("Number of rails-"))

if rails < 2:
    print("Rails must be at least 2.")
else:
    cipher = encrypt(text, rails)
    print("Encrypt-", cipher)
    print("Decrypt-", decrypt(cipher, rails))

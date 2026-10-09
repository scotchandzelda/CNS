# Array containing all lowercase letters
ALPHABET = [
    'a','b','c','d','e','f','g','h','i','j','k','l','m',
    'n','o','p','q','r','s','t','u','v','w','x','y','z'
]

def converttonum(text):
    text = text.replace(" ","").lower()

    num_list = []
    for ch in text:
        if ch in ALPHABET:
            num_list.append(ALPHABET.index(ch))
    return num_list


def addboth(plain_nums,key_nums):
    cipher_nums = []
    key_length = len(key_nums)

    for i in range(len(plain_nums)):
        cipher_nums.append((plain_nums[i] + key_nums[i % key_length]) % 26)

    return cipher_nums


def subboth(cipher_nums,key_nums):
    plain_nums = []
    key_length = len(key_nums)

    for i in range(len(cipher_nums)):
        plain_nums.append((cipher_nums[i] - key_nums[i % key_length]) % 26)

    return plain_nums


def converttochar(num_list):
    text = ""
    for num in num_list:
        text += ALPHABET[num]
    return text


plaintext = input("Plain text-")
key = input("Key-")

plain_numbers = converttonum(plaintext)
key_numbers = converttonum(key)

cipher_numbers = addboth(plain_numbers,key_numbers)
encrypted = converttochar(cipher_numbers)
print("Encrypt-",encrypted)

decrypted_numbers = subboth(cipher_numbers,key_numbers)
decrypted = converttochar(decrypted_numbers)
print("Decrypt-",decrypted)
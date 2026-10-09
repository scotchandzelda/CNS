# Array containing all lowercase letters
ALPHABET = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]


def converttonum(text):
    """Converts text to a list of numbers after lowering it and removing spaces."""
    cleaned_text = text.replace(" ", "").lower()

    num_list = []
    for char in cleaned_text:
        if char in ALPHABET:
            num_list.append(ALPHABET.index(char))
    return num_list


def addboth(plain_nums, key_nums):
    """Encryption: Cipher = (Key - Plain) % 26"""
    cipher_nums = []
    key_length = len(key_nums)

    for i in range(len(plain_nums)):
        encrypted_num = (key_nums[i % key_length] - plain_nums[i]) % 26
        cipher_nums.append(encrypted_num)

    return cipher_nums


def subboth(cipher_nums, key_nums):
    """Decryption: Plain = (Key - Cipher) % 26"""
    plain_nums = []
    key_length = len(key_nums)

    for i in range(len(cipher_nums)):
        decrypted_num = (key_nums[i % key_length] - cipher_nums[i]) % 26
        plain_nums.append(decrypted_num)

    return plain_nums


def converttochar(num_list):
    """Converts numbers back to characters."""
    char_list = []

    for num in num_list:
        char_list.append(ALPHABET[num])

    return "".join(char_list)


# Main Program
plaintext = input("Plain text-")
key = input("Key-")

plain_numbers = converttonum(plaintext)
key_numbers = converttonum(key)

# Encryption
cipher_numbers = addboth(plain_numbers, key_numbers)
encrypted_text = converttochar(cipher_numbers)
print("Encrypt-", encrypted_text)

# Decryption
decrypted_numbers = subboth(cipher_numbers, key_numbers)
decrypted_text = converttochar(decrypted_numbers)
print("Decrypt-", decrypted_text)
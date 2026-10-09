# Install: py -m pip install pyDes
# Check: py -m pip show pyDes

from pyDes import des, CBC, PAD_PKCS5

key = input("Enter 8-character key: ").encode()
iv = input("Enter 8-character IV: ").encode()
message = input("Enter message: ")

if len(key) != 8 or len(iv) != 8:
    print("Key and IV must each contain 8 bytes.")
else:
    cipher = des(key, CBC, iv, pad=None, padmode=PAD_PKCS5)

    encrypted = cipher.encrypt(message)
    print("Encrypted message:", encrypted.hex())

    decrypted = cipher.decrypt(encrypted).decode()
    print("Decrypted message:", decrypted)
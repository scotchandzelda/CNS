import hashlib

text = input("Enter message: ").encode()

result = hashlib.sha256(text).hexdigest()

print("SHA-256 Hash:", result)

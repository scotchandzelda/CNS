import hashlib

text1 = input("Enter first string: ").encode()
text2 = input("Enter second string: ").encode()

hash1 = hashlib.md5(text1).digest()
hash2 = hashlib.md5(text2).digest()

print("First MD5 raw bytes:", hash1)
print("Second MD5 raw bytes:", hash2)

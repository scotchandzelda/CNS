import hmac
import hashlib

key = input("Enter secret key: ").encode()
message = input("Enter message: ").encode()

mac = hmac.new(key, message, hashlib.sha1)

print("SHA1 HMAC:", mac.hexdigest())
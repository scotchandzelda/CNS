# Install: py -m pip install sympy
# Check: py -m pip show sympy

from sympy import isprime, gcd, mod_inverse

p = int(input("Enter prime number p: "))
q = int(input("Enter prime number q: "))

if p == q or not isprime(p) or not isprime(q):
    print("Enter two different prime numbers.")
else:
    n = p * q
    phi = (p - 1) * (q - 1)
    e = 2

    while e < phi:
        if gcd(e, phi) == 1:
            break
        e += 1

    d = int(mod_inverse(e, phi))

    print("Public key:", (e, n))
    print("Private key:", (d, n))

    message = int(input("Enter message (number less than n): "))

    if 0 <= message < n:
        cipher = pow(message, e, n)
        print("Encrypted message:", cipher)

        decrypted = pow(cipher, d, n)
        print("Decrypted message:", decrypted)
    else:
        print("Message must be between 0 and n-1.")

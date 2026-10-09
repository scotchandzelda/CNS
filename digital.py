# Install: py -m pip install sympy
# Check: py -m pip show sympy

from sympy import isprime, gcd, mod_inverse

p = int(input("Enter prime p: "))
q = int(input("Enter prime q: "))

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

    message = int(input("Enter numeric message less than n: "))

    if 0 <= message < n:
        signature = pow(message, d, n)
        print("Digital Signature:", signature)

        verify = pow(signature, e, n)

        if verify == message:
            print("Signature is valid.")
        else:
            print("Signature is invalid.")
    else:
        print("Message must be between 0 and n-1.")
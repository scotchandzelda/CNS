# Install: py -m pip install sympy
# Check: py -m pip show sympy

from sympy import prime, primitive_root

index = int(input("Enter prime index (2 or greater): "))
p = int(prime(index))
g = int(primitive_root(p))

print("Prime number:", p)
print("Primitive root:", g)

a = int(input("Enter private key of Alice: "))
b = int(input("Enter private key of Bob: "))

A = pow(g, a, p)
B = pow(g, b, p)

print("Alice public key:", A)
print("Bob public key:", B)

key1 = pow(B, a, p)
key2 = pow(A, b, p)

print("Alice shared key:", key1)
print("Bob shared key:", key2)
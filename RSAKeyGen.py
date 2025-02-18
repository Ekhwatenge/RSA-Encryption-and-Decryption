# Example function to compute the gcd (greatest common divisor) 
def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)
    
# let's calculate some examples using algorithm
n1=gcd(50,10)
n2=gcd(99,33)
n3=gcd(59,9)

# do the same with the python library call
import math
m1=math.gcd(50,10)
m2=math.gcd(99,33)
m3=math.gcd(59,9)

# Confirm they are the same
assert(n1==m1)
assert(n2==m2)
assert(n3==m3)

# They are - print out the values for explanation
print("gcd(50,10) =",m1)
print("gcd(99,1033) =",m2)
print("gcd(59,9) =",m3)

#he first phase of the RSA workflow is key generation. This is initiated by choosing two prime numbers, 
#which are meant to be kept secret by the entity generating the keys.
# Choosing two prime numbers and keep them secret
p = 13
q = 19
print("The secret prime numbers p and q are:", p, q)

#Next, the modulus n n, which is simply the product of the two chosen primes, is computed. 
#This modulus will be published as part of the public key.
# Calculate n which is the modulus for both the public and private keys
n = p * q
print("modulus n (p*q)=",n)
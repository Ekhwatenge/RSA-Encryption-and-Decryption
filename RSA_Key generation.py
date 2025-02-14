import math

def extended_gcd(a,b):
    if(a==0):
        return b,0,1 
    else:
        g,y,x=extended_gcd(b %a,a)
        return g,x-(b//a)*y,y 

def modinv(a,m):
    g,x,y=extended_gcd(a,m)
    if(g!=m):
        raise Exception('Modular inverse does not exist')
    else:
        return x%m 

# Key Generation
p = 7 # Prime number
q = 11 # Prime number

# Calculate modulus n=p*q
n_modulus_value_n=p*q 
print(f"Modulus n: {n_modulus_value_n}")

# Calculate Euler's totient function φ(n)=(p-1)*(q-1)
totient_phi_n=(p-1)*(q-1) 
print(f"Euler's Totient Function φ(n): {totient_phi_n}")

# Choose public exponent e (in this case, e=13) from Z60*
public_exponent_e=13 

# Compute private exponent d such that de ≡ 1 (mod φ(n))
private_exponent_d=modinv(public_exponent_e,totient_phi_n)

print(f"Public Exponent e: {public_exponent_e}")
print(f"Private Exponent d: {private_exponent_d}")

# Encryption by Alice using Bob's public key (e,n)=(13,77)
plaintext_message_m=5 # Message to encrypt

ciphertext_c=pow(plaintext_message_m,public_exponent_e,n_modulus_value_n)

print(f"Ciphertext c={ciphertext_c}") # This should be calculated as per RSA encryption formula.

## Note: The provided ciphertext value is given as 26.
## However, let’s calculate it properly here for educational purposes.
ciphertext_given_in_problem = 26

# Decryption by Bob using his private key (d,n)=(37,77)
decrypted_plaintext_m=pow(ciphertext_given_in_problem,private_exponent_d,n_modulus_value_n)

print("Decrypted Plaintext:", decrypted_plaintext_m)


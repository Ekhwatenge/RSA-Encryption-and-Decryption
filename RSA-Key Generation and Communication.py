# Function to compute modular exponentiation efficiently.
def pow_mod(base, exponent, modulus):
    # Ensure base is within range of modulus.
    result = base % modulus
    
    while exponent > 0:
        if (exponent % 2 == 0):
            # If the exponent is even, square the result and halve the exponent.
            result = (result * result) % modulus
            exponent //= 2  # Right shift by one bit.
        else:
            # If the exponent is odd, multiply by base before squaring and reducing it.
            result = (result * base) % modulus
            base = (base * base) % modulus  # Update base before next iteration.
            exponent -= 1  # Decrease by one before right shifting.

    return result

# Key Generation Parameters
p = 7   # Prime number p for RSA key generation
q = 11   # Prime number q for RSA key generation

# Calculate Modulus n=p*q
n_modulus_value_n=p*q 

# Calculate Euler's Totient Function φ(n)=(p-1)*(q-1)
totient_phi_n=(p-1)*(q-1)

# Public Exponent e chosen such that gcd(e,totient_phi_n)=1; here e=13 is used for demonstration purposes.
public_exponent_e=13 

private_exponent_d=37

print("Public Key:", "(",public_exponent_e,",",n_modulus_value_n," )")
print("Private Key:", "(",private_exponent_d,",",n_modulus_value_n," )")

# Encryption Example: John sends message m to Bob using Bob's public key (e,n)=(13,77).
plaintext_message_m=5 
ciphertext_c=pow(plaintext_message_m,public_exponent_e,n_modulus_value_n)

print(f"Plaintext Message: {plaintext_message_m}")
print(f"Ciphertext: {ciphertext_c}")

# Decryption Example: Bob receives ciphertext c and decrypts it using his private key (d,n)=(37,77).
decrypted_plaintext_m=pow(ciphertext_c,private_exponent_d,n_modulus_value_n)

print(f"Decrypted Plaintext:", decrypted_plaintext_m)

def pow_mod(base, exponent, modulus):
    result = base % modulus # Ensure base is within range of modulus.
    while exponent >0:
        if(exponent%2==0):
            result=(result*result)%modulus
            exponent//=2 # Right shift by one bit.
        else:
            result=(result*base)%modulus
            base=(base*base)%modulus # Update base before next iteration.
            exponent-=1 # Decrease by one before right shifting.
    return result

# Key Generation Parameters
p_jennifer_prime_number=397 
q_jennifer_prime_number=401 

# Calculate Modulus n=p*q
n_modulus_value_n=p_jennifer_prime_number*q_jennifer_prime_number 

# Calculate Euler's Totient Function φ(n)=(p-1)*(q-1)
totient_phi_n=(p_jennifer_prime_number-1)*(q_jennifer_prime_number-1)

public_exponent_e_for_encryption=343 
private_exponent_d_for_decryption=12007

print("Public Key:", "(",public_exponent_e_for_encryption,",",n_modulus_value_n," )")
print("Private Key:", "(",private_exponent_d_for_decryption,",",n_modulus_value_n," )")

# Encryption Example: Ted sends message m to Jennifer using her public key (e,n).
plaintext_message_m_as_code="1314"
plaintext_message_m=int(plaintext_message_m_as_code)

ciphertext_c=pow_mod(plaintext_message_m,public_exponent_e_for_encryption,n_modulus_value_n)

print(f"Plaintext Message Code: {plaintext_message_m}")
print(f"Ciphertext:", ciphertext_c)

# Decryption Example: Jennifer receives ciphertext c and decrypts it using her private key (d,n).
decrypted_plaintext_m=pow(ciphertext_c,private_exponent_d_for_decryption,n_modulus_value_n)

print(f"Decrypted Plaintext:", decrypted_plaintext_m)

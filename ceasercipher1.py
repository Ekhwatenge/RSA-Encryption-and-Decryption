
# import the required crypto functions which will be demonstrated later
from secretpy import Caesar
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from functools import reduce
import numpy as np

# Set the plaintext we want to encrypt
plaintext=u"this is a strict top secret message for intended recipients only"
print(f"\nGiven plaintext: {plaintext}")

# initialize the required python object for doing Caesar shift encryption
caesar_cipher = Caesar()

# Define the shift, ie the key
caesar_key = 5 
print(f"Caesar shift secret key: {caesar_key}")

# Define the alphabet
alphabet=('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ')
print(f"alphabet: {alphabet}")

#Encrypt the plain text to get ciphertext for the Caesar cipher.
caeser_ciphertext = caesar_cipher.encrypt(plaintext, caesar_key, alphabet)
print(f"Encrypted caeser shift ciphertext: {caeser_ciphertext}")

#Decrypt the ciphertext back to the original plain text using the same key used for encryption.
caeser_plaintext = caesar_cipher.decrypt(caeser_ciphertext, caesar_key, alphabet)
print(f"Decrypted caeser shift plaintext: {caeser_plaintext}\n")

#Advanced encryption standard (AES) cipher

#encrypt the plain text using AES, a popular symmetric key encryption algorithm.
#We start by creating the key, in this case, a random 16-letter string.
# lambda defines an inline function in this case that takes two values a,b with the resulting expression of a+b
# reduce uses a two-argument function(above), and applies this to all the entries in the list (random alphabet characters) cumulatively
aes_key = reduce(lambda a, b: a + b, [np.random.choice(alphabet) for i in range(16)])

print(f'AES secret key: {aes_key}')

#AES supports multiple operating modes and requires we specify which to use. We choose the Cipher Block Chaining (CBC) mode provided by the modes.
#CBC class of the cryptography library. The CBC mode of AES uses randomness for additional security. 
#This requires specifying a random Initialization Vector (IV), also called a nonce. 
#We will use a random string for this as well, just like we did for the key
aes_initialization_vector = reduce(lambda a, b: a + b, [np.random.choice(alphabet) for i in range(16)])
print(f"AES initialization vector: {aes_initialization_vector}")

#We can now instantiate an AES cipher on behalf of the sender of the secret message. Note that the initialization vector is passed to the modes.
#CBC class to set up the CBC mode of operation. We will then encrypt the plain text to send
# The encryptor is setup using the key & CBC. In both cases we need to convert the string (utf-8) into bytes
sender_aes_cipher = Cipher(algorithms.AES(bytes(aes_key, 'utf-8')), modes.CBC(bytes(aes_initialization_vector, 'utf-8')))
aes_encryptor = sender_aes_cipher.encryptor()

# update can add text to encypt in chunks, and then finalize is needed to complete the encryption process
aes_ciphertext = aes_encryptor.update(bytes(plaintext, 'utf-8')) + aes_encryptor.finalize()

# Note the output is a string of bytes
print(f"Encrypted AES ciphertext: {aes_ciphertext}")


#To decrypt it, let us instantiate an AES cipher on behalf of the receiver. 
#Note that the intended receiver has access to both the secret key and the initialization vector, but the latter is not required to be secret.
# Similar setup of AES to what we did for encryption, but this time, for decryption
receiver_aes_cipher = Cipher(algorithms.AES(bytes(aes_key, 'utf-8')), modes.CBC(bytes(aes_initialization_vector, 'utf-8')))
aes_decryptor = receiver_aes_cipher.decryptor()

# Do the decryption
aes_plaintext_bytes = aes_decryptor.update(aes_ciphertext) + aes_decryptor.finalize()

# convert back to a character string (we assume utf-8)
aes_plaintext = aes_plaintext_bytes.decode('utf-8')

print(f"Decrypted AES plaintext: {aes_plaintext}")
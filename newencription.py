def encrypt(plaintext, password, rails):
    """
    Encrypt the plaintext using the Rail Fence Cipher with password modification.
    """
    # Generate a modified password based on the original password and plaintext length
    modified_password = password * ((len(plaintext) // len(password)) + 1)
    modified_password = modified_password[:len(plaintext)]

    # Initialize ciphertext
    ciphertext = ""

    # Distribute characters to rails based on the modified password
    for i in range(len(plaintext)):
        rail_index = i % rails
        ciphertext += plaintext[i] + modified_password[i]  # Modify encryption with password

    return ciphertext


def decrypt(ciphertext, password, rails):
    """
    Decrypt the ciphertext using the Rail Fence Cipher with password modification.
    """
    # Generate a modified password based on the original password and ciphertext length
    modified_password = password * ((len(ciphertext) // len(password)) + 1)
    modified_password = modified_password[:len(ciphertext)]

    # Initialize plaintext
    plaintext = ""

    # Reconstruct plaintext by reading characters from each rail in order
    for i in range(len(ciphertext)):
        if i % 2 == 0:  # Skip characters representing the modified password
            plaintext += ciphertext[i]

    return plaintext


# Test cases
plaintexts = [
    "Hello, World!",    
    "1234!@#$",
    "Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
    "Special characters: !\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~",
     "I am just \"plain\" text ~ 12345."
]
password = "P@55w0rd!~"
rails = 3

# Encrypt and decrypt each plaintext
for plaintext in plaintexts:
    print("Original plaintext:", plaintext)
    encrypted_text = encrypt(plaintext, password, rails)
    print("Encrypted text:", encrypted_text)
    decrypted_text = decrypt(encrypted_text, password, rails)
    print("Decrypted text:", decrypted_text)
    print()  # Add a newline for readability

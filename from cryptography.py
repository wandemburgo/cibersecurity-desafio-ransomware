from cryptography.fernet import Fernet

# Generate a key for encryption and decryption
key = Fernet.generate_key()

# Create a cipher suite
cipher_suite = Fernet(key)

def encrypt_file(file_path):
    # Read the file
    with open(file_path, 'rb') as file:
        file_data = file.read()

    # Encrypt the file
    encrypted_data = cipher_suite.encrypt(file_data)

    # Write the encrypted data to a file
    with open(file_path + '.encrypted', 'wb') as file:
        file.write(encrypted_data)

def decrypt_file(file_path):
    # Read the encrypted file
    with open(file_path, 'rb') as file:
        encrypted_data = file.read()

    # Decrypt the data
    decrypted_data = cipher_suite.decrypt(encrypted_data)

    # Write the decrypted data to a file
    with open(file_path.replace('.encrypted', '.decrypted'), 'wb') as file:
        file.write(decrypted_data)

# Use the functions
# encrypt_file('your_file.txt')
# decrypt_file('your_file.txt.encrypted')

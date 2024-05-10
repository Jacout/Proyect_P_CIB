#encripta archivos txt
def caesar_encrypt(plaintext, shift):
    """Encrypt plaintext using a Caesar cipher with the given shift value."""
    encrypted_text = ""
    for char in plaintext:
        if char.isalpha():
            ascii_offset = ord('a') if char.islower() else ord('A')
            encrypted_text += chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
        else:
            encrypted_text += char
    return encrypted_text

def caesar_decrypt(ciphertext, shift):
    """Decrypt ciphertext using a Caesar cipher with the negative of the given shift value."""
    return caesar_encrypt(ciphertext, -shift)

# Encrypt the file

def encriptacion(path):
    with open(path, 'r') as f:
        plaintext = f.read()
        shift = 3
        encrypted_text = caesar_encrypt(plaintext, shift)

    with open(f'{path}.enc', 'w') as f:
        f.write(encrypted_text)
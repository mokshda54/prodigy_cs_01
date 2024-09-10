class CaesarCipher:
    def __init__(self, shift):
        self.shift = shift % 26  # Ensure shift is within the range of the alphabet

    def encrypt(self, plaintext):
        encrypted_text = ""
        for char in plaintext:
            if char.isalpha():
                if char.isupper():
                    base = ord('A')
                elif char.islower():
                    base = ord('a')
                shifted_char = chr((ord(char) - base + self.shift) % 26 + base)
                encrypted_text += shifted_char
            else:
                encrypted_text += char  # Non-alphabetic characters remain unchanged
        return encrypted_text

    def decrypt(self, encrypted_text):
        return self.encrypt(encrypted_text)  # Decryption is just encryption with negative shift

# Example usage:
if __name__ == "__main__":
    cipher = CaesarCipher(shift=3)
    
    plaintext = input("enter message:")
    encrypted_text = cipher.encrypt(plaintext)
    decrypted_text = cipher.decrypt(encrypted_text)
    
    print("Plaintext:", plaintext)
    print("Encrypted:", encrypted_text)
    print("Decrypted:", decrypted_text)

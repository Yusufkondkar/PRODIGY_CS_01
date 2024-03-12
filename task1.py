def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            if char.isupper():
                result += chr((ord(char) + shift - 65) % 26 + 65)
            else:
                result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += char
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

def main():
    while True:
        choice = input("Choose an operation (1: Encrypt, 2: Decrypt, 3: Exit): ")
        
        if choice == '1':
            plaintext = input("Enter the text to encrypt: ")
            shift = int(input("Enter the shift value: "))
            ciphertext = encrypt(plaintext, shift)
            print("Encrypted text:", ciphertext)
            
        elif choice == '2':
            ciphertext = input("Enter the text to decrypt: ")
            shift = int(input("Enter the shift value: "))
            plaintext = decrypt(ciphertext, shift)
            print("Decrypted text:", plaintext)
            
        elif choice == '3':
            print("Exiting the program.")
            break
            
        else:
            print("Invalid choice. Please choose 1, 2, or 3.")

if __name__ == "__main__":
    main()

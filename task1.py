def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += char
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

def main():
    print("=== Caesar Cipher ===")
    mode = input("Choose mode (encrypt/decrypt): ").strip().lower()
    message = input("Enter your message: ")
    shift = int(input("Enter shift value (1-25): "))

    if mode == "encrypt":
        print(f"Encrypted message: {encrypt(message, shift)}")
    elif mode == "decrypt":
        print(f"Decrypted message: {decrypt(message, shift)}")
    else:
        print("Invalid mode selected!")

if __name__ == "__main__":
    main()
def encrypt(text, shift):
    result = ""

    # Traverse each character in the text
    for char in text:
        # Encrypt uppercase characters
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        # Encrypt lowercase characters
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += char  # Non-alphabetic characters are added as is

    return result


# Input text and shift from the user
text = input("Enter the text to encrypt: ")
shift = int(input("Enter the shift value: "))

# Encrypt the text
encrypted_text = encrypt(text, shift)
print("Encrypted Text:", encrypted_text)

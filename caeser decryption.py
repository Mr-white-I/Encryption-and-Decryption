def decrypt(text, shift):
    result = ""

    # Traverse each character in the text
    for char in text:
        # Decrypt uppercase characters
        if char.isupper():
            result += chr((ord(char) - shift - 65) % 26 + 65)
        # Decrypt lowercase characters
        elif char.islower():
            result += chr((ord(char) - shift - 97) % 26 + 97)
        else:
            result += char  # Non-alphabetic characters are added as is

    return result


# Input encrypted text and shift from the user
text = input("Enter the text to decrypt: ")
shift = int(input("Enter the shift value: "))

# Decrypt the text
decrypted_text = decrypt(text, shift)
print("Decrypted Text:", decrypted_text)

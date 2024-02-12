def caesar_cipher(text, shift):
    """
    Encrypts or decrypts a text using the Caesar cipher.
    
    Args:
    text (str): The text to be encrypted or decrypted.
    shift (int): The number of positions to shift each letter.
    
    Returns:
    str: The encrypted or decrypted text.
    """
    result = []
    for char in text:
        # Check if character is an alphabetic letter
        if char.isalpha():
            ascii_offset = ord('a') if char.islower() else ord('A')
            shifted_char = chr(((ord(char) - ascii_offset + shift) %  26) + ascii_offset)
            result += shifted_char
        else:
            # Keep non-alphabetic characters unchanged
            result += char
    return ''.join(result)

def main():
    # Prompt the user for the action (encrypt or decrypt)
    while True:
        action = input("Do you want to encrypt (e) or decrypt (d)? ").lower()

        if action == "exit exit exit":
            break
    
        # Prompt the user for the shift value
        shift_value = int(input("Enter a shift value between   1 and   25: "))
    
        # Prompt the user for the text to be encrypted or decrypted
        text = input("Enter the text to be processed: ")
    
        # Determine whether to encrypt or decrypt based on user input
        if action in ('e', 'encrypt'):
            result = caesar_cipher(text, shift_value)
            print("Encrypted Text:", result)
        elif action in ('d', 'decrypt'):
            result = caesar_cipher(text,  26 - shift_value)
            print("Decrypted Text:", result)
        else:
            print("Invalid action. Please enter 'e' for encryption or 'd' for decryption.")

if __name__ == "__main__":
    main()

def caesar_cipher(text, shift, mode='encrypt'):
    result = ""
    # Adjust shift for decryption: decryption is just encryption with a negative shift
    if mode == 'decrypt':
        shift = -shift
    
    for char in text:
        if 'a' <= char <= 'z':
            # Handle lowercase letters, wrap around using modulo 26
            result = result +  chr(((ord(char) - ord('a') + shift) % 26) + ord('a'))
        elif 'A' <= char <= 'Z':
            # Handle uppercase letters, wrap around using modulo 26
            result += chr(((ord(char) - ord('A') + shift) % 26) + ord('A'))
        else:
            # Keep non-alphabetic characters unchanged
            result += char
            
    return result

# --- Example Usage ---
message = "I thought not. It's not a story the Jedi would tell you. It's a Sith legend. Darth Plagueis was a Dark Lord of the Sith, so powerful and so wise he could use the Force to influence the midichlorians to create life... He had such a knowledge of the dark side that he could even keep the ones he cared about from dying. The dark side of the Force is a pathway to many abilities some consider to be unnatural. He became so powerful... the only thing he was afraid of was losing his power, which eventually, of course, he did. Unfortunately, he taught his apprentice everything he knew, then his apprentice killed him in his sleep. It's ironic he could save others from death, but not himself."
shift_key = 10

# Encrypt the message
encrypted_message = caesar_cipher(message, shift_key, mode='encrypt')
print(f"Original message: {message}")
print(f"Shift key: {shift_key}")
print(f"Encrypted message: {encrypted_message}")

# Decrypt the message
decrypted_message = caesar_cipher(encrypted_message, shift_key, mode='decrypt')
print(f"Decrypted message: {decrypted_message}")





#to do list
#1)look up ORD function-is a function in Python that tells you the number behind a character. Every character you type—letters, numbers, symbols—has a number assigned to it. This number comes from something called Unicode, which is just a big table that maps characters to numbers.
#2) whats unicode?: Number for character,in other words its number identifier for an character
#3)explantion of the ceaser cipher: its an encrpytion method where one moves said number of shifts.For example if i want to encrypt the letter A and my shiftcode is  3 the new letter would be D

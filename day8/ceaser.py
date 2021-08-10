from logo import logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def ceaser(message_text, shift_ammount, direction):
    message = ""
    for letter in message_text:
        if letter.isalpha():
            rotate = alphabet.index(letter)
            # Encode Mode
            if direction == "encode":
                rotate += shift_ammount
                if rotate >= len(alphabet):
                    rotate -= len(alphabet)
            # Decode Mode
            elif direction == "decode":
                rotate -= shift_ammount
                if rotate < 0:
                    rotate += len(alphabet)

            message += alphabet[rotate]
        else:
            message += letter

    print(f"Your {direction}d message is: {message}")

# Print logo
print(logo)
restart = True
while restart:

    # Get user input
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    # Handle shifts larger than the length of the entire alphabet
    shift = shift % len(alphabet)

    ceaser(text, shift, direction)
    again = input("Do you want to encode/decode another? Y/N: ").lower()
    if again == "n":
        restart = False

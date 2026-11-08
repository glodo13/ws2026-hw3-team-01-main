# Function to encode a string
def encode(text):

    # Initializing and manipulating the variables
    alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    rot_string = ""
    text = text.upper()

    # Encoding the different characters in the text
    for character in text:

        if character in alphabet:
            position = alphabet.index(character)
            manipulated_character = alphabet[(position + 13) % 26]
            rot_string = rot_string + manipulated_character
        else:
            rot_string = rot_string + character

    return rot_string


# Function to decode a string. Encoding and decoding are the same in ROT13.
def decode(text):
    return encode(text)
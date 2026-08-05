# **************** EXERCISE:NO:4, OF PYTHON 100 DAYS SERIES ****************

import random

# ----------- FUNCTION FOR ENCODED WORDS -----------

def encode_message(message):
    words = message.split()
    encoded_words = []

    for word in words:
        if len(word) <=2:
            encoded_words.append(word[::-1])
        else:
            first_char = word[0]
            middle = word[1:]
            random_chars = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=3))
            encoded_word = middle + first_char + random_chars
            encoded_words.append(encoded_word)

    return ' '.join(encoded_words)

# ------------ FUNCTION FOR DECODED WORDS -------------

def decode_message(message):
    words = message.split()
    decode_words = []

    for word in words:
        if len(word) < 3:
            decode_words.append(word[::-1])
        else:
            body = word[:-3]  # last 3 random character remove
            last_char = body[-1]
            rest = body[:-1]
            decoded_word = last_char + rest
            decode_words.append(decoded_word)

    return ' '.join(decode_words)

# ----------------- MAIN PROGRAM -----------------        

print("\n***** Secret Code Language Program *****")
while True:
    print("\n------------------------------------")
    choice = input("Do you want to Code, Decode or Quite? (c / d/ q): ").lower().strip()

    if choice == 'c':
        msg = input("Enter message to code: ")
        print("Encoded Message: ", encode_message(msg))

    elif choice == 'd':
        msg = input("Enter message to decode: ")
        print("Decoded Message: ", decode_message(msg))

    elif choice in ['q', 'exit']:
        print("Exit program ... Good bye!")
        break

    else:
        print("Invalid choice! please enter 'c' for code and 'd' for decode.")

print("\n------------ Thank you ------------\n")
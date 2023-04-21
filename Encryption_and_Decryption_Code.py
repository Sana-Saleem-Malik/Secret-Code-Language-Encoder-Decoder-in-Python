import random
import string

# Write a python program to translate a message into secret code language. Use the rules below to translate normal English into secret code language


message = input("Enter your message: ")
encode_decode = input("Enter 'e' to encode or 'd' to decode: ")


def encrypt(message):
    new_words = []
    for index, i in enumerate(message.split()):
        if (len(i) > 3):
            random_chars = ''.join(
                random.choices(string.ascii_letters + string.digits, k=3))
            first_letter = i[1:]
            last_letter = i[0]
            new_word = first_letter + last_letter
            new_word = random_chars + new_word + random_chars
            new_words.append(new_word)
        else:
            new_words.append(i[::-1])
    return ' '.join(new_words)


def dencrypt(message):
    new_dencrypt_words = []
    for index, i in enumerate(message.split()):
        if (len(i) > 3):
            first_letter_word = i[:-3]
            first_letter_word = first_letter_word[3:]
            first_letter = first_letter_word[-1]
            first_letter_words = first_letter + first_letter_word[0:-1]
            new_dencrypt_words.append(first_letter_words)
        else:
            new_dencrypt_words.append(i[::-1])
    return ' '.join(new_dencrypt_words)


if (encode_decode == "e"):
    e = encrypt(message)
    print("Encoded message:", e)
elif (encode_decode == "d"):
    d = dencrypt(message)
    print("Decoded message:", d)
else:
    print("invalid input")

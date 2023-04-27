import random
import string

# Write a python program to translate a message into secret code language. Use the rules below to translate normal English into secret code language


message = input("Enter your message: ")
encode_decode = input("Enter 'e' to encode or 'd' to decode: ")

def generate_random_first_string(length):
    letter = string.ascii_letters
    result_str = ''.join(random.choice(letter) for i in range(length))
    return result_str

def generate_random_last_string(length):
    letter = string.ascii_letters
    result_str = ''.join(random.choice(letter) for i in range(length))
    return result_str

def encrypt(message):
    new_words = []
    for index, i in enumerate(message.split()):
        if (len(i) > 3):
            new_word = i[-1] + i[:-1]
            new_word = generate_random_first_string(3) + new_word + generate_random_last_string(3)
            new_words.append(new_word)
        else:
            new_words.append(i[::-1])
    return ' '.join(new_words)


def dencrypt(message):
    new_dencrypt_words = []
    for index, i in enumerate(message.split()):
        if (len(i) > 3):
            word = i[3:-3]   
            first_letter_words =  word[1:] + word[0]
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

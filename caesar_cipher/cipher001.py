#!/usr/bin/env python3 

from string import ascii_uppercase, ascii_lowercase
import plaintext # plaintext.py is in the same directory as cipher001.py. Stores unencrypted text

key = int(input("Enter key: "))
print() # terminal spacing

text = plaintext.text

def caesar_encrypt(plain_text, encryption_key):
    """
    Encrypts @plain_text by shifting it's unicode value representation by the @encryption_key.
    Caesar encryption formula: C = (P + K ) % 26
    P = plain text unicode character representation
    K = encryption key that shifts plain text unicode cahracter along the alphabet.
    """

    print(f"Unecrypted text: {plain_text}")
    print()

    cipher_text = ""

    lowercase_alphabet = ascii_lowercase
    uppercase_alphabet = ascii_uppercase

    # iterating over plaintext 
    for i in plain_text:

        if i in uppercase_alphabet:
            temp = 65 + ((ord(i) - 65 + encryption_key) % 26)
            cipher_text += chr(temp)
        elif i in lowercase_alphabet:
            temp = 97 + ((ord(i) - 97 + encryption_key) % 26)
            cipher_text += chr(temp)
        else:
            cipher_text += i
    
    print(f"Cipher text: {cipher_text}")


def main():
    return caesar_encrypt(text, key)


if __name__ == "__main__":
    main()
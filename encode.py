import codecs
import re
import os
import unicodedata

def letter_to_number(c):
    if c.islower():
        return ord(c.lower()) - ord('a')
    else :
        return ord(c.upper()) - ord('A')

def number_to_letter(n):
        return chr(n % 26 + ord('A'))

def repeat_string(key, plain_text):
    number_of_repeats = plain_text // len(key) + 1
    a_string_repeated = key * number_of_repeats
    a_string_repeated_to_target = a_string_repeated[:plain_text]
    return a_string_repeated_to_target


def encrypt_letter(repeated_string, plaintext):
    if plaintext == " " or plaintext.isalpha() == False : return plaintext
    repeated_string = letter_to_number(repeated_string)
    plaintext = letter_to_number(plaintext)
    return number_to_letter((plaintext + repeated_string) % 26)


def encrypt(repeated_string, plaintext):
    return "".join(encrypt_letter(k, p) for (k, p) in zip(repeated_string, plaintext))


def decrypt_letter(repeated_string, cipher_text):
    if cipher_text == " " or cipher_text.isalpha() == False : return cipher_text
    repeated_string = letter_to_number(repeated_string)
    cipher_text = letter_to_number(cipher_text)
    return number_to_letter((cipher_text - repeated_string + 26) % 26)


def decrypt(repeated_string, cipher_text):
    return "".join(decrypt_letter(h, i) for (h, i) in zip(repeated_string, cipher_text))



def cipher():
    if s == "encrypt":
        need = encrypt(repeated_string, plain_text)
        a = unicodedata.normalize('NFKD', need).encode('ascii','ignore')
        print(a)
        ans = 'secret.txt'
        with open(ans,'wb') as f:
            f.write(a)
        os.rename(ans,os.path.splitext(ans)[0]+ext)


    elif s == "decrypt":
        need = decrypt(repeated_string, cipher_text)
        a = unicodedata.normalize('NFKD', need).encode('ascii','ignore')
        print(a)
        ans = 'secret.txt'
        with open(ans,'wb') as f:
            f.write(a)
        os.rename(ans,os.path.splitext(ans)[0]+ext)
    else : print("Not possible")


file = input("Path for file")
s = input("The operation to be done:\n")
key = input("Type the key here:\n")
ext = os.path.splitext(file)[1]
filehandle = open(file,'rb')
bin_data = filehandle.read()
hex_data = (codecs.encode(bin_data, "hex_codec")).decode('utf-8')
quote   = ''.join([chr(int(''.join(c), 16)) for c in zip(hex_data[0::2],hex_data[1::2])]).replace(';', '\n- ')
plain_text = cipher_text = quote
repeated_string = repeat_string(key, len(plain_text))
cipher()

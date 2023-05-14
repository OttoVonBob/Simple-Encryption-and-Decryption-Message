# -*- coding: utf-8 -*-
"""
Created on Sun May 14 19:57:06 2023

@author: Abdullah

"""

case = []
def fromWordsToNum(statement):
    z26_elements = []
    for char in statement:
        if char.isalpha():  # check if character is a 
            if char != char.upper():
                z26_elements.append((ord(char) - ord('a')) % 26)
            elif char.isupper():
                z26_elements.append((ord(char) - ord('A')) % 26)
                case.append((ord(char) - ord('A')) % 26)
        elif char == ' ':
            z26_elements.append(' ')
    return z26_elements
            
def fromNumToWords(statement):
    decryptedMSG = ''
    for elem in statement:
        if elem == ' ':
            decryptedMSG += ' '
        else:
            if elem in case:
                decryptedMSG += chr(elem + ord('A'))
            else:
                decryptedMSG += chr(elem + ord('a'))
    return decryptedMSG

def encryptor(text):
    encrypted = []
    transaledWords = fromWordsToNum(text)
    print(transaledWords)
    for i in range(len(transaledWords)):
        if transaledWords[i] == ' ':
            encrypted.append(' ')
        else:
            encrypted.append((transaledWords[i] + k) % 26)
    print(encrypted)
    
    print(fromNumToWords(encrypted))
    
def decryptor(text):
    decrypted = []
    transaledWords = fromWordsToNum(text)
    print(transaledWords)
    for i in range(len(transaledWords)):
        if transaledWords[i] == ' ':
            decrypted.append(' ')
        else:
            decrypted.append((transaledWords[i] - k) % 26)
    print(decrypted)
    
    print(fromNumToWords(decrypted))
    

if __name__ == "__main__":
    encryptReq = 'Hello World'
    decryptReq = 'kHoor zruog'
    k = 3
    encryptor(encryptReq)
    decryptor(decryptReq)
    
    
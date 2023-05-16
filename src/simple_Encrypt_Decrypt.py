import tkinter as tk

# List used for holding the position of the capital letter
casePos = []

# Translate from English Alphabet in z26 format
def fromWordsToNum(statement):
    z26_elements = []
    flag = 0
    for char in statement:
        if char.isalpha():  # check if character is a letter
            if char != char.upper():
                z26_elements.append((ord(char) - ord('a')) % 26)
            elif char.isupper():
                z26_elements.append((ord(char) - ord('A')) % 26)
                casePos.append(flag)
            
        elif char == ' ':
            z26_elements.append(' ')
        
        flag += 1
    return z26_elements

#Translate from z26 format to English Alphabet
def fromNumToWords(statement):
    decryptedMSG = ''
    flag = 0
    for elem in statement:
        
        if elem == ' ':
            decryptedMSG += ' '
        else:
            if flag in casePos:
                decryptedMSG += chr(elem + ord('A'))
            
            else:
                decryptedMSG += chr(elem + ord('a'))
        flag += 1
    return decryptedMSG

#Encrypt the english statment
def encryptor(text, k):
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
    return fromNumToWords(encrypted)

#Decrypt the english statement
def decryptor(text, k):
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
    return fromNumToWords(decrypted)
    
#The main function that Runs the GUI and runs the program
def Run(): 
    master = tk.Tk()

    #The key input
    key = tk.Label(text = 'Key:')
    key.pack()

    keyBox = tk.Entry()
    keyBox.pack()
    
    #Encryption message input
    encryption = tk.Label(text='Encryption')
    encryption.pack()

    encryptionBox = tk.Entry()
    encryptionBox.pack()
     
    #Message after encryption
    encrypted = tk.Label(text= "Encrypted Message:")
    encrypted.pack()
    
    encryptedBox = tk.Entry(state='disabled')
    encryptedBox.pack()
    
    #Decryption message input
    decryption = tk.Label(text='Decryption')
    decryption.pack()

    decryptionBox = tk.Entry()
    decryptionBox.pack()

    #Message after decryption
    decrypted = tk.Label(text= "Decrypted Message:")
    decrypted.pack()

    decryptedBox = tk.Entry(state='disabled')
    decryptedBox.pack()

    def EncryptMSG():
        encryptedBox.configure(state='normal')
        encryptedBox.delete(0, tk.END)
        encryptedBox.insert(0, encryptor(encryptionBox.get(), int(keyBox.get())))
        encryptedBox.configure(state='disabled')
        
    def DecryptMSG():
        decryptedBox.configure(state='normal')
        decryptedBox.delete(0, tk.END)
        decryptedBox.insert(0, decryptor(decryptionBox.get(), int(keyBox.get())))
        decryptedBox.configure(state='disabled')
        
    #Encrypt Buttom
    encryptButton = tk.Button(
        text='Encrypt',
        fg='red',
        width='25',
        height='2',
        command= EncryptMSG
        )
    encryptButton.pack()

    #Decrypt Buttom
    decryptButton = tk.Button(
        text='Decrypt',
        fg='blue',
        width='25',
        height='2',
        command= DecryptMSG
        )
    decryptButton.pack()

    master.mainloop()

#Start
Run()
    
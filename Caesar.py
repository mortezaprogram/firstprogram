my_string=input("PLZ inter your message: ")
key=int(input("how many shift do you need? "))
secret_message=""
for word in my_string:
    if word.isalpha():
        char_code = ord(word)
        char_code += key

        if word.isupper():
            if char_code > ord('Z'):
                 char_code -= 26
            elif char_code < ord('A'):
                 char_code += 26
        else:
            if  char_code > ord('z'):
                char_code -= 26
            elif char_code < ord('a'):
                char_code += 26
        secret_message+=chr(char_code)
    else:
        secret_message += word

print("encryptes message",secret_message)


key = -key

orig_message = ""

for word in secret_message:
    if word.isalpha():
        char_code = ord(word)
        char_code += key

        if word.isupper():
            if char_code > ord('Z'):
                 char_code -= 26
            elif char_code < ord('A'):
                 char_code += 26
        else:
            if  char_code > ord('z'):
                char_code -= 26
            elif char_code < ord('a'):
                char_code += 26
        orig_message+=chr(char_code)

    else:
        orig_message += word
print("Decrypted :", orig_message)





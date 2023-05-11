import random

letters=["a","b","c","d","e","f","g","h","i","j","k","l","m","n"]
numbers=["1","2","3","4","5","6","7","8","9","0"]
symbols=["!","@","#","$","%","^","&","*"]
letters_count=int(input("Please input your letters count: \n"))
numbers_count=int(input("Please input your numbers count: \n"))
symbols_count=int(input("Please input your symbols count: \n"))
secret= ""
for letter in range(1,letters_count+1):
    secret+=random.choice(letters)
print(secret)
for number in range(1,numbers_count+1):
    secret+=random.choice(numbers)
print(secret)
for symbol in range(1,symbols_count+1):
    secret+=random.choice(symbols)
print(secret)

mylist=list(secret)
random.shuffle(mylist)
final_secret=""
for secret in mylist:
    final_secret+=secret
print(final_secret)

# for char in secret:
#     final_secret=secret[char]

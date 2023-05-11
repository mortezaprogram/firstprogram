import random
from hangman_words import word_list
from hangman_art import stages
from replit import clear


lives=6

selected_word=random.choice(word_list)
print(f"The selected word is {selected_word}.")
guessed_word=[]
for _ in range(1,len(selected_word)+1):
    guessed_word+="_"
# print(guessed_word)
End_of_game=False
from hangman_art import logo
print(logo)
while End_of_game==False:

    inserted_letter = input("Please insert a letter: ").lower()
    clear()
    for position in range(0,len(selected_word)):
        letter=selected_word[position]
        if letter==inserted_letter:
            guessed_word[position] =inserted_letter
    if inserted_letter not in selected_word:
       lives-=1
       if lives==0:
           print("You Lose")
           End_of_game=True
    print(stages[lives])
        # else:
             # print("Wrong")
    print(guessed_word)
    if "_" not in guessed_word:
        End_of_game=True
        print("You Win")
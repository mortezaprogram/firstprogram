alphabet=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
should_continue=True
while should_continue:
     direction=input("Please insert your direction: \n")
     start_MSG=input("Please insert your message: \n")
     shift_number=int(input("Please input your shift: \n"))
     shift_number=shift_number % 26
     def ceasar(start_MSG,shift_number,direction):
         end_txt=""
         if direction == "decode":
             shift_number *= -1
         for letter in start_MSG:
             position=alphabet.index(letter)
             new_position=position+shift_number
             end_txt+=alphabet[new_position]
         print(end_txt)

     ceasar(start_MSG,shift_number,direction)
     result=input("Do you want to continue(yes/no)? \n")
     if result=="no":
         should_continue=False
         print("Goodbye")
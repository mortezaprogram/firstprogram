'''
def greet_with_name(name,location):
    print(f"Hello {name} from {location}")

greet_with_name(name="morteza",location="Tehran")
'''
import math
def how_many_cans(height,lenght,cans_need_for_square_meter):
    # height=input("Please input height: ")
    # lenght=input("Please input lenght: ")
    # cans_need_for_square_meter=input("Please input cans_need_for_square_meter: ")
    cans=math.ceil((height*lenght)/cans_need_for_square_meter)
    print(f"You need {cans} cans for {lenght*height} square meter")

how_many_cans(4,5,2)

'''programming_dict={"Bug":"Failure in program.","Key":"word for login.","Price":"How much pay for it."}
for record in programming_dict:
    print(f"{record}: ")
    print(programming_dict[record])

student_records={"david":60,"jack":67,"john":77,"bill":88,"sara":93}
score_records={}
for student in student_records:
    score=student_records[student]
    if score >= 90:
        score_records[student]="best"
    elif score >= 80 and score < 90:
        score_records[student]="good"
    else:
        score_records[student]="bad"
print(score_records)

travel_log=[
    {"country":"France",
     "cities_visit":["paris", "dijin"],
     "number_of_visit":12},

    {"country":"germany"
        ,"cities_visit":["berlin", "humburg"],
     "number_of_visit":14}]

def add_new_record_to_dict(country,cities_visit,number_of_visit):
    new_country={}
    new_country["country"]=country
    new_country["cities_visit"]=cities_visit
    new_country["number_of_visit"]=number_of_visit
    travel_log.append(new_country)
add_new_record_to_dict("Turkey",["istanbul","Ankara"],21)
print(travel_log)
'''
from replit import clear
bids={}
bidding_finished=False
def find_highest_bidder(bidding_records):
    highest_record=0
    winner=""
    for bibber in bidding_records:
        bid_amount=bidding_records[bibber]
        if bid_amount>highest_record:
            highest_record=bid_amount
            winner=bibber
    print(f"The winner is {winner} with bid amount of {highest_record}")


while not bidding_finished:
    name=input("What is your name? ")
    price=int(input("What is your bid: $"))
    bids[name]=price
    should_continue=input("Do you whant to continue?(yes/no)")
    if should_continue=="no":
        bidding_finished=True
        find_highest_bidder(bids)
    elif should_continue=="yes":
        clear()














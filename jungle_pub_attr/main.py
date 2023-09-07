from jungleBook import Jungle,RateJungle
def main():
    j = Jungle("Meher")
    j.welcomemessage()
    r = RateJungle(3)
    r.printRating()
    r._staffRating = 30
    print("Staff rating : ", r._staffRating)
    # print("Jungle Guide rating : ", r.__jungleGuideRating)
    print("Guide rating : ", r._RateJungle__jungleGuideRating)

if __name__=="__main__":
    main()
from jungleBook import Jungle,RateJungle
def main():
    j=Jungle().welcomemessage()
    k=Jungle("Mori").welcomemessage()

    r = RateJungle("Meher", 3)
    r.printRating()
    r.welcomemessage

if __name__=="__main__":
    main()

class Dog:
    num_of_dogs = 0

    def __init__(self , name="Unknown"):
        self.name = name
        Dog.num_of_dogs += 1

    @staticmethod
    def get_num_of_dogs():
        print("{} is number of dogs".format(Dog.num_of_dogs))
def main():
    spot=Dog("Spot")
    doug=Dog("Doug")
    prsh=Dog("Prsh")
    spot.get_num_of_dogs()
main()




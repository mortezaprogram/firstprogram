class Jungle:
    def __init__(self,animal="Elephant",isPet="Yes"):
        self.animal=animal
        self.isPet=isPet


def main():
    j1=Jungle()
    print(j1.__dict__)
    j2 = Jungle("Lion", "No")
    print(j2.__dict__)
    print(Jungle.__dict__)
    print(Jungle.__doc__)
if __name__=='__main__':
    main()
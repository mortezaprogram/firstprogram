class Jungle:
    def __init__(self,name="unknown"):
        self.visitorname=name

    def welcomemessage(self):
        print("Hello %s,Welcome"%self.visitorname)
class RateJungle(Jungle):
    def __init__(self,name,feedback):
        self.feedback=feedback
        super().__init__(name)
    def printRating(self):
        print("Thank %s for your rating "%self.visitorname)
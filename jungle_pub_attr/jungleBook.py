class Jungle:
    def __init__(self,name="Unknown"):
        self.visitorNmae=name
    def welcomemessage(self):
        print("welcome %s ",self.visitorNmae)

class RateJungle:
    def __init__(self,feedback):
        self.feedback=feedback
        self._staffRating = 50
        self.__jungleGuideRating = 100
        self.updateStaffRating()
        self.updateGuideRating()

    def printRating(self):
        print("Feedback : %s \tGuide Rating: %s \tStaff Rating: %s " % (self.feedback, self.__jungleGuideRating, self._staffRating))

    def updateStaffRating(self):
        if self.feedback <5:
            self._staffRating+=5
        else:
            self._staffRating-+5

    def updateGuideRating(self):
        if self.feedback <5:
            self.__jungleGuideRating+=10
        else:
            self.__jungleGuideRating-=10


class Jungle:
    sum_of_feedback = 0.0
    def __init__(self,name="Unknown"):
        self.visitorName=name
    def welcomeMessage(self):
        print("Hello %s "%self.visitorName)

    def averageFeedback(self):
        self.__avg_feedback = Jungle.sum_of_feedback / RateJungle.total_num_feedback
        print("Average feedback : ", self.__avg_feedback)
class RateJungle(Jungle):
    total_num_feedback = 0

    def __init__(self, name, feedback):
        self.feedback=feedback
        Jungle.sum_of_feedback+=self.feedback
        RateJungle.total_num_feedback += 1
        super().__init__(name)

    def printRating(self):
        print("Thanks %s for your feedback" % self._visitorName)


class Test:
    def __init__(self):
        print("sum_of_feedback (Jungle class attribute) : ", Jungle.sum_of_feedback)
        print("total_num_feedback (RateJungle class attribute) : ", RateJungle.total_num_feedback)
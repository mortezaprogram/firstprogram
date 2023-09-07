from abc import ABCMeta,abstractmethod

class Jungle(metaclass=ABCMeta):
    def __init__(self,name="unkown"):
        self.visitorName=name
    def welcomeMessage(self):
        print("Hello %s .Welcome to the jungle"%self.visitorName)

    @abstractmethod
    def scarySound(self):
        pass
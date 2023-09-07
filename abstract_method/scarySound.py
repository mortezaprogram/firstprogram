from jungleBook import Jungle

class Animal(Jungle):
    def scarySound(self):
        print("Animals are running away due to scary sound.")

class Bird(Jungle):
    def scarySound(self):
        print("Birds are flying away due to scary sound.")

 # since Jungle is defined as metaclass
 # therefore all the abstract methods are compulsory be defined in child class
class Insect(Jungle):
     def scarySound(self):
         print("Insects do not care about scary sound.")
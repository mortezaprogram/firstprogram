class admin:
    def __init__(self,name,weight,height,income):
        self.name = name
        self.weight=weight
        self.height=height
        self.income=income
    def myname(self):
        print("{} is my name. ".format(self.name))
    def myweight(self):
        print("{} is my weight. ".format(self.weight))

    def myheight(self):
        print("{} is my height. ".format(self.height))

    def myincome(self):
        print("{} is my income. ".format(self.income))
def main():
       test=admin("Mori",60,2,3)
       test.myname()
       test.myweight()
       test.myheight()
       test.myincome()
main()

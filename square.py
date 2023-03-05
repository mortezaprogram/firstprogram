class Square:
    def __init__(self,width="0",height="0"):
        self.width=width
        self.height=height
    @property
    def height(self):
        print("Retrieving the height")
        return self.__height
    @height.setter
    def height(self,value):
      if value.isdigit():
        self.__height=value
      else:
        print("Please inter valid value")
    @property
    def width(self):
        print("Retrieving the height")
        return self.__width
    @width.setter
    def width(self,value):
      if value.isdigit():
        self.__width=value
      else:
        print("Please inter valid value")
    def get_area(self):
        return int(self.__width)*int(self.__height)


def main():
    square=Square()
    width=input("Please inter the width: ")
    height=input("Please inter the height: ")
    square.width=width
    square.height=height
    print(square.width)
    print(square.height)
    print("Area is: ",square.get_area())
main()

class Time:
    def __init__(self,hour=0,minute=0,second=0,milisecond=0):
        self.hour=hour
        self.minute=minute
        self.second=second
        self.milisecond=milisecond
    def __str__(self):
      return "{}:{:02d}:{:02d}:{:03d}".format(self.hour,self.minute,self.second,self.milisecond)
    def __add__(self,other_time):
      new_time=Time()
      if (self.milisecond+other_time.milisecond)>=100:
          self.second+=1
          new_time.milisecond=(self.milisecond+other_time.milisecond)-100
      else:
          new_time.milisecond=self.milisecond+other_time.milisecond
      if(self.second+other_time.second) >= 60:
          self.minute+=1
          new_time.second=(self.second+other_time.second)-60
      else:
          new_time.second=self.second+other_time.second
      if (self.minute + other_time.minute) >= 60:
          self.hour += 1
          new_time.minute=(self.minute + other_time.minute) - 60
      else:
          new_time.minute = self.minute + other_time.minute
      if (self.hour + other_time.hour) >= 24:
          new_time.hour=(self.hour + other_time.hour) - 24
      else:
          new_time.hour = self.hour + other_time.hour
          return new_time
def main():
    time1=Time(10,45,55,99)
    print(time1)
    time2=Time(10,45,8,99)
    print(time2+time1)
main()

class Sum:
  @staticmethod
  def get_sum(*args):
      sum_1=0
      for i in args:
          sum_1+=i
      return sum_1
def main():
  print("Sum:",Sum.get_sum(11,13,14))
main()
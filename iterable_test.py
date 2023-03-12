'''
samp_iter=iter("my_samplae")
print("Char: ",next(samp_iter))
print("Char: ",next(samp_iter))
print("Char: ",next(samp_iter))
print("Char: ",next(samp_iter))
'''
class Alphabet:
    def __init__(self):
       self.letters="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
       self.index=-1

    def __iter__(self):
       return self

    def __next__(self):
       if self.index >= len(self.letters)-1:
           raise StopIteration
       self.index+=1
       return self.letters[self.index]
alpha=Alphabet()
for letter in alpha:
    print(letter)

Mori={"fname":"mori","lname":"XLG"}
for key in Mori:
    print(key,Mori[key])

class FibGenerator:
    def __init__(self):
        self.first=0
        self.second=1
    def __iter__(self):
        return self
    def __next__(self):
        fib_num=self.first+self.second
        self.first=self.second
        self.second=fib_num
        return fib_num

fib_seq=FibGenerator()
for i in range(10):
    print("Fib: ",next(fib_seq))

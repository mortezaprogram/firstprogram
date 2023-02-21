
def prime_number(num):
    for i in range(2,num):
        if (num%i) == 0:
            return False
    return True

def get_prime(max_number):
   list_of_primes = []
   for j in range(2,max_number):
       if(prime_number(j)):
         list_of_primes.append(j)
   return list_of_primes
max_number=int(input("Please input max number: "))
print(get_prime(max_number))
def sum_cal(*args):
    sum=0
    for i in args:
        sum += i
    return sum
print(sum_cal(2,3))

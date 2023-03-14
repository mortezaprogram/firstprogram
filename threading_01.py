
'''
def execute_threat(i):
    print("Thread {} sleeps at {}".format(i,time.strftime("%H:%M:%S",time.gmtime())))
    print()
    rand_sleep_time=random.randint(1,5)
    time.sleep(rand_sleep_time)
    print("Thread {} stop sleep at {}".format(i,time.strftime("%H:%M:%S",time.gmtime())))
for i in range(10):
    threat=threading.Thread(target=execute_threat,args=(i,))
    threat.start()
    print()
    print("Active Threat: ",threading.activeCount())
    print("Threat Objects",threading.enumerate())


class Cust_Thread(threading.Thread):
    def __init__(self,name):
        threading.Thread.__init__(self)
        self.name=name
    def run(self):
        get_time(self.name)
        print("Thread",self.name,"Execution Ends")
def get_time(name):
    print("Threat {} sleeps at {}".format(name,time.strftime("%H:%M:%S",time.gmtime())))
    rand_sleep_time=random.randint(3,8)
    time.sleep(rand_sleep_time)

thread1=Cust_Thread("1")
thread2=Cust_Thread("2")
thread1.start()
thread2.start()
print("Threat 1 is live: ",thread1.is_alive())
print("Threat 2 is live: ",thread2.is_alive())
print("Threat 1 name is: ",thread1.getName())
print("Threat 2 name is: ",thread2.getName())
thread1.join()
thread2.join()
print("End Execution")
'''

import threading
import time
import random
class BankAccount(threading.Thread):
    account_balance=100
    def __init__(self,name,money_request):
        threading.Thread.__init__(self)
        self.name=name
        self.money_request=money_request
    def run(self):
        threadLock.acquire()
        BankAccount.get_money(self)
        threadLock.release()
    @staticmethod
    def get_money(customer):
        print("{} try to withdraw ${} at {} ".format(customer.name,customer.money_request,time.strftime("%H:%M:%S",time.gmtime())))
        if BankAccount.account_balance-customer.money_request>0:
            BankAccount.account_balance-=customer.money_request
            print("New Account balance is ${} ".format(BankAccount.account_balance))
        else:
            print("There aren't enough money in your account.")
            print("Your account balance is ${}".format(BankAccount.account_balance))
        time.sleep(2)
threadLock=threading.Lock()
mori=BankAccount("Mori",1)
david=BankAccount("David",100)
helen=BankAccount("Helen",50)
mori.start()
david.start()
helen.start()

#print("Mori is a live: ",mori.is_alive())
#print("David is a live: ",david.is_alive())
#print("Helen is a live: ",helen.is_alive())
mori.join(timeout=1)
david.join(timeout=1)
helen.join(timeout=1)
print("Execution Ends")










num_list=[1,23,55,22,11,33,2,777,999,654]
i=len(num_list)-1
while i>1:
    j=0
    while j<i:
        print("\nls {}>{}".format(num_list[j],num_list[j+1]))
        print()
        if num_list[j]<num_list[j+1]:
            print("switch")
            temp=num_list[j]
            num_list[j]=num_list[j+1]
            num_list[j + 1]=temp
        else:
            print("Don't switch")
            j+=1
        for k in num_list:
            print(k,end=",")
            print()
    print("end of round")
    i-=1
for k in num_list:
    print(k, end=",")
    print()
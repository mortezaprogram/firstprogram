import math
num_list=[i*2 for i in range(10) ]
print(num_list)
pow_num_list=[[math.pow(m,2),math.pow(m,3),math.pow(m,4)] for m in num_list]
print(pow_num_list)
multi_dim_list=[[0]*10 for i in range(10)]

for i in range(10):
    for j in range(10):
        multi_dim_list[i][j]="{}:{}".format(i,j)
for i in range(10):
    for j in range(10):
        multi_dim_list[i][j] = "{}:{}".format(i, j)
        print(multi_dim_list[i][j],end="|")
    print()
print()
print()
multi_dim_list=[[0]*10 for i in range(10)]
for i in range(10):
    for j in range(10):
        multi_dim_list[i][j]="{}".format((i+1)*(j+1))
for i in range(10):
    for j in range(10):
        print(multi_dim_list[i][j],end="|")
    print()

row1=[" "," "," "]
row2=[" "," "," "]
row3=[" "," "," "]
row=[row1,row2,row3]
print(f"{row1}\n{row2}\n{row3}\n")
position=input("Please input your position to change: \n")
p1=int(position[0])
p2=int(position[1])


row[p1-1][p2-1]="X"

print(f"{row1}\n{row2}\n{row3}\n")
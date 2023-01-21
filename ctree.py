tree_height=int(input("Please input height of tree: "))
spaces=tree_height-1
hash=1
stump_space=tree_height-1
while tree_height!=0:
    for i in range(spaces):
        print(' ',end="")
    for i in range(hash):
        print('#',end="")
    spaces-=1
    hash+=2
    tree_height-=1
    print()
for i in range(stump_space):
    print(' ',end="")
print("#")


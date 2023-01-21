while True:
    try:
        number=int(input("Please input the number: "))
        break
    except ValueError:
        print("Please input valid number")
    except:
        print("Please input valid number x")
print("TNX")
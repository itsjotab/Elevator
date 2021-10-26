floor = input("Floor number: ")
level = int(floor)

if level <= 5:
    if level == 1:
        print ("1st floor")
    elif level == 2:
        print("2nd floor it is!")
    elif level == 3:
        print("Youre 2 floors up from where you started")
    elif level == 4:
        print("4th floor")
    elif level == 5 :
        print("Youre at the top!!")
else:
    print("We dont go that high.. Sorry!")

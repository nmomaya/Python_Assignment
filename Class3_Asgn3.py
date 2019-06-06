"""  Triangle Inequality Theorem """

side1 = eval(input("Enter Side1: "))
print ("You entered: ",side1)

side2 = eval(input("Enter Side2: "))
print ("You entered: ",side2)

side3 = eval(input("Enter Side3: "))
print ("You entered: ",side3)

if ((side1+side2) < side3 and (side1+side3) < side2 and (side2+side3) < side1):
    print("It's an triangle")
else:
    print("It's not a triangle")

    """
    while True:
            try:
                side1 = int(input("Enter Side1: "))
                break
            except:
                print("That's not a valid option!")

    """

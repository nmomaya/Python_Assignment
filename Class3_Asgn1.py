"""  Max\Min number """

number1 = eval(input("Enter First Number: "))
print ("You entered: ",number1)
print (type(number1))
number2 = eval(input("Enter Second Number: "))
print ("You entered: ",number2)
print (type(number2))
number3 = eval(input("Enter Third Number: "))
print ("You entered: ",number3)
print (type(number3))
"""
if (number1 < number2) and (number1 < number3):
    print("Max number is", number1)
elif (number2 > number3):
    print ("Max number is:", number2)
else:
    print("Max number is",number3)

print("The sum of" + number1 "and " +number2 "is" number1 + number2)

print ("Sum is: ",number1+number2)

print("The sum of {0} and {1} is {2}".format(number1,number2,sum1))
"""
def minimum(number1,number2,number3):
    if (number1 < number2) and (number1 < number3):
        print("Min number is: %d"%(number1))
    elif (number2 < number3):
        print("Min number is:", number2)
    else:
        print("Min number is", number3)



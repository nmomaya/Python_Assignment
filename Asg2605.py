"""
Assignment1: Write program convert int to string

if __name__ == '__main__':
    no = int(input("Enter Number:"))
    output = str(no)
    print(type(output),str(output))


Assignment2: Accept no from user and check for Divisibility of 2,3, and 5

def div(no1, no2):
    if no1 % no2 == 0:
        return True
    else:
        return False

if __name__ == '__main__':
    no1 = eval(input("Enter Number:"))
    if (div(no1,2) == True) and (div(no1,3) == True) and (div(no1,5) == True):
        print("{} is divivded by 2 ,3 and 5".format(no1))
    elif (div(no1, 2) == True) and (div(no1, 3) == True):
        print("{} is divivded by 2 and 3".format(no1))
    elif (div(no1, 2) == True) and (div(no1, 5) == True):
        print("{} is divivded by 2 and 5".format(no1))
    elif (div(no1, 3) == True) and (div(no1, 5) == True):
        print("{} is divivded by 3 and 5".format(no1))
    elif (div(no1, 2) == True):
        print("{} is divided by 2".format(no1))
    elif (div(no1, 3) == True):
        print("{} is divided by 3".format(no1))
    elif (div(no1, 5) == True):
        print("{} is divided by 5".format(no1))
    else:
        print("{} is not divided by 2,3 and 5".format(no1))

"""
"""
Assignment3: Accept line from user 
if length of input line is less than20 char , print Very Short Line
if length of input line is between 20 to 80 char, print Sufficent Line
if length of input line is more than 80 char, print Length of Line exceeded

def charlength(str1):
    if len(str1) <= 20:
        print("You entered very short line!!!")
    elif len(str1) > 20 and len(str1) < 80:
        print("You entered sufficient line!!!")
    else:
        print("You exceeded the limit!!!")

if __name__ == '__main__':
    str1 = eval(input("Enter Charcetrs"))
    charlength(str1)
"""
"""
Assignment5: Accept number from user stop when user enter multiple of 11

no1 = 10
while(no1 % 11 != 0):
    no1 = eval(input("Enter no:"))
    print("Entered no.:",no1)
"""
"""

Assignment 8:Accept Start index,end index and step value from user, Define your own slice function
"""




"""
Assignment 9: Accept two string from user and chk the reversal of string

"""
"""
def streversal(str1,str2):
    st3 = st1[::-1]
    print(st3)
    if (st2 == st3):
        print("String {} is Reversal of {}".format(st1,st2))
    else:
        print("String {} is not Reversal of {}".format(st1, st2))


st1,st2 = eval(input("Enter Two Strings: "))
streversal(st1,st2)

"""
"""
Assignment 10: Reversal of number
"""
"""
def reverse(no):
    rev=0
    while(no>0):
        dig=no%10
        rev=rev*10 + dig
        no=no//10
    return(rev)


no = int(input("Enter number for reverse: "))
print("Reversal of number {} is {} ".format(no,reverse(no)))
"""
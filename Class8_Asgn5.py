# Write a program to accept numbers from user check it is Armstrong

def armstrong(no1):
    no2 = no1
    sum = 0
    while (no2 > 0):
        digit = no2 % 10
        print (digit)
        sum = sum + digit ** 3
        #import math
        # math.floor(no2) #Getting infinet loop error
        no2 //= 10
        
    if (no1 == sum):
        print("{} number is Palindrome".format(no1))
    else:
        print("{} number is not a Palindrome".format(no1))


  
no1 = eval(input("Enter Number:"))
armstrong(no1)
    


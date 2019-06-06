""" Write a program to accept a range from user & display
sum of odd numbers in that range """

lb,ub = eval(input ("Please enter range of number"))
print(lb,ub)
y = 0

if(lb < ub):
    for x in range(lb,ub+1):   """ ub=1 used to include the upperbond number """
        if((x & 1) == 1):
            print ("Odd numbers in the range is %d"%x)
    y = x + y
    print ("Total count of odd number for given range is %d" %y)       
else:
    print ("Incorrect range")

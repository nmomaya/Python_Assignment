""" Write a program to perform menu driven arithmatic operations.
Hind: write funt for + - * /. Show choices to user +-*/exit. """
def arh(no1,no2,opr):
    if (opr == "*"):
        return (no1*no2)
        #print ("Your answer is %f" %(no1*no2))
    elif (opr == "+"):
        return (no1+no2)
    elif (opr == "-"):
        return (no1-no2)
    elif (opr == "/"):
        return (no1/no2)

no1,no2 = eval(input ("Please enter two numbers"))
opr = eval(input ("Please select the arithmatic operations +,-,*,/ :"))
result = arh(no1,no2,opr)
print ("   %d \n %s %d \n ------- \n %d"%(no1,opr,no2,result))

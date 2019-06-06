def minimum(number1,number2,number3):
    if (number1 < number2) and (number1 < number3):
        return number1
    elif (number2 < number3):
        return ("No2:"+repr(number2))
    else:
        return ("No3:"+repr(number3))

if __name__ == '__main__':
    no1,no2,no3 = eval(input("Enter three Numbers"))
    result = minimum(no1,no2,no3)
    print ("Minimum number amoung number1:%d Number 2:%d Number 3:%d is %d"%(no1,no2,no3,result))
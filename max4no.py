"""
def max4no(n1,n2,n3,n4):
    return(max(n1,n2,n3,n4))

if __name__ == '__main__':
    no1,no2,no3,no4 = eval(input("Enter four Numbers:"))
    result = max(no1,no2,no3,no4)
    print ("Max number is %d"%(result))
"""
def max4no():
    numbers = []
    '''
    while True:
        number = eval(input("Please enter a number. Enter 0 to finish.: "))

        if number == 0:
            break
        numbers.append(number)
    '''
    numbers = eval(input("Enter List of Numbers:"))
    print("Maximum of {} is {}".format(numbers, max(numbers)))

max4no()


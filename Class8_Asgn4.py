# Write a function which should be able to add 2,3,4, 5 no's

def add(a,b,c=0,d=0,e=0):
    return(a+b+c+d+e)

#no1 = eval(input("Enter how many number you want for addtiona"))
#for i in range (no1):
#    no2[i] = eval(input("Enter {} numbers for additiona".format(no1))

result = add(5.2,6.3,7)
print("Addtion of nubmer is {}".format(result))

result = add(5,6)
print("Addtion of nubmer is {}".format(result))

result = add(5,6,7.2,4.5,7.8)
print("Addtion of nubmer is {}".format(result))


# Write a function which should be able to add 'n' no's

def addno(*nos):
    y = 0
    for x in nos:
        y = y + x
    print("Addtiona of provided number is {}".format(y))
"""
# Entering mutiple inputs bu user
total_no = eval(input("How many numbers do you want for addtion:").split(,))
for i in range (1,total_no+1):
    print ("Enter {}st number".format(i))
    nos [i]= eval(input()) # getting some error
    print (nos)
""" 
addno(12,56,78,89.9,45.6,78.4,67.4,7,6,3,2)

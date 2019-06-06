# Write a prog accept range from user and print all the numbers
# in that range which are not multiple of 2 and 3 - use continue

def module(lb,ub):
    for i in range (lb,ub):
        if (i%2 == 0 or i%3 == 0):
            continue
        print(i)
    
lb,ub = eval(input("Enter numbers"))
if (lb < ub):
    module(lb,ub)
else:
    print ("Incorrect range")
             

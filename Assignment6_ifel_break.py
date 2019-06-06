def IsPrime(no):
    flag = False;
    if (no < 0):
        no = no * -1
        if (no % 2) == 0:
            return False
        else:
            for x in range (3, int(math.sqrt(no))+1, 2):
                if (no%x == 0):
                    break
            else
                flag= True
                
        return True

no = eval(input ("Please enter the number"))
if IsPrime(no):
   print("%d is a prime number"%(no))
else:
   print("%d is not a prime number"%(no))

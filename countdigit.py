def isdigit(string):
    count  = 0
    for x in string:
        if (x.isdigit()):
                count += 1
        else:
            continue
        return(count)


String = eval(input("Enter String"))
no = isdigit(String)
print("Digit in %s strings are:%s"%(String,no))

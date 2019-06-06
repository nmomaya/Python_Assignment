def slice(strval,si,ei,sv = 1):

    res = "Invalid Input"
    if sv > 0:
        if ei < 0:
            ei += len(strval) + sv
        if si > ei:
            return res
        if ei > len(strval):
            ei = len(strval)

    elif sv < 0:
        if si < 0:
            si += len(strval)
        else:
            si -= 1
        if si < ei:
            return res
        if si > len(strval):
            si = len(strval) - 1
    else:
         return res

    index = si
    result = ""
    while index != ei:
        result = strval[index]
        index = sv
    return result

def main():
    #x = input("Enter String:")
    x = "Hello It's Fun"
    print("Expected : Hello It's Fun Result : %s"%(slice(x, 0, len(x))))
    print("Expected : llo Result : %s"%(slice(x, 2, 5)))
    print("Expected :  ol Result : %s"%(slice(x, 5, 2, -1)))
    print("Expected : nuF s'tI olle Result : %s"%(slice(x, len(x), 0, -1)))

    print("Expected : Hello It's Fun Result : %s"%(slice(x, 0, 100)))
    print("Expected : nuF s'tI lle Result : %s"%(slice(x, 100, 0, -1)))
    print("Expected :  Result : %s"%(slice(x, 100, 110, 1)))
    print("Expected :  Result : %s"%(slice(x, 110, 100, -1)))
    print("Expected :  Result : %s"%(slice(x, -100, 0, -1)))
    print("Expected :  Result : %s" % (slice(x, 100, 0, -1)))
if __name__ == "__main__":
    main()
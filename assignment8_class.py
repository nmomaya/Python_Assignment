input_str = eval(input("Enter String one:"))
validate_str = eval(input("Enter String two:"))
if (IsRotation(input_str, validate_str)):
    print ("{0} is rotation of {1}".format(validate_str,input_str))
else:
    print ("{1} is not rotation of {0}".format(validate_str,input_str))

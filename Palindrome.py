""" Palindrome String """

st1 = eval(input("Enter String: "))
st2 = st1[::-1]

if (st2 == st1):
    print("String %s is Palindrome"%(st1))
else:
    print("String %s is not Palindrome"%(st1))


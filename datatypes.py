""" Data Types """

x = 10
type(x)
type(++x)
""" type(x++) will give error """

x= 3+4j  """ complex data type """
type(x)

x =100
id(x)
y=x
id(y)
z= 1000
id(z)
""" here id of x and y will be same """
x="Hello"
x=y
z="Hello"
id(x),id(y),id(z)
"""Single word associated to same memory location - Inelegancy of python """

x="Hel lo"
x=y
z="Hel lo"
id(x),id(y),id(z)

""" Space will give different memory locatrion """
x= "Hello"
y="World"
x+y
"Hello World"


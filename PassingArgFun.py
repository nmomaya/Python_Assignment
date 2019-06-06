# 1) Positional :
def PostArgDemo(a,b):
    print("Pos Arg Passed are ={},{}".format(a,b)) 

PostArgDemo(10,20)

# 2) Keyword Arguments
def KeyArgDemo(a,b):
    print("Key Arg Passed are ={},{}".format(a,b)) 

KeyArgDemo(b=10,a=20)

# 3) Default Parameters

def DefParamDemo(a,b = 100):
    print("Def Arg Passed are ={},{}".format(a,b)) 


DefParamDemo(10)   # a =10, b=100
DefParamDemo(10,20)   #a =10, b=20 it overwrites the value

#4) Variable Number of Arguments Demo

def VariableNumberofArgumentsDemo(*args):
    print(type(args))
    for x in args:
        print(x)


VariableNumberofArgumentsDemo(1,2,3,4)
VariableNumberofArgumentsDemo(14,62,83,94.67,75,6,"Hi","Bye")

"""
for i in range(4):
    pass
else:
    print:"Finish"

    
def PostArgDemo(a,b):
    print("Pos Arg Passed are ={},b{}".format(a,b)) 

def main():
    PostArgDemo(10,20)


"""





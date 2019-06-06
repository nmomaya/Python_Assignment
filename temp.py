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

def VariableNumberofArgumentsDemo(*args):
    print(type(args))
    for x in args:
        print(x)


VariableNumberofArgumentsDemo(1,2,3,4)
VariableNumberofArgumentsDemo(14,62,83,94.67,75,6,"Hi","Bye")



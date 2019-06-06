""""
def IsPrime(no1):
    import math
    if (no1 < 0):
        no1 = no1 * -1
    if (no1 % 2 == 0):
        return False
    else:
        for x in range(3, int(math.sqrt(no1)) + 1, 2):
            if no1 % x == 0:
                return False
        return True

def main():
    no1, no2 = eval(input("Enter Range of Number in increasing"))
    for i in range (no1,no2):
        if IsPrime(i):
            print(i)

if __name__ == "__main__":
    main()
"""
"""
def table(no):
    print("Displaying Table of %d"%(no))
    for i in range (1,11):
        print ("%d * %d  = %d"%(no,i,(no*i)))


def main():
    no1, no2 = eval(input("Enter Range of Number in increasing"))
    for no in range (no1,no2+1):
         table(no)

if __name__ == "__main__":
    main()
"""
"""
def fun(x,y,z,no2=1):
    print(x,y,z,no2)

def main():
    fun(2,5,z=10)

if __name__ == "__main__":
    main()
"""
"""
def mul(n1,n2,n3 = 1,n4 =1,n5 =1):
    print(n1*n2*n3*n4*n5)

def add(n1,n2,n3,n4 =0,n5 =0):
    print(n1,n2,n3,n4,n5)

def main():
    mul(3,3)
    add(3,3,n5 = 8,n3 = 10)
if __name__ == "__main__":
    main()
"""
"""
def add( *args):
    sum = 0
    for x in args:
        if type(x) == 'int':
            print(x)
            sum = x + sum
        else:
            continue
    print(sum)
add(1,2,3,"n")
"""
def demo(a,b,*args,**kwargs):
    print(type(a))
    print(type(args))
    print(type(kwargs))
    for x in args:
        print(x)
    for x in kwargs:
        print(x,kwargs[x])

demo(1,2,3,4,5,name="Nimesh",hobby="Travelling",company="Veritas")



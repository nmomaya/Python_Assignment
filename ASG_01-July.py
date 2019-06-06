"""
WAP to accept file from user , display alternate characters
"""
"""
def altchar(filename):
    if type(filename) == str and filename != "":
        import io
        fd = io.FileIO(filename,"r")
        fd1 = io.FileIO("alt.txt","w")
        if fd != None:
            while True:
                ch = fd.read(1)
                fd1.write(ch)
                if ch == b"":
                    break;
                print(ch)
                fd.read(1)
                #fd.seek(1,1)
def main():
    n = input("Please provide the file name")
    altchar(n)

if __name__ == '__main__':
    main()
"""
"""
WAP to accept file from user & display first alternate charcaters  and than remainng alternate char.
e.g. 1 -> 10, 21->30
next iteration 11->20
"""
import io
def charopr(filename):
    if type(filename) == str and filename != "":
        fd = io.FileIO(filename,"r")
        if fd != None:
            #while True:
                #fd.seek(1,10)
                ch = fd.read(1)
                print(ch)

def main():
    #n = input("Please provide the file name")
    charopr("c:\\readline1.txt")

if __name__ == '__main__':
    main()

"""
# WAP to accept file from user read line find length and compare with next line

def readline(filename):
    import io
    fd = io.FileIO(filename,"r")
    if type(filename) == str and filename != "":
        i = 0
        if fd != None:
            for line in fd:
                print(line)
                if (len(line) >= i):
                    i = len(line)
                    print("Line is {} and Length is {}".format(line,i-2))
        print(i-2)

def main():
    #n = input("Please provide the file name")
    readline("c:\\readline1.txt")

if __name__ == '__main__':
    main()

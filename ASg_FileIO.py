"""
WAP to accept file from user & display first alternate charcaters  and than remainng alternate char.
e.g. 1 -> 10, 21->30
next iteration 11->20
"""
import io
def charopr(filename):
    if type(filename) == str and filename != "":
        import io
        fd = io.FileIO(filename, "r")
        if fd != None:
            while True:
                ch = fd.read(10)
                print(ch)
                if ch == b"":
                    break;
                print(ch)
                fd.read(1)
                # fd.seek(1,1)
def main():
    #n = input("Please provide the file name")
    charopr("c:\\readline1.txt")

if __name__ == '__main__':
    main()

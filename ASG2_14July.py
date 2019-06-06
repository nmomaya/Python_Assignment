def copyfile(sf1,df1):
    import io
    if type(sf1) == str and sf1 != "":
        fd = io.FileIO(sf1, "r")
        fd1 = io.FileIO(df1,"w")
        if fd != None:
            line = fd.readline()
            while (line != b""):
                line = fd.readline()
                fd1.write(bytes(line))

def main():
    import sys
    print(sys.argv)
    #sf = input("Please provide the file names to copy")
    #df = input("Please provide the file names to paste")
    #copyfile("C:\\Test\\petrol1.txt","C:\\Test\\new.txt")
    copyfile(sys.argv[1],sys.argv[2])

if __name__ == '__main__':
    main()

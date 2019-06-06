def avgpetrol(filename):
    import io
    if type(filename) == str and filename != "":
        fd = io.FileIO("c:\\Petrol.txt", "r")
        mpetrol = 0
        kpetrol = 0
        gpetrol = 0
        if fd != None:
            line = fd.readline()
            while (line != b""):
                petrol = line.split(b" ")
                mpetrol = mpetrol + petrol[1]
                kpetrol = kpetrol + petrol[2]
                gpetrol = gpetrol + petrol[3]
                print(mpetrol,kpetrol,gpetrol)
                line = fd.readline()
        mavg =

def main():
    #n = input("Please provide the file name")
    avgpetrol("c:\\Petrol.txt")

if __name__ == '__main__':
    main()

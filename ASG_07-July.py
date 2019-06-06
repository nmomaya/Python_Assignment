def fileopr(filename):
    import io
    if type(filename) == str and filename != "":
        result = {}
        session = {}

        fd = io.FileIO("c:\\audio.conf","r")
        if fd != None:
            line = fd.readline() # read first line
            while (line != b""):
                if not line.startswith(b"#"):
                    if not line.startswith(b"\n"):
                        line = line[:-1] #this code remove '\n'from the line
                        if (b"=" in line):
                            if (b"#" in line):
                                index = line.find(b"#")
                                line = line[:index]

                            pair = line.split(b"=")
                            pair[0]  = pair[0].strip()
                            pair[1] = pair[1].strip()
                            
                line = fd.readline()
        print(result)
        print()

def main():
    #n = input("Please provide the file name")
    fileopr("c:\\audio.conf")

if __name__ == '__main__':
    main()

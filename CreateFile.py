def createfile(dr,file):

    import os
    dirpath = "c:/Test/" + dr
    print(dirpath)
    os.mkdir(dirpath)
    filepath = dirpath + "/" + file + ".txt"
    print(filepath)
    nf = open(filepath,"w+")
    alp = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for char in alp:
        nf.write(char)

dr,file = eval(input("Enter Directory and path on C drive:"))
createfile(dr,file)


"""
if (result == '0'):
    print("File %s has been created successfull under directory %s"%(file,dir))
else:
    print("Unable to create File %s under directory %s" % (file, dir))
"""
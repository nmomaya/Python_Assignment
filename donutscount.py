def donut(count):
    if (count < 10):
        return(count)
    else:
        return("Many")

if __name__ == '__main__':
    count = donut(eval(input("Enter Number of Donuts")))
    print(type(count))
    print("No. of Donuts are: {}".format(count))
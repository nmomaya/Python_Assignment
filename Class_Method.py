""""
class Employee:
    name = []
    des = []
    no = eval(input("Enter no. of employee"))
    for i in range (0,no):
         ename = eval(input("Enter your name"))
         name.append(ename)
         edes = eval(input("Enter your designation"))
         des.append(edes)


em1 = Employee()

for x in range(0, len(em1.name)):
    print(em1.name[x]," -> ",em1.des[x])

"""

class emp:
     def empdetails(self):
        self.name = "Nimesh"

     def printemp(self):
        print(self.name)


eobj = emp()
eobj.printemp()










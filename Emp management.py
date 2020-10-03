import pickle
import os
import pathlib

class Emp:
    name = ''
    addemp= ''
    Id= 0

    def createEmp(self):
        self.Id = int(input("Enter a Id :"))
        self.name = input("Enter a name :")
        self.department = input("Enter a department :")
        self.salary = int(input("Enter a salary :"))
        print("\n\n\nEmp Added Succesfully")

    def showEmp(self):
        print("empId:",self.Id)
        print("empname:",self.name)
        print("empdepartment:",self.department)
        print("empsalary:",self.salary)

        
    def modifyEmp(self):
        print("Id Number : ",self.Id)
        self.name = input("Modify Emp Name :")
        self.department = input("Modify Department of Emp :")
        self.salary = int(input("Modify Salary :"))


    def report(self):
        print(self.Id, " ",self.name ," ",self.department," ", self.salary)
    
    

    def getEmpId(self):
        return self.Id
    def getEmpname(self):
        return self.name
    def getEmpdepartment(self):
        return self.type
    def getEmpsalary(self):
        return self.salary


def intro():
    print("\t\t\t\t**********************")
    print("\t\t\t\tEMP MANAGEMENT SYSTEM")
    print("\t\t\t\t**********************")


def writeEmp():
    acc = Emp()
    acc.createEmp()
    writeEmpFile(acc)


def displayAll():
    file = pathlib.Path("acc.data")
    if file.exists ():
        infile = open('acc.data','rb')
        mylist = pickle.load(infile)
        for item in mylist :
            print(item.Id," ", item.name, " ",item.department, " ",item.salary )
        infile.close()
    else :
        print("No records to display")
           
def displaySp(num): 
    file = pathlib.Path("acc.data")
    if file.exists ():
        infile = open('acc.data','rb')
        mylist = pickle.load(infile)
        infile.close()
        found = False
        for item in mylist :
            if item.Id == num :
                print("Emp Detail is = ",item.Id,item.name,item.department,item.salary)
                found = True
    else :
        print("No records to Search")
    if not found :
        print("No existing record with this Id")




def modifyEmp(num):
    file = pathlib.Path("acc.data")
    if file.exists ():
        infile = open('acc.data','rb')
        oldlist = pickle.load(infile)
        infile.close()
        os.remove('acc.data')
        for item in oldlist :
            if item.Id == num :
                item.name = input("Enter Emp name : ")
                item.department = input("Enter department: ")
                item.salary = int(input("Enter Salary : "))
        
        outfile = open('newacc.data','wb')
        pickle.dump(oldlist, outfile)
        outfile.close()
        os.rename('newacc.data', 'acc.data')




def deleteEmp(num):
    file = pathlib.Path("acc.data")
    if file.exists ():
        infile = open('acc.data','rb')
        oldlist = pickle.load(infile)
        infile.close()
        newlist = []
        for item in oldlist :
            if item.Id != num :
                newlist.append(item)
        os.remove('acc.data')
        outfile = open('newacc.data','wb')
        pickle.dump(newlist, outfile)
        outfile.close()
        os.rename('newacc.data', 'acc.data')


def writeEmpFile(acc) : 
    
    file = pathlib.Path("acc.data")
    if file.exists ():
        infile = open('acc.data','rb')
        oldlist = pickle.load(infile)
        oldlist.append(acc)
        infile.close()
        os.remove('acc.data')
    else :
        oldlist = [acc]
    outfile = open('newacc.data','wb')
    pickle.dump(oldlist, outfile)
    outfile.close()
    os.rename('newacc.data', 'acc.data')
    
        
# start of the program
ch=''
num=0
intro()

while ch != 6:

    print("\tMAIN MENU")
    print("\t1. ADD EMP")
    print("\t2. SHOW EMP")
    print("\t3. Dispaly EMP")
    print("\t4. Modify Emp")
    print("\t5. Delete EMP")
    print("\t6. EXIT")
    print("\tSelect Your Option (1-6) ")
    ch = input()
   
    
    if ch == '1':
        writeEmp()
    elif ch == '2':
        num = int(input("\tEnter The Id. : "))
        displaySp(num)
    elif ch == '3':
        displayAll();
    elif ch == '4':
        num =int(input("\tEnter The EmpId. : "))
        modifyEmp(num);
    elif ch == '5':
        num =int(input("\tEnter The EmpId. : "))
        deleteEmp(num);    
    elif ch == '6':
        print("\tThanks for using Emp managemnt system")
        break
    else :
        print("Invalid choice")
    
    ch = input("Enter your choice : ")
    


    

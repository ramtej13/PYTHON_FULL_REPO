#write a code for initialisung employee data and also giving salary using inheritance method 
# #note==={code 1---employee details like gender,name,id} 
# #code2-------salary for the same employee through inheritance #example==name:ram,gender:male,age:22,id=89,salary--2000000. 
# #pooja,female,22,98,200000

class Employee:
    def __init__(self,**kwargs):
        self._Data=kwargs
    def GetName(self):
        return self._Data["name"]
    def GetGender(self):
        return self._Data["gender"]
    def GetAge(self):
        return self._Data["age"]
    def GetId(self):
        return self._Data["id"]


class Salary(Employee):
    def GetSalary(self):
        return self._Data["salary"]

class EmployeeForm:
    def __init__(self,**kwargs):
        self._Data=kwargs
    def GetNameEmp(self):
        return self._Data["nameemp"]
    def GetGenderEmp(self):
        return self._Data["genderemp"]
    def GetAgeEmp(self):
        return self._Data["ageemp"]
    def GetIdEmp(self):
        return self._Data["idemp"]

class SalaryForm(EmployeeForm):
    def GetSalaryEmp(self):
        return self._Data["salaryemp"]

def main():
    FillingName = input("enter you name here")
    FillingGender = input("enter your gender")
    FillingAge = int(input("enter you salary"))
    FillingId =int(input("enter you Age"))
    FillingSalary =int(input("enter you ID"))
    DataPull.output(FillingName,FillingGender,FillingAge,FillingId,FillingSalary)

class DataPull:
    def output(self,FillingName,FillingGender,FillingAge,FillingId,FillingSalary):  #FillingName,FillingGender,FillingAge,FillingId,FillingSalary):
        # FillingName = input("enter you name here")
        # FillingGender = input("enter your gender")
        # FillingSalary = int(input("enter you salary"))
        # FillingAge = int(input("enter you Age"))
        # FillingId = int(input("enter you ID"))
        self._employeedetails = Salary(name=FillingName, gender=FillingGender, age=FillingAge, id=FillingId, salary=FillingSalary)
        id = self._employeedetails.GetId()
        name = self._employeedetails.GetName()
        gender = self._employeedetails.GetGender()
        age = self._employeedetails.GetAge()
        salary=self._employeedetails.GetSalary()
        self._employeedetailsform = SalaryForm(nameemp="Name", genderemp="Gender", ageemp="Age", idemp="ID", salaryemp="Salary")
        formname = self._employeedetailsform.GetNameEmp()
        formgender = self._employeedetailsform.GetGenderEmp()
        formage = self._employeedetailsform.GetAgeEmp()
        formid = self._employeedetailsform.GetIdEmp()
        formsalary = self._employeedetailsform.GetSalaryEmp()
        print("{} = {}\n{} = {}\n{} = {}\n{} = {}\n{} = {}".format(formname,name,formsalary,salary,formgender,gender,formage,age,formid,id))


if __name__ == '__main__':main()

















































# def input(self,name,gender,age,id,salary):
#     self._name = input("enter you name ")
#     self._gender = input("enter you id")
#     age = input("enter you age")
#     id = input("enter you id")
#     salary = input("enter you salary")







class Employee:
    def __init__(self, **kwargs):
        self._Data = kwargs

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
    def __init__(self, **kwargs):
        self._Data = kwargs

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


class main():
    FillingName = str(input("enter you name here"))
    FillingGender = str(input("enter your gender"))
    FillingAge = int(input("enter you salary"))
    FillingId = int(input("enter you Age"))
    FillingSalary = int(input("enter you ID"))
    employeedetails = Salary(name=FillingName, gender=FillingGender, age=FillingAge, id=FillingId,salary=FillingSalary)
    id = employeedetails.GetId()
    name = employeedetails.GetName()
    gender = employeedetails.GetGender()
    age = employeedetails.GetAge()
    salary = employeedetails.GetSalary()
    employeedetailsform = SalaryForm(nameemp="Name", genderemp="Gender", ageemp="Age", idemp="ID",salaryemp="Salary")
    formname = employeedetailsform.GetNameEmp()
    formgender = employeedetailsform.GetGenderEmp()
    formage = employeedetailsform.GetAgeEmp()
    formid = employeedetailsform.GetIdEmp()
    formsalary = employeedetailsform.GetSalaryEmp()
    print("{} = {}\n{} = {}\n{} = {}\n{} = {}\n{} = {}".format(formname, name, formsalary, salary, formgender, gender,
                                                               formage, age, formid, id))

if __name__ == '__main__':main()

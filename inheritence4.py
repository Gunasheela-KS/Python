class Employee:

    raise_amount = 1.04
    total_num_employees=0
    def __init__(self,firstName,lastName,salary):
        self.firstName=firstName
        self.lastName=lastName
        self.salary=salary
        self.email=self.firstName + '.' + self.lastName + "@gmail.com"

        Employee.total_num_employees += 1

    def full_name(self):
        return self.firstName + ' ' + self.lastName

    def emp_raise(self):
        #self.salary += self.salary * Employee.raise_amount # Use this when the raise is same for all employees
        self.salary += self.salary * self.raise_amount     # Use this when the raise amount is different for different employees

class Developer(Employee):
    raise_amount=1.10

    def __init__(self,firstName,lastName,salary,prog_lang):
        super().__init__(firstName,lastName,salary)
        self.prog_lang=prog_lang



class Manager(Employee):
    raise_amount=1.20
    def __init__(self, firstName, lastName, salary,employees=None):
        super().__init__(firstName, lastName, salary)
        if employees is None:
            self.employees=[]
        else:
            self.employees=employees

    def add_employee(self,emp):
        if emp not in self.employees :
            self.employees.append(emp)

    def remove_employee(self,emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def list_employees(self):
        for emp in self.employees:
            print(f'--> {emp.full_name()}')


dev_1=Developer('Gunasheela','Shivanna',50000,'Python')
dev_2=Developer('Siri','Shivanna',50000,'Java')

man_1=Manager('Vinay','kumar',60000,[dev_1])

# print(man_1.email)
# print(man_1.list_employees())
#
# man_1.add_employee(dev_2)
# print(man_1.list_employees())
#
# man_1.remove_employee(dev_1)
# print(man_1.list_employees())

## isinstance, issubclass

print(isinstance(dev_2,Employee))
print(isinstance(dev_2,Manager))

print(issubclass(Manager,Developer))
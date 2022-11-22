# Inheritence allows us to inherit attributes and methods from the parent class
# It is useful because we can create the subclasses with all the functionalities of the parent class, can add new functinalities
# all without affecting the parent class

# Employee base class
# Developer subclass, manager subclass

# Employee class already has attributes like name, email,salary, we can inherit those functionalities from Employee class instead of re writing the same thing again

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
        return self.firstName + self.lastName

    def emp_raise(self):
        #self.salary += self.salary * Employee.raise_amount # Use this when the raise is same for all employees
        self.salary += self.salary * self.raise_amount     # Use this when the raise amount is different for different employees


class Developer(Employee):
    pass

dev_1=Developer('Gunasheela','Shivanna',50000)
dev_2=Developer('Siri','Vinay',50000)

# print(dev_1.email)
# print(dev_2.email)

# printing the help on the class gives you method resolution order--> First it looks for attributes in the developer class then the employee class then builtin
# objetc class
print(help(Developer))
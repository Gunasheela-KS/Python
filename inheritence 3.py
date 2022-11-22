# Adding new variables in the subclass

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
    raise_amount=1.10

    def __init__(self,firstName,lastName,salary,prog_lang):
        super().__init__(firstName,lastName,salary)
        self.prog_lang=prog_lang



dev_1=Developer('Gunasheela','Shivanna',50000,'Python')

print(dev_1.raise_amount)
print(dev_1.full_name())
print(dev_1.prog_lang)
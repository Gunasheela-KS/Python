# class variables are variables which are shared between all instances of the class
# instance variables are the unique values for that particular instance

#raise_amount and total_num_employees are class variable
#raise_amount is shared across different instances of the same class but we can assign diffferent raise using self.raise_amount
# total_num_employees is shared across different instances of the same class but the value is same foe all the instances
#Employee.total_num_employees

# class Employee:
#
#     raise_amount = 4/100
#
#     def __init__(self,firstName,lastName,salary):
#         self.firstName=firstName
#         self.lastName=lastName
#         self.salary=salary
#         self.email=self.firstName + '.' + self.lastName + "@gmail.com"
#
#     def full_name(self):
#         return self.firstName + self.lastName
#
#     def emp_raise(self):
#         self.salary += self.salary * Employee.raise_amount # Use this when the raise is same for all employees
#         #self.salary += self.salary * self.raise_amount
#         #self.salary += self.salary * raise_amount # you will get name error
#
#
# emp_1=Employee("gunasheela","shivanna",50000)
# emp_2=Employee("Siri","vinay",100)
#
# print(emp_1.salary)
# print(emp_2.salary)
#
# emp_1.emp_raise()
# print(emp_1.salary)


# class Employee:
#
#     raise_amount = 4/100
#
#     def __init__(self,firstName,lastName,salary):
#         self.firstName=firstName
#         self.lastName=lastName
#         self.salary=salary
#         self.email=self.firstName + '.' + self.lastName + "@gmail.com"
#
#     def full_name(self):
#         return self.firstName + self.lastName
#
#     def emp_raise(self):
#         #self.salary += self.salary * Employee.raise_amount # Use this when the raise is same for all employees
#         self.salary += self.salary * self.raise_amount     # Use this when the raise amount is different for different employees
#         #self.salary += self.salary * raise_amount
#
#
# emp_1=Employee("gunasheela","shivanna",50000)
# emp_2=Employee("Siri","vinay",50000)
#
# emp_1.raise_amount=10/100
# emp_2.raise_amount=20/100
#
# print(emp_1.salary)
# print(emp_2.salary)
#
# emp_1.emp_raise()
# emp_2.emp_raise()
# print(emp_1.salary)
# print(emp_2.salary)

class Employee:

    raise_amount = 4/100
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


emp_1=Employee("gunasheela","shivanna",50000)
emp_2=Employee("Siri","vinay",50000)

emp_1.raise_amount=10/100
emp_2.raise_amount=20/100

print(emp_1.salary)
print(emp_2.salary)

emp_1.emp_raise()
emp_2.emp_raise()
print(emp_1.salary)
print(emp_2.salary)

print(emp_1.total_num_employees)
print(emp_2.total_num_employees)
print(Employee.total_num_employees)
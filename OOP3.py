# Regular methods
# class methods
# static methods

# Regular methods in class automatically takes in instance variable (self) as a first argument
# As a standard practice we denote this as self

# Class methods takes in first argument as class variable instead of instance variable as first argument
# How to create--> add decorator to the regular method to make it as class method
# @classmethod

# static methods don't pass anything automatically, they behave just like normal methods


# class Employee:
#
#     raise_amount = 1.04
#     total_num_employees=0
#     def __init__(self,firstName,lastName,salary):
#         self.firstName=firstName
#         self.lastName=lastName
#         self.salary=salary
#         self.email=self.firstName + '.' + self.lastName + "@gmail.com"
#
#         Employee.total_num_employees += 1
#
#     def full_name(self):
#         return self.firstName + self.lastName
#
#     def emp_raise(self):
#         #self.salary += self.salary * Employee.raise_amount # Use this when the raise is same for all employees
#         self.salary += self.salary * self.raise_amount     # Use this when the raise amount is different for different employees
#
#     @classmethod
#     def set_raise_amount(cls,amount):
#         cls.raise_amount= amount
#
# emp_1=Employee('Gunasheela','Shivanna',50000)
# emp_2=Employee('Siri','Vinay',50000)
#
# print(emp_1.raise_amount)
#
# Employee.set_raise_amount(1.05)
#
# print(emp_1.raise_amount)
#
# print(emp_2.raise_amount)


# class Employee:
#
#     raise_amount = 1.04
#     total_num_employees=0
#     def __init__(self,firstName,lastName,salary):
#         self.firstName=firstName
#         self.lastName=lastName
#         self.salary=salary
#         self.email=self.firstName + '.' + self.lastName + "@gmail.com"
#
#         Employee.total_num_employees += 1
#
#     def full_name(self):
#         return self.firstName + self.lastName
#
#     def emp_raise(self):
#         #self.salary += self.salary * Employee.raise_amount # Use this when the raise is same for all employees
#         self.salary += self.salary * self.raise_amount     # Use this when the raise amount is different for different employees
#
#     @classmethod
#     def set_raise_amount(cls,amount):
#         cls.raise_amount= amount
#
# # How to use class method as alternative constructor
#     @classmethod
#     def from_string(cls,emp_str):
#         first,last,salary=emp_str.split('-')
#         return cls(first,last,salary)
#
# # emp_1=Employee('Gunasheela','Shivanna',50000)
# # emp_2=Employee('Siri','Vinay',50000)
#
# emp_1=Employee.from_string('Gunasheela-Shivanna-50000')
#
# print(emp_1.salary)

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

    @classmethod
    def set_raise_amount(cls,amount):
        cls.raise_amount= amount

# How to use class method as alternative constructor
    @classmethod
    def from_string(cls,emp_str):
        first,last,salary=emp_str.split('-')
        return cls(first,last,salary)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


import datetime

day=datetime.date(2022,12,10)
print(Employee.is_workday(day))





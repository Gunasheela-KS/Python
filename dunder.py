# These are some special methods we can use in our class
# Helps to emulate builtin behaviour in python
# used to implement operator overloading

# it is adding two numbers when two integers
# it is concatenating when two strings are used
# Depending on what objects you are using the addition has different behaviour
# print(2+3)
# print('a'+'b')


# It would be nice when we print out the object-- we see something useful rather than <__main__.Employee object at 0x7fe5a98a4208>
# These special methods allows us to do that

# By defining our own special methods we will be able to change this builtin behaviour

# These special methods are sorrounded by __

# Two special methods that we need to always implement are
# __repr__
# Unambiguous representation of object used for debugging,logging etc..read by other developers
# __str__
# Readable representation of object--display to the end user

# class Employee:
#     pass
# emp_1=Employee()
# print(emp_1)


# class Employee:
#     def __init__(self,firstName,lastName,salary):
#         self.firstName=firstName
#         self.lastName=lastName
#         self.salary=salary
#         self.email=self.firstName + '.' + self.lastName + "@gmail.com"
#
#     def full_name(self):
#         return self.firstName + ' ' + self.lastName
#
#     def __repr__(self):
#         # Developer can look at it and understand what arguments are needed to recreate the object
#         return f'Employee {self.firstName,self.lastName,self.salary}'
#
#     def __str__(self):
#         # this is for the end user to see when they print out the object
#         return f'Employee-{self.full_name()},{self.email}'
#
#
# emp_1=Employee("gunasheela",'shivanna',50000)
# print(emp_1)
#
# print(repr(emp_1))
# print(str(emp_1))
#
# print(Employee.__repr__(emp_1))
# print(Employee.__str__(emp_1))


## operators overloading

# print(str.__add__('1','2'))
# print(int.__add__(1,2))

class Employee:
    def __init__(self,firstName,lastName,salary):
        self.firstName=firstName
        self.lastName=lastName
        self.salary=salary
        self.email=self.firstName + '.' + self.lastName + "@gmail.com"

    def full_name(self):
        return self.firstName + ' ' + self.lastName

    def __repr__(self):
        # Developer can look at it and understand what arguments are needed to recreate the object
        return f'Employee {self.firstName,self.lastName,self.salary}'

    def __str__(self):
        # this is for the end user to see when they print out the object
        return f'Employee-{self.full_name()},{self.email}'

    def __add__(self, other):
        return self.salary + other.salary

    def __len__(self):
        return len(self.full_name())


emp_1=Employee("gunasheela",'shivanna',50000)
emp_2=Employee('Siri','Vinay',50000)

# print(emp_1+emp_2)

# print(len('Test'))
# print('Test'.__len__())

print(len(emp_2))


























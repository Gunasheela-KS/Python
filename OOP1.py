# class is a blueprint to create instances
# instance variables are unique to each instance of the class
# self is a instance variable, name of the instance will be passed each time you create an object
#

# class Employee:
#     pass
#
# emp_1=Employee()
# emp_2=Employee()
#
# print(emp_1)
# print(emp_2)

# class Employee:
#     pass
#
# emp_1=Employee()
# emp_2=Employee()
#
# emp_1.firstName="gunasheela"
# emp_1.lastName="shivanna"
# emp_1.email= emp_1.firstName + "." + emp_1.lastName + "@gmail.com"
#
# emp_2.firstName="siri"
# emp_2.lastName="vinay"
# emp_2.email= emp_2.firstName + "." + emp_2.lastName + "@gmail.com"
#
# print(emp_1.firstName)
# print(emp_2.firstName)
# print(emp_2.email)


class Employee:
    def __init__(self,firstName,lastName,salary):
        self.firstName=firstName
        self.lastName=lastName
        self.salary=salary
        self.email=self.firstName + '.' + self.lastName + "@gmail.com"

    def full_name(self):
        return self.firstName + self.lastName


emp_1=Employee("gunasheela","shivanna",50000)
emp_2=Employee("Siri","vinay",100)

#Way 1:
# print(emp_1.full_name())
# print(emp_2.full_name())

#Way 2: classname.method_name(instance name)
print(Employee.full_name(emp_1))
print(Employee.full_name(emp_2))
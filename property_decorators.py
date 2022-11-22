
# Property decorators allows us to create methods which can be used as attributes.

# class Employee:
#     def __init__(self,firstName,lastName):
#         self.firstName=firstName
#         self.lastName=lastName
#         self.email=self.firstName + '.' + self.lastName + "@gmail.com"
#
#     def full_name(self):
#         return self.firstName + ' ' + self.lastName
#
# emp_1=Employee('gunasheela','shivanna')
#
# print(emp_1.firstName)
# print(emp_1.email)
# print(emp_1.full_name())

# class Employee:
#     def __init__(self,firstName,lastName):
#         self.firstName=firstName
#         self.lastName=lastName
#         self.email=self.firstName + '.' + self.lastName + "@gmail.com"
#
#     def full_name(self):
#         return self.firstName + ' ' + self.lastName
#
# emp_1=Employee('gunasheela','shivanna')
#
# # observe email has not changed, but full_name has changed correctly, because everytime it is called it will make use of recent value
# emp_1.firstName='siri'
# print(emp_1.firstName)
# print(emp_1.email)
# print(emp_1.full_name())


# class Employee:
#     def __init__(self,firstName,lastName):
#         self.firstName=firstName
#         self.lastName=lastName
#
#
#     def email(self):
#         return self.firstName + '.' + self.lastName + "@gmail.com"
#
#     def full_name(self):
#         return self.firstName + ' ' + self.lastName
#
# emp_1=Employee('gunasheela','shivanna')
#
#
# emp_1.firstName='siri'
# print(emp_1.firstName)
# print(emp_1.email())
# print(emp_1.full_name())


class Employee:
    def __init__(self,firstName,lastName):
        self.firstName=firstName
        self.lastName=lastName

    @property
    def email(self):
        return self.firstName + '.' + self.lastName + "@gmail.com"

    @property
    def full_name(self):
        return self.firstName + ' ' + self.lastName

emp_1=Employee('gunasheela','shivanna')


emp_1.firstName='siri'
print(emp_1.firstName)
print(emp_1.email)
print(emp_1.full_name)
# Setters - define the same method with @methodname.setter decorator


# class Employee:
#     def __init__(self,firstName,lastName):
#         self.firstName=firstName
#         self.lastName=lastName
#
#     @property
#     def email(self):
#         return self.firstName + '.' + self.lastName + "@gmail.com"
#
#     @property
#     def full_name(self):
#         return self.firstName + ' ' + self.lastName
#
#
# emp_1=Employee('gunasheela','shivanna')
#
# # can't set attribute error
# emp_1.full_name='siri sampige'
# print(emp_1.firstName)
# print(emp_1.email)
# print(emp_1.full_name)


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

    @full_name.setter
    def full_name(self,name):
        first,last=name.split(' ')
        self.firstName=first
        self.lastName=last

emp_1=Employee('gunasheela','shivanna')

# can't set attribute error
emp_1.full_name='siri sampige'
print(emp_1.firstName)
print(emp_1.email)
print(emp_1.full_name)
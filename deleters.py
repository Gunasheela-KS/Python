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

    @full_name.deleter
    def full_name(self):
        print('Deleting Name')
        self.firstName = None
        self.lastName = None

emp_1=Employee('gunasheela','shivanna')


emp_1.full_name='siri sampige'
print(emp_1.firstName)
print(emp_1.full_name)

del emp_1.full_name

print(emp_1.firstName)
print(emp_1.lastName)


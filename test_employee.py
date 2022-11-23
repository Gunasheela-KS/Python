import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    def test_fullname(self):
        emp_1=Employee('gunasheela','shivanna',50000)
        emp_2=Employee('siri','vinay',60000)

        self.assertEqual(emp_1.fullname,'gunasheela shivanna')
        self.assertEqual(emp_2.fullname, 'siri vinay')


    def test_email(self):
        emp_1 = Employee('gunasheela', 'shivanna', 50000)
        emp_2 = Employee('siri', 'vinay', 60000)

        self.assertEqual(emp_1.email, 'gunasheela.shivanna@gmail.com')
        self.assertEqual(emp_2.email, 'siri.vinay@gmail.com')

    def test_apply_raise(self):
        emp_1 = Employee('gunasheela', 'shivanna', 50000)
        emp_2 = Employee('siri', 'vinay', 60000)

        self.assertEqual(emp_1.apply_raise(), 52500)
        self.assertEqual(emp_2.apply_raise(), 63000)





if __name__ == '__main__':
    unittest.main()

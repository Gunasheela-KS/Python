# use setup method when there is a repeating code before each test
# setup method is run before every test

# add self. as these are instance variables now everywhere

# Use tear down method when cleanup is required after the test
# tear down method is run after every test


import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):

    def setUp(self):
        self.emp_1 = Employee('gunasheela', 'shivanna', 50000)
        self.emp_2 = Employee('siri', 'vinay', 60000)

    def tearDown(self):
        pass

    def test_fullname(self):
        self.assertEqual(self.emp_1.fullname,'gunasheela shivanna')
        self.assertEqual(self.emp_2.fullname, 'siri vinay')

        self.emp_1.first='tara'
        self.emp_2.first = 'sowmya'

        self.assertEqual(self.emp_1.fullname,'tara shivanna')
        self.assertEqual(self.emp_2.fullname, 'sowmya vinay')


    def test_email(self):
        self.assertEqual(self.emp_1.email, 'gunasheela.shivanna@gmail.com')
        self.assertEqual(self.emp_2.email, 'siri.vinay@gmail.com')

        self.emp_1.first = 'tara'
        self.emp_2.first = 'sowmya'

        self.assertEqual(self.emp_1.email, 'tara.shivanna@gmail.com')
        self.assertEqual(self.emp_2.email, 'sowmya.vinay@gmail.com')

    def test_apply_raise(self):
        self.assertEqual(self.emp_1.apply_raise(), 52500)
        self.assertEqual(self.emp_2.apply_raise(), 63000)



if __name__ == '__main__':
    unittest.main()


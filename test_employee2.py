# Tests will not get executed in the same order you have written them
# setUp method is executed before each test
# tearDown method is executed after each test

# setUpClass method is executed before everything once
# tearDownClass method gets executed after everything once


#########################################################Best Practices###################################################
# 1. Tests should be isolated (One test should not have any dependency on the other test)
# 2. Test driven development

import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('setupClass method')

    @classmethod
    def tearDownClass(cls):
        print('tearDownClass method')

    def setUp(self):
        print('Setup method')
        self.emp_1 = Employee('gunasheela', 'shivanna', 50000)
        self.emp_2 = Employee('siri', 'vinay', 60000)

    def tearDown(self):
        print('tearDown method')

    def test_fullname(self):
        print('test fullname')
        self.assertEqual(self.emp_1.fullname,'gunasheela shivanna')
        self.assertEqual(self.emp_2.fullname, 'siri vinay')

        self.emp_1.first='tara'
        self.emp_2.first = 'sowmya'

        self.assertEqual(self.emp_1.fullname,'tara shivanna')
        self.assertEqual(self.emp_2.fullname, 'sowmya vinay')


    def test_email(self):
        print('test email')
        self.assertEqual(self.emp_1.email, 'gunasheela.shivanna@gmail.com')
        self.assertEqual(self.emp_2.email, 'siri.vinay@gmail.com')

        self.emp_1.first = 'tara'
        self.emp_2.first = 'sowmya'

        self.assertEqual(self.emp_1.email, 'tara.shivanna@gmail.com')
        self.assertEqual(self.emp_2.email, 'sowmya.vinay@gmail.com')

    def test_apply_raise(self):
        print('test apply raise')
        self.assertEqual(self.emp_1.apply_raise(), 52500)
        self.assertEqual(self.emp_2.apply_raise(), 63000)



if __name__ == '__main__':
    unittest.main()



# Lets say in your code, you are making a call to a website
# If the website is down, your tests will also fail--> This is not desirable
# We want our code to fail only when there is something wrong in our code only
# To get around this problem, we use mocking


import unittest
import requests
from unittest.mock import patch
# patch can be used as decorator or context manager
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

    def test_monthly_schedule(self):
        with patch('employee.requests.get') as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = 'Success'

            schedule=self.emp_1.monthly_schedule('May')
            mocked_get.assert_called_with('http://company.com/shivanna/May')
            self.assertEqual(schedule,'Success')

            mocked_get.return_value.ok = False

            schedule = self.emp_2.monthly_schedule('June')
            mocked_get.assert_called_with('http://company.com/vinay/June')
            self.assertEqual(schedule, 'Bad Response!')




if __name__ == '__main__':
    unittest.main()

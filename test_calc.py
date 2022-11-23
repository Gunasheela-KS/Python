# Let's say you made some updates in your project code, if it impacts other section your project code.
# It is easy to understand which part of the code is not working using unit tests

# method name start with test_
# file name starts with test_
# python -m unittest test_calc.py
# If you detect some bug while fixing the code, it is a good practice to add that as a test case


import unittest
import calc

class TestCalc(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calc.add(10,6), 16)
        self.assertEqual(calc.add(10, -1), 9)
        self.assertEqual(calc.add(-3, -2), -5)

    def test_sun(self):
        self.assertEqual(calc.sub(2,3),-1)
        self.assertEqual(calc.sub(-2, 3), -5)
        self.assertEqual(calc.sub(0, 3), -3)

    def test_mul(self):
        self.assertEqual(calc.mul(2,0),0)
        self.assertEqual(calc.mul(2, -1), -2)
        self.assertEqual(calc.mul(-20, -2), 40)

    def test_div(self):
        self.assertEqual(calc.div(2,1),2)
        self.assertEqual(calc.div(5, 2), 2.5)
        self.assertEqual(calc.div(0, 1), 0)
        # way 1
        #self.assertRaises(ValueError,calc.div,10,0)
        # way 2 context manager
        with self.assertRaises(ValueError):
            calc.div(10,0)



if __name__ == '__main__':
    unittest.main()

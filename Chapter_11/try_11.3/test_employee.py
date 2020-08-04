#Done by Carlos Amaral in 18/07/2020


"""
Write a class called Employee . The __init__() method should
take in a first name, a last name, and an annual salary, and store each of these
as attributes. Write a method called give_raise() that adds $5,000 to the
annual salary by default but also accepts a different raise amount.
Write a test case for Employee . Write two test methods, test_give_default
_raise() and test_give_custom_raise() . Use the setUp() method so you don’t
have to create a new employee instance in each test method. Run your test
case, and make sure both tests pass.
"""

import unittest

from Employee import A_Employee

class TestEmployee(unittest.TestCase):
    """Tests for the class Employee."""

    def setUp(self):

        self.carlos = A_Employee('carlos', 'amaral', 50_000)

    def test_give_default_raise(self):
        self.carlos.give_raise()
        self.assertEqual(self.carlos.annual_salary, 55000)

    def test_give_custom_raie(self):
        self.carlos.give_raise(4000)
        self.assertEqual(self.carlos.annual_salary, 54000)

if __name__ == '__main__':
    unittest.main()
                
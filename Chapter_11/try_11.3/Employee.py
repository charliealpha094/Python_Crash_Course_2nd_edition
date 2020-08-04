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

class A_Employee():
    """Collects information about an employee."""

    def __init__(self, first_name, last_name, annual_salary):
        """Store the employee's attributes."""
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = annual_salary

    def get_descriptive_employee(self):
        employee = f"{self.first_name} {self.last_name} {self.annual_salary}"
        return employee

    def give_raise(self, amount=5000):
        self.annual_salary += amount      
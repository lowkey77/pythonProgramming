import unittest
from employee import Employee


class TestEmployee(unittest.TestCase):
    """Test for class Employee.py"""

    def setUp(self) -> None:
        self.john = Employee("John", "Doe", 10000)
        self.jane = Employee("Jane", "Doe", 10000)

    def test_give_default_raise(self):
        self.john.give_raise()
        self.assertEqual(self.john.salary, 15000)

    def test_give_custom_raise(self):
        self.jane.give_raise(10000)
        self.assertEqual(self.jane.salary, 20000)


if __name__ == "__main__":
    unittest.main()

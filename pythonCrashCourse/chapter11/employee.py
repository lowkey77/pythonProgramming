class Employee:
    """Employee class"""
    def __init__(self, first, last, salary):
        self.first = first
        self.last = last
        self.salary = salary

    def give_raise(self, increase=5000):
        self.salary += increase

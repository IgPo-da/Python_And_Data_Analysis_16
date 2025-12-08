import datetime

class Employee:

    number_of_employees = 0
    raise_amount = 1.04
    
    def __init__(self, first: str, last: str, salary: float):
        self.first = first
        self.last = last
        self.salary = salary
        Employee.number_of_employees += 1


    def full_name(self):
        return  f'{self.first} {self.last}'
    
    def email(self):
        return f'{self.first.lower()}.{self.last.lower()}@company.com'

    def raise_salary(self):
        self.salary = self.salary * Employee.raise_amount

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount
    
    @classmethod
    def from_string(cls, emp_string):
        first, last, salary = emp_string.split('-')
        return cls(first.title(), last.title(), salary)
    
    @staticmethod
    def is_workday():
        if datetime.datetime.now().weekday() in [5, 6]:
            return False
        return True


emp1 = Employee('Jack', 'Smith', 2000.0)
emp2 = Employee('Mary', 'Gold', 3000.0)

emp_string = 'BOB-SUMMERS-2400'
emp3 = Employee.from_string(emp_string)

print(Employee.is_workday())
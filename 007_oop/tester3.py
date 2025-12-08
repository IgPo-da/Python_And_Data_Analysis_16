class Employee:

    def __init__(self, first: str, last: str, salary: float):
        self.first = first
        self.last = last
        self.salary = salary

    @property
    def full_name(self):
        return  f'{self.first} {self.last}'
    
    @full_name.setter
    def full_name(self, name):
        first, last = name.split()
        self.first = first
        self.last = last

    @full_name.deleter
    def full_name(self):
        self.first = ''
        self.last = ''
    
    @property
    def email(self):
        return f'{self.first.lower()}.{self.last.lower()}@company.com'
    
    def __str__(self):
        return self.full_name

    def __repr__(self):
        return f'Employee{self.first, self.last, self.salary}'
    
    def __add__(self, other):
        return self.salary + other.salary


emp1 = Employee('Jack', 'Smith', 2000.0)
emp2 = Employee('Mary', 'Gold', 3000.0)

emp1.full_name = 'Bob Summers'
del emp1.full_name
print(emp1.full_name)
print(emp1.email)
print(emp1.first, emp1.last)

class Employee:

    raise_amount = 1.04
    
    def __init__(self, first: str, last: str, salary: float):
        self.first = first
        self.last = last
        self.salary = salary

    def full_name(self):
        return  f'{self.first} {self.last}'
    
    def email(self):
        return f'{self.first.lower()}.{self.last.lower()}@company.com'

    def raise_salary(self):
        self.salary = self.salary * Employee.raise_amount


class Developer(Employee):

    def __init__(self, first: str, last: str, salary: float, prog_lang: str):
        super().__init__(first, last, salary)
        # Employee.__init__(self, first, last, salary)
        self.prog_lang = prog_lang

    def write_code(self):
        print(f'{self.full_name()} writes code in {self.prog_lang}!')


class Manager(Employee):

    def __init__(self, first: str, last: str, salary: float, employees: list[object] = []):
        super().__init__(first, last, salary)
        self.employees = employees

    def list_employees(self):
        if self.employees:
                
            for employee in self.employees:
                print(employee.full_name())
        else:
            print(f'There are no employees set for {self.full_name()}')

    def add_employee(self, employee):
        if employee not in self.employees:
            self.employees.append(employee)

    def remove_employee(self, employee):
        if employee in self.employees:
            self.employees.remove(employee)

emp1 = Employee('Jack', 'Smith', 2000.0)
dev1 = Developer('Mary', 'Gold', 3000.0, 'Python')
man1 = Manager('Sarah', 'Summers', 5000.0)

man1.list_employees()
man1.add_employee(dev1)
man1.list_employees()
man1.remove_employee(dev1)
man1.list_employees()

print(isinstance(man1, Developer))

print(issubclass(Manager, Employee))


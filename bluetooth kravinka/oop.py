class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

class Branch:
    def __init__(self, name):
        self.name = name
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def remove_employee(self, employee):
        self.employees.remove(employee)

class Position:
    def __init__(self, name):
        self.name = name

class Company:
    def __init__(self):
        self.branches = []
        self.positions = []

    def add_branch(self, branch):
        self.branches.append(branch)

    def remove_branch(self, branch):
        self.branches.remove(branch)

    def add_position(self, position):
        self.positions.append(position)

    def remove_position(self, position):
        self.positions.remove(position)

    def get_employees_by_branch(self, branch_name):
        for branch in self.branches:
            if branch.name == branch_name:
                return branch.employees
        return []

    def get_employees_by_position(self, position_name):
        employees = []
        for branch in self.branches:
            for employee in branch.employees:
                if employee.position.name == position_name:
                    employees.append(employee)
        return employees

    def get_branches(self):
        return [branch.name for branch in self.branches]

    def get_positions(self):
        return [position.name for position in self.positions]

# Vytvoření zaměstnanců
employee1 = Employee("John Doe", Position("Manager"))
employee2 = Employee("Jane Smith", Position("Developer"))

# Vytvoření poboček
branch1 = Branch("Branch A")
branch2 = Branch("Branch B")

# Přidání zaměstnanců do poboček
branch1.add_employee(employee1)
branch2.add_employee(employee2)

# Vytvoření společnosti
company = Company()

# Přidání poboček a pozic do společnosti
company.add_branch(branch1)
company.add_branch(branch2)
company.add_position(Position("Manager"))
company.add_position(Position("Developer"))

# Zobrazení zaměstnanců pobočky
print(company.get_employees_by_branch("Branch A"))

# Zobrazení zaměstnanců pozice
print(company.get_employees_by_position("Manager"))

# Zobrazení seznamu poboček
print(company.get_branches())

# Zobrazení seznamu pracovních pozic
print(company.get_positions())

# Odebrání pobočky
company.remove_branch(branch1)

# Odebrání zaměstnance
branch2.remove_employee(employee2)
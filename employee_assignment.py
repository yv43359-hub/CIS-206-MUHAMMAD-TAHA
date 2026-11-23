# Base class: Employee

class Employee:
    def __init__(self, name, employee_id, salary):
        self.name = name
        self.employee_id = employee_id
        self.salary = salary

    def display_info(self):
        print("Employee Information")
        print("Name:", self.name)
        print("Employee ID:", self.employee_id)
        print("Salary: $", self.salary)


# Inherited class: Manager

class Manager(Employee):
    def __init__(self, name, employee_id, salary, department):
        super().__init__(name, employee_id, salary)
        self.department = department

    # Overriding the base class method
    def display_info(self):
        print("Manager Information")
        print("Name:", self.name)
        print("Employee ID:", self.employee_id)
        print("Salary: $", self.salary)
        print("Department:", self.department)

    # New method added to the inherited class
    def calculate_bonus(self):
        bonus = self.salary * 0.10
        print("Annual Bonus: $", bonus)


# Test the classes

if __name__ == "__main__":
    manager1 = Manager("Muhammad Taha", 101, 60000, "IT")

    manager1.display_info()
    manager1.calculate_bonus()
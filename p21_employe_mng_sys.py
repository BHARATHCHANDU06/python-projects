class Employee:

    def __init__(self, id, name, department, salary):
        self.id = id
        self.name = name
        self.department = department
        self.salary = salary
    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}, Department: {self.department}, Salary: {self.salary}"
class EmployeeManagement:
    def __init__(self):
        self.employees = []
    def add_employee(self, id, name, department, salary):
        employee = Employee(id, name, department, salary)
        self.employees.append(employee)
        print("Employee added successfully!")
    def view_employees(self):
        if not self.employees:
            print("No employees found!")
        else:
            for employee in self.employees:
                print(employee)
    def search_employee(self, id):
        for employee in self.employees:
            if employee.id == id:
                return employee
        return None
    def update_employee(self, id, name, department, salary):
        employee = self.search_employee(id)
        if employee:
            employee.name = name
            employee.department = department
            employee.salary = salary
            print("Employee updated successfully!")
        else:
            print("Employee not found!")
    def delete_employee(self, id):
        employee = self.search_employee(id)
        if employee:
            self.employees.remove(employee)
            print("Employee deleted successfully!")
        else:
            print("Employee not found!")
system = EmployeeManagement()
system.add_employee(101, "Chandu", "IT", 30000)
system.add_employee(102, "Rahul", "HR", 25000)
system.view_employees()
while True:
    print("1. Add Employee")
    print("2. View Employees")
    print("3. Search Employee")
    print("4. Update Employee")
    print("5. Delete Employee")
    print("6. Exit")
    choice = int(input("Enter your choice (1-6): "))
    if choice == 1:
        id = int(input("Enter Employee ID: "))
        name = input("Enter Employee Name: ")
        department = input("Enter Employee Department: ")
        salary = float(input("Enter Employee Salary: "))
        system.add_employee(id, name, department, salary)
    elif choice == 2:
        system.view_employees()
    elif choice == 3:
        id = int(input("Enter Employee ID to search: "))
        employee = system.search_employee(id)
        if employee:
            print(employee)
        else:
            print("Employee not found!")
    elif choice == 4:
        id = int(input("Enter Employee ID to update: "))
        name = input("Enter new Employee Name: ")
        department = input("Enter new Employee Department: ")
        salary = float(input("Enter new Employee Salary: "))
        system.update_employee(id, name, department, salary)
    elif choice == 5:
        id = int(input("Enter Employee ID to delete: "))
        system.delete_employee(id)
    elif choice == 6:
        print("Exiting the program...")
        break
    else:
        print("Invalid choice! Please try again.")
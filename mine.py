from models.developer import Developer
from models.designer import Designer
from models.manager import Manager
from models.department import Department

def main():
    # Create some Developer and Designer objects
    dev1 = Developer("John", "Doe", 1000, 3)
    dev2 = Developer("Alice", "Johnson", 1100, 6)
    designer1 = Designer("Jane", "Smith", 1200, 4, 0.9)
    designer2 = Designer("Emily", "Davis", 1300, 7, 0.85)

    # Create a Manager and assign a team
    manager1 = Manager("Bob", "Brown", 2000, 6, [dev1, designer1])
    manager2 = Manager("Charlie", "Wilson", 2500, 8, [dev2, designer2])

    # Create a Department and add managers
    department = Department()
    department.add_manager(manager1)
    department.add_manager(manager2)

    # Calculate and print salaries for all employees in the department
    department.give_salary()

    # Save employees to a JSON file
    department.save_employees("data/employees.json")

    # Load employees from a JSON file (if exists)
    department.load_employees("data/employees.json")

if __name__ == "__main__":
    main()

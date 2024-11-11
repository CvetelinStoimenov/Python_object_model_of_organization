import json
from .manager import Manager
from .designer import Designer
from .developer import Developer

class Department:
    def __init__(self):
        self.managers = []

    def add_manager(self, manager: Manager):
        self.managers.append(manager)

    def give_salary(self):
        for manager in self.managers:
            print(f"{manager.first_name} {manager.last_name} received {round(manager.calculate_salary())} money.")
            for member in manager.team:
                print(f"{member.first_name} {member.last_name} received {round(member.calculate_salary())} money.")

    def save_employees(self, filename):
        try:
            with open(filename, 'w') as file:
                json.dump([manager.to_dict() for manager in self.managers], file, indent=4)
        except Exception as e:
            print(f"Error saving employees: {e}")

    def load_employees(self, filename):
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
                for manager_data in data:
                    team = []
                    for member_data in manager_data['team']:
                        if 'eff_coeff' in member_data:  # This is a Designer
                            team.append(Designer(**member_data))
                        else:  # This is either Developer or Manager
                            if 'team' in member_data:  # This should be a Manager
                                team.append(Manager(**member_data))
                            else:  # This should be a Developer
                                team.append(Developer(**member_data))

                    manager = Manager(**manager_data)  # Create the manager
                    self.add_manager(manager)  # Add the manager with its team to the department
        except FileNotFoundError:
            print(f"Error loading employees: File '{filename}' not found.")
        except json.JSONDecodeError:
            print(f"Error loading employees: Invalid JSON.")
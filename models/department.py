import json
from .manager import Manager
from .designer import Designer
from .developer import Developer


class Department:
    """
    A class representing a Department, containing multiple managers and their teams.
    The Department class allows for adding managers, calculating salaries, and saving/loading employee data.
    """

    def __init__(self):
        """
        Initialize the Department with an empty list of managers.
        """
        self.managers = []  # List of managers in the department

    def add_manager(self, manager: Manager):
        """
        Add a manager to the department.

        Args:
        manager (Manager): A Manager object to be added to the department.
        """
        self.managers.append(manager)

    def give_salary(self):
        """
        Calculate and print the salary for each manager and their team members.

        The method iterates through all managers and their teams, calculates their salary,
        and prints the salary information for each individual.
        """
        for manager in self.managers:
            # Calculate the salary of the manager
            salary = manager.calculate_salary()
            print(f"{manager.first_name} {manager.last_name} received {round(salary)} money.")

            # Calculate and print the salary for each team member under the manager
            for member in manager.team:
                member_salary = member.calculate_salary()
                print(f"{member.first_name} {member.last_name} received {round(member_salary)} money.")

    def save_employees(self, filename):
        """
        Save the list of managers and their teams to a JSON file.

        Args:
        filename (str): The name of the file to which employee data will be saved.

        This method serializes the department's managers and their teams into a JSON file,
        which can be reloaded later.
        """
        try:
            with open(filename, 'w') as file:
                # Serialize all managers and their teams into the file in JSON format
                json.dump([manager.to_dict() for manager in self.managers], file, indent=4)
        except Exception as e:
            print(f"Error saving employees: {e}")

    def load_employees(self, filename):
        """
        Load employee data from a JSON file and populate the department with managers and their teams.

        Args:
        filename (str): The name of the file from which employee data will be loaded.

        This method deserializes employee data from the given JSON file and re-creates the Manager,
        Designer, and Developer objects as per the saved data.
        """
        try:
            with open(filename, 'r') as file:
                # Load the JSON data from the file
                data = json.load(file)

                # Iterate through the data to create manager objects and their team members
                for manager_data in data:
                    team = []
                    for member_data in manager_data['team']:
                        # Check if the team member is a Designer (has 'eff_coeff')
                        if 'eff_coeff' in member_data:
                            team.append(Designer(**member_data))
                        else:
                            # Check if the team member is another Manager (has 'team')
                            if 'team' in member_data:
                                team.append(Manager(**member_data))
                            else:
                                # Otherwise, the team member is a Developer
                                team.append(Developer(**member_data))

                    # Create a Manager object and add to the department
                    manager = Manager(**manager_data)
                    self.add_manager(manager)
        except FileNotFoundError:
            print(f"Error loading employees: File '{filename}' not found.")
        except json.JSONDecodeError:
            print(f"Error loading employees: Invalid JSON.")

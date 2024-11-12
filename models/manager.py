from .developer import Developer
from .employee import Employee


class Manager(Employee):
    """
    A class representing a Manager, inheriting from the Employee class.
    This class includes logic for calculating a manager's salary based on their team's size,
    the number of developers in the team, and applies a salary increase based on these factors.
    """

    def __init__(self, first_name, last_name, base_salary, experience, team=None):
        """
        Initialize a Manager instance with a team and additional employee details.

        Args:
        first_name (str): The first name of the manager.
        last_name (str): The last name of the manager.
        base_salary (float): The base salary of the manager.
        experience (int): The number of years of experience the manager has.
        team (list, optional): A list of team members (Employees, Developers, etc.), default is an empty list.

        """
        # Initialize the parent Employee class with the basic details
        super().__init__(first_name, last_name, base_salary, experience)

        # Set the manager's team (defaults to an empty list if no team is provided)
        self.team = team or []

    def calculate_salary(self):
        """
        Calculate the manager's salary based on various factors:
        - Base salary from the Employee class.
        - An increase if the team size is greater than 5 or 10.
        - A bonus if more than half of the team are developers.

        Returns:
        float: The final salary of the manager, after all bonuses and adjustments.
        """
        # Start with the base salary calculated by the Employee class
        salary = super().calculate_salary()

        # Adjust salary based on team size
        if len(self.team) > 10:
            salary += 300  # Add 300 if team size is greater than 10
        elif len(self.team) > 5:
            salary += 200  # Add 200 if team size is between 6 and 10

        # Count the number of Developers in the team
        num_developers = sum(1 for member in self.team if isinstance(member, Developer))

        # If more than half of the team are Developers, increase the salary by 10%
        if len(self.team) > 1 and num_developers > len(self.team) / 2:
            salary *= 1.1  # Apply 10% bonus for a majority of Developers in the team

        # Return the final rounded salary
        return round(salary)

    def to_dict(self):
        """
        Convert the Manager instance into a dictionary format, including team details.

        This method extends the to_dict method from the Employee class by adding the team's
        members as serialized dictionaries.

        Returns:
        dict: A dictionary containing the manager's first name, last name, base salary,
              experience, and team details.
        """
        # Get the dictionary representation of the manager from the parent Employee class
        data = super().to_dict()

        # Add the team details to the dictionary by serializing each team member
        data['team'] = [member.to_dict() for member in self.team]

        return data

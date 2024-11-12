from .developer import Developer
from .employee import Employee


class Manager(Employee):
    def __init__(self, first_name, last_name, base_salary, experience, team=None):
        super().__init__(first_name, last_name, base_salary, experience)
        self.team = team or []  # Initialize team as an empty list if not provided

    def calculate_salary(self):
        # Start with the base salary calculation (inherited from Employee class)
        salary = super().calculate_salary()

        # Apply team size bonuses
        if len(self.team) > 10:
            salary += 300  # Additional bonus for teams with more than 10 members
        elif len(self.team) > 5:
            salary += 200  # Bonus for teams with more than 5 members

        # Apply bonus if more than half of the team members are Developers
        num_developers = sum(1 for member in self.team if isinstance(member, Developer))

        # Only apply the 10% increase if team has more than one member and more than half are developers
        if len(self.team) > 1 and num_developers > len(self.team) / 2:
            salary *= 1.1  # Increase by 10% if more than half are Developers

        return round(salary)

    def to_dict(self):
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "base_salary": self.base_salary,
            "experience": self.experience,
            "team": [member.to_dict() for member in self.team]  # Serialize team members
        }

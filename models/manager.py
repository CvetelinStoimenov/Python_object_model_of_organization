from .developer import Developer
from .designer import Designer


class Manager(Designer):
    def __init__(self, first_name, last_name, base_salary, experience, team=None):
        super().__init__(first_name, last_name, base_salary, experience,
                         eff_coeff=1.0)  # Assuming no eff_coeff for Managers
        self.team = team or []

    def calculate_salary(self):
        counted_salary = super().calculate_salary()  # Get salary from Designer (or base logic)

        # Apply team size bonuses
        if len(self.team) > 5:
            counted_salary += 200
        if len(self.team) > 10:
            counted_salary += 300

        # Apply bonus for having more than half Developers
        dev_count = sum(isinstance(member, Developer) for member in self.team)
        if dev_count > len(self.team) / 2:
            counted_salary *= 1.1  # 10% bonus for more than half being developers

        return counted_salary

    def to_dict(self):
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "base_salary": self.base_salary,
            "experience": self.experience,
            "team": [member.to_dict() for member in self.team]  # Serialize team members
        }
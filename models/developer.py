from .employee import Employee

class Developer(Employee):

    def to_dict(self):
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "base_salary": self.base_salary,
            "experience": self.experience
        }
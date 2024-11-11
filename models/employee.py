class Employee:
    def __init__(self, first_name, last_name, base_salary, experience):
        self.first_name = first_name
        self.last_name = last_name
        self.base_salary = base_salary
        self.experience = experience

    def calculate_salary(self):
        if self.experience > 5:
            return self.base_salary * 1.2 + 500
        elif self.experience > 2:
            return self.base_salary + 200
        return self.base_salary

    def to_dict(self):
        return {
            'first_name': self.first_name,
            'last_name': self.last_name,
            'base_salary': self.base_salary,
            'experience': self.experience
        }
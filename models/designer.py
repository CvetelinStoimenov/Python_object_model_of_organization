from .employee import Employee

class Designer(Employee):
    def __init__(self, first_name, last_name, base_salary, experience, eff_coeff):
        super().__init__(first_name, last_name, base_salary, experience)
        self.eff_coeff = eff_coeff

    def calculate_salary(self):
        salary = super().calculate_salary()
        return salary * self.eff_coeff

    def to_dict(self):
        data = super().to_dict()
        data['eff_coeff'] = self.eff_coeff
        return data

from .employee import Employee

class Designer(Employee):
    def __init__(self, first_name, last_name, base_salary, experience, eff_coeff):

        if eff_coeff is None:
            raise ValueError("Efficiency coefficient must be provided.")

        if not (0 <= eff_coeff <= 1):
            raise ValueError("Efficiency coefficient must be between 0 and 1.")

        super().__init__(first_name, last_name, base_salary, experience)
        self.eff_coeff = eff_coeff

    def calculate_salary(self):
        salary = super().calculate_salary()
        efficiency_bonus = salary * self.eff_coeff
        counted_salary = salary+ efficiency_bonus
        return counted_salary

    def to_dict(self):
        data = super().to_dict()
        data['eff_coeff'] = self.eff_coeff
        return data

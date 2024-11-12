from .employee import Employee


class Designer(Employee):
    """
    A class representing a Designer, inheriting from the Employee class.
    This class includes logic for calculating a designer's salary with an efficiency
    coefficient, and overrides methods to serialize the designer's details into a dictionary.
    """

    def __init__(self, first_name, last_name, base_salary, experience, eff_coeff):
        """
        Initialize a Designer instance with an efficiency coefficient and other employee details.

        Args:
        first_name (str): The first name of the designer.
        last_name (str): The last name of the designer.
        base_salary (float): The base salary of the designer.
        experience (int): The number of years of experience the designer has.
        eff_coeff (float): The efficiency coefficient that affects the designer's salary.

        Raises:
        ValueError: If the efficiency coefficient is None or not between 0 and 1.
        """
        # Check if the efficiency coefficient is provided and within valid range (0-1)
        if eff_coeff is None:
            raise ValueError("Efficiency coefficient must be provided.")

        if not (0 <= eff_coeff <= 1):
            raise ValueError("Efficiency coefficient must be between 0 and 1.")

        # Initialize the parent Employee class with the common employee details
        super().__init__(first_name, last_name, base_salary, experience)

        # Set the efficiency coefficient specific to the Designer class
        self.eff_coeff = eff_coeff

    def calculate_salary(self):
        """
        Calculate the designer's salary by adding an efficiency bonus to the base salary.

        The final salary is calculated as follows:
        - Base salary is calculated by the parent Employee class.
        - An efficiency bonus is calculated by multiplying the base salary with the efficiency coefficient.

        Returns:
        float: The final salary of the designer including the efficiency bonus.
        """
        # Calculate the base salary using the Employee class method
        salary = super().calculate_salary()

        # Calculate the efficiency bonus based on the base salary and efficiency coefficient
        efficiency_bonus = salary * self.eff_coeff

        # Add the efficiency bonus to the base salary
        counted_salary = salary + efficiency_bonus

        return counted_salary

    def to_dict(self):
        """
        Convert the Designer instance into a dictionary format, including the efficiency coefficient.

        This method extends the to_dict method from the Employee class by adding the designer's
        efficiency coefficient.

        Returns:
        dict: A dictionary containing the designer's first name, last name, base salary, experience,
              and efficiency coefficient.
        """
        # Get the dictionary from the parent Employee class
        data = super().to_dict()

        # Add the efficiency coefficient to the dictionary for serialization
        data['eff_coeff'] = self.eff_coeff

        return data

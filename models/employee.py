class Employee:
    """
    A class representing an Employee with basic attributes and methods to
    calculate the salary based on years of experience.
    """

    def __init__(self, first_name, last_name, base_salary, experience):
        """
        Initialize an Employee instance with the following attributes:

        Parameters:
        first_name (str): The first name of the employee.
        last_name (str): The last name of the employee.
        base_salary (float): The base salary of the employee before any adjustments.
        experience (int): The number of years of experience the employee has.
        """

        # Validate first_name and last_name to be non-empty and alphabetic
        if not first_name or not first_name.isalpha():
            raise ValueError("First name must be a non-empty string containing only alphabetic characters.")

        if not last_name or not last_name.isalpha():
            raise ValueError("Last name must be a non-empty string containing only alphabetic characters.")

        # Validate base_salary to be a positive number
        if base_salary <= 0:
            raise ValueError("Base salary must be a positive number.")

        # Validate experience to be a non-negative integer
        if experience < 0:
            raise ValueError("Experience must be a non-negative number.")

        self.first_name = first_name
        self.last_name = last_name
        self.base_salary = base_salary
        self.experience = experience

    def calculate_salary(self):
        """
        Calculate the salary of the employee based on their experience.

        - If the employee has more than 5 years of experience, they receive a
          20% increase to their base salary and an additional 500 units.
        - If the employee has between 2 and 5 years of experience, they receive
          a 200 units increase to their base salary.
        - If the employee has less than 2 years of experience, their salary
          remains the base salary.

        Returns:
        float: The calculated salary of the employee.
        """
        # If employee has more than 5 years of experience, apply 20% increase
        # and add 500 units to their salary
        if self.experience > 5:
            return self.base_salary * 1.2 + 500

        # If employee has between 2 and 5 years of experience, apply a 200
        # units increase to the base salary
        elif self.experience > 2:
            return self.base_salary + 200

        # If employee has less than or equal to 2 years of experience, return
        # their base salary without any increase
        return self.base_salary

    def to_dict(self):
        """
        Convert the Employee instance into a dictionary representation.

        Returns:
        dict: A dictionary containing the employee's attributes.
        """
        return {
            'first_name': self.first_name,
            'last_name': self.last_name,
            'base_salary': self.base_salary,
            'experience': self.experience
        }
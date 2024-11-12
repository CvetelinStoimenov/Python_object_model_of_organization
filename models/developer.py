from .employee import Employee

class Developer(Employee):
    """
    A class representing a Developer, inheriting from the Employee class.
    This class provides a way to represent a developer's details, with an
    overridden method to return the developer's attributes in dictionary format.
    """

    def to_dict(self):
        """
        Override the to_dict method to return the Developer's attributes as a
        dictionary. This method is useful for serializing the developer instance
        into a dictionary format, which can be used for storing or sending
        data in formats like JSON.

        Returns:
        dict: A dictionary containing the developer's first name, last name,
              base salary, and experience.
        """
        # Returning the developer's details as a dictionary, which includes the
        # first name, last name, base salary, and experience inherited from the
        # Employee class.
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "base_salary": self.base_salary,
            "experience": self.experience
        }
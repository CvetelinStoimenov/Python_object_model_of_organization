import unittest
from io import StringIO
from unittest.mock import patch
from models.employee import Employee
from models.developer import Developer
from models.designer import Designer
from models.manager import Manager
from models.department import Department

class TestEmployee(unittest.TestCase):
    """
    Unit tests for the Employee class to ensure salary calculation works correctly.
    """

    class TestEmployeeValidation(unittest.TestCase):

        def test_invalid_first_name(self):
            """
            Test that an exception is raised if the first name contains non-alphabetic characters.
            """
            with self.assertRaises(ValueError) as context:
                Employee("John123", "Doe", 1000, 5)
            self.assertEqual(str(context.exception),
                             "First name must be a non-empty string containing only alphabetic characters.")

        def test_invalid_last_name(self):
            """
            Test that an exception is raised if the last name contains non-alphabetic characters.
            """
            with self.assertRaises(ValueError) as context:
                Employee("John", "Doe123", 1000, 5)
            self.assertEqual(str(context.exception),
                             "Last name must be a non-empty string containing only alphabetic characters.")

        def test_empty_first_name(self):
            """
            Test that an exception is raised if the first name is empty.
            """
            with self.assertRaises(ValueError) as context:
                Employee("", "Doe", 1000, 5)
            self.assertEqual(str(context.exception),
                             "First name must be a non-empty string containing only alphabetic characters.")

        def test_empty_last_name(self):
            """
            Test that an exception is raised if the last name is empty.
            """
            with self.assertRaises(ValueError) as context:
                Employee("John", "", 1000, 5)
            self.assertEqual(str(context.exception),
                             "Last name must be a non-empty string containing only alphabetic characters.")

        def test_invalid_base_salary(self):
            """
            Test that an exception is raised if the base salary is a negative number.
            """
            with self.assertRaises(ValueError) as context:
                Employee("John", "Doe", -1000, 5)
            self.assertEqual(str(context.exception), "Base salary must be a positive number.")

        def test_invalid_experience(self):
            """
            Test that an exception is raised if the experience is a negative number.
            """
            with self.assertRaises(ValueError) as context:
                Employee("John", "Doe", 1000, -1)
            self.assertEqual(str(context.exception), "Experience must be a non-negative number.")

    def test_salary_no_experience(self):
        """
        Test salary calculation when the employee has no experience.
        Expected output is the base salary.
        """
        employee = Employee("John", "Doe", 1000, 0)
        self.assertEqual(1000, employee.calculate_salary())

    def test_salary_with_two_years_experience(self):
        """
        Test salary calculation when the employee has two years of experience.
        Expected output is the base salary (no salary increase for 2 years).
        """
        employee = Employee("Test", "User", 1000, 2)
        self.assertEqual(1000, employee.calculate_salary())

    def test_salary_with_experience(self):
        """
        Test salary calculation when the employee has more than 2 years of experience.
        Expected output is base salary + 200.
        """
        employee = Employee("Jane", "Smith", 1000, 3)
        self.assertEqual(1200, employee.calculate_salary())

    def test_salary_with_five_years_experience(self):
        """
        Test salary calculation when the employee has five years of experience.
        Expected output is base salary + 200.
        """
        employee = Employee("Jane", "Smith", 1000, 5)
        self.assertEqual(1200, employee.calculate_salary())

    def test_salary_with_high_experience(self):
        """
        Test salary calculation when the employee has more than five years of experience.
        Expected output is base salary * 1.2 + 500.
        """
        employee = Employee("Alice", "Johnson", 1000, 6)
        self.assertEqual(1700, employee.calculate_salary())


class TestDesigner(unittest.TestCase):
    """
    Unit tests for the Designer class to ensure salary calculation works correctly,
    considering the efficiency coefficient.
    """

    def test_salary_with_eff_coeff_zero(self):
        """
        Test salary calculation for a designer with an efficiency coefficient of 0.
        Expected output is base salary + efficiency bonus (eff_coeff * base_salary).
        """
        designer = Designer("Emily", "Davis", 1200, 4, 0)
        self.assertEqual(1400, designer.calculate_salary())

    def test_salary_with_eff_coeff_positive(self):
        """
        Test salary calculation for a designer with an efficiency coefficient greater than 0.
        Expected output is base salary + efficiency bonus.
        """
        designer = Designer("Emily", "Davis", 1200, 4, 0.9)
        self.assertEqual(2660, designer.calculate_salary())

    def test_salary_with_high_eff_coeff(self):
        """
        Test salary calculation for a designer with the highest efficiency coefficient (1).
        Expected output is base salary + efficiency bonus.
        """
        designer = Designer("Alice", "Johnson", 1300, 7, 1.0)
        self.assertEqual(4120, designer.calculate_salary())

    def test_eff_coeff_too_high(self):
        """
        Test that an exception is raised if the efficiency coefficient is higher than 1.
        """
        with self.assertRaises(ValueError) as context:
            designer = Designer("John", "Doe", 1000, 5, 1.2)

        self.assertEqual("Efficiency coefficient must be between 0 and 1.", str(context.exception))

    def test_negative_eff_coeff(self):
        """
        Test that an exception is raised if the efficiency coefficient is negative.
        """
        with self.assertRaises(ValueError) as context:
            Designer("John", "Doe", 1000, 5, -0.5)

        self.assertEqual("Efficiency coefficient must be between 0 and 1.", str(context.exception))

    def test_no_eff_coeff(self):
        """
        Test that an exception is raised if the efficiency coefficient is not provided.
        """
        with self.assertRaises(ValueError) as context:
            Designer("John", "Doe", 1000, 5, None)

        self.assertEqual("Efficiency coefficient must be provided.", str(context.exception))

    def test_invalid_first_name(self):
        """
        Test that an exception is raised if the first name contains non-alphabetic characters.
        """
        with self.assertRaises(ValueError) as context:
            Designer("John123", "Doe", 1200, 4, 0.8)
        self.assertEqual(str(context.exception), "First name must be a non-empty string containing only alphabetic characters.")

    def test_invalid_last_name(self):
        """
        Test that an exception is raised if the last name contains non-alphabetic characters.
        """
        with self.assertRaises(ValueError) as context:
            Designer("John", "Doe123", 1200, 4, 0.8)
        self.assertEqual(str(context.exception), "Last name must be a non-empty string containing only alphabetic characters.")

    def test_invalid_base_salary(self):
        """
        Test that an exception is raised if the base salary is a negative number.
        """
        with self.assertRaises(ValueError) as context:
            Designer("John", "Doe", -1200, 4, 0.8)
        self.assertEqual(str(context.exception), "Base salary must be a positive number.")

    def test_invalid_experience(self):
        """
        Test that an exception is raised if the experience is a negative number.
        """
        with self.assertRaises(ValueError) as context:
            Designer("John", "Doe", 1200, -4, 0.8)
        self.assertEqual(str(context.exception), "Experience must be a non-negative number.")

class TestManager(unittest.TestCase):
    """
    Unit tests for the Manager class to ensure salary calculation works correctly,
    considering team size and developer count.
    """

    def test_invalid_first_name(self):
        """
        Test that an exception is raised if the first name contains non-alphabetic characters.
        """
        with self.assertRaises(ValueError) as context:
            Manager("John123", "Doe", 2000, 5, [])
        self.assertEqual(str(context.exception), "First name must be a non-empty string containing only alphabetic characters.")

    def test_invalid_last_name(self):
        """
        Test that an exception is raised if the last name contains non-alphabetic characters.
        """
        with self.assertRaises(ValueError) as context:
            Manager("John", "Doe123", 2000, 5, [])
        self.assertEqual(str(context.exception), "Last name must be a non-empty string containing only alphabetic characters.")

    def test_invalid_base_salary(self):
        """
        Test that an exception is raised if the base salary is a negative number.
        """
        with self.assertRaises(ValueError) as context:
            Manager("John", "Doe", -2000, 5, [])
        self.assertEqual(str(context.exception), "Base salary must be a positive number.")

    def test_invalid_experience(self):
        """
        Test that an exception is raised if the experience is a negative number.
        """
        with self.assertRaises(ValueError) as context:
            Manager("John", "Doe", 2000, -5, [])
        self.assertEqual(str(context.exception), "Experience must be a non-negative number.")

    def test_invalid_team_member(self):
        """
        Test that an exception is raised if a team member is not an instance of Employee (or subclass).
        """
        with self.assertRaises(ValueError) as context:
            Manager("John", "Doe", 2000, 5, ["invalid_member"])  # Team member not an instance of Employee
        self.assertEqual(str(context.exception), "All team members must be instances of Employee (or subclass).")

    def test_manager_with_no_team(self):
        """
        Test salary calculation for a manager with no team.
        Expected output is base salary + 200 (no team to increase salary).
        """
        manager = Manager("Test", "Manager", 2000, 5, [])
        self.assertEqual(2200, manager.calculate_salary())

    def test_salary_with_under_five_employee_in_team(self):
        """
        Test salary calculation for a manager with less than five employees in the team.
        Expected output is base salary + 200.
        """
        manager = Manager("Bob", "Brown", 2000, 6, [Developer("John", "Doe", 1000, 3)])
        self.assertEqual(2900, manager.calculate_salary())

    def test_salary_with_more_than_half_developers(self):
        """
        Test salary calculation for a manager with more than half developers in the team.
        Expected output is base salary * 1.1.
        """
        manager = Manager("Bob", "Brown", 2000, 6, [
            Developer("John", "Doe", 1000, 3),
            Developer("Jane", "Smith", 1200, 4),
            Designer("Charlie", "Wilson", 1400, 5, 0.85),
        ])
        self.assertEqual(3190, manager.calculate_salary())

    def test_salary_with_more_then_five_team_equal_designer_and_developers(self):
        """
        Test salary calculation for a manager with a balanced team of designers and developers.
        Expected output is base salary with applicable adjustments.
        """
        manager = Manager("Alice", "Johnson", 2000, 7, [
            Developer("John", "Doe", 1000, 3),
            Designer("Jane", "Smith", 1200, 4, 0.9),
            Developer("Charlie", "Wilson", 1500, 5),
            Designer("Lisa", "Green", 1300, 6, 0.8),
            Developer("Eve", "White", 1100, 2),
            Designer("Jane", "Wilson", 1300, 8, 0.6)
        ])
        self.assertEqual(3100, manager.calculate_salary())

    def test_manager_with_large_team_of_designers(self):
        """
        Test salary calculation for a manager with a large team of designers.
        Expected output is base salary with applicable adjustments.
        """
        manager = Manager("Test", "Manager", 2000, 5, [
            Designer("John", "Doe", 1200, 3, 0.5),
            Designer("Jane", "Smith", 1300, 4, 0.7),
            Designer("Alice", "Johnson", 1100, 2, 0.9),
            Designer("Bob", "Brown", 1400, 6, 0.8),
            Designer("Eve", "White", 1100, 2, 0.3),
            Designer("Jane", "Wilson", 1300, 8, 0.6)
        ])
        self.assertEqual(2400, manager.calculate_salary())

    def test_salary_with_large_team_and_more_developers(self):
        """
        Test salary calculation for a manager with a large team consisting of more developers than designers.
        Expected output is base salary with applicable adjustments.
        """
        manager = Manager("Alice", "Johnson", 2000, 7, [
            Developer("John", "Doe", 1000, 3),
            Designer("Jane", "Smith", 1200, 4, 0.9),
            Developer("Charlie", "Wilson", 1500, 5),
            Designer("Lisa", "Green", 1300, 6, 0.8),
            Developer("Eve", "White", 1100, 2),
            Developer("Max", "Black", 1200, 3),
            Developer("Anna", "Grey", 1250, 4),
            Designer("Oliver", "Blue", 1400, 5, 0.7),
            Developer("Mia", "Red", 1350, 3),
            Developer("Zoe", "Pink", 1450, 6),
        ])
        self.assertEqual(3410, manager.calculate_salary())


class TestDepartment(unittest.TestCase):
    """
    Unit tests for the Department class to ensure proper functionality of salary distribution.
    """

    @patch('sys.stdout', new_callable=StringIO)
    def test_department_salary_distribution(self, mock_stdout):
        """
        Test that the department correctly distributes salaries to managers and their team members.
        The output is captured and validated.
        """
        department = Department()
        manager = Manager("John", "Doe", 2000, 6, [
            Developer("John", "Doe", 1000, 3),
            Designer("Jane", "Smith", 1200, 4, 0.9),
            Developer("Charlie", "Wilson", 1500, 5)])
        department.add_manager(manager)

        # Call the method to give salaries
        department.give_salary()
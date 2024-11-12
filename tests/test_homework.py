import unittest
from io import StringIO
from unittest.mock import patch
from models.employee import Employee
from models.developer import Developer
from models.designer import Designer
from models.manager import Manager
from models.department import Department

class TestEmployee(unittest.TestCase):

    def test_salary_no_experience(self):
        employee = Employee("John", "Doe", 1000, 0)
        self.assertEqual(1000, employee.calculate_salary())

    def test_salary_with_two_years_experience(self):
        employee = Employee("Test", "User", 1000, 2)
        self.assertEqual(1000, employee.calculate_salary())

    def test_salary_with_experience(self):
        employee = Employee("Jane", "Smith", 1000, 3)
        self.assertEqual(1200, employee.calculate_salary())

    def test_salary_with_five_years_experience(self):
        employee = Employee("Jane", "Smith", 1000, 5)
        self.assertEqual(1200, employee.calculate_salary())

    def test_salary_with_high_experience(self):
        employee = Employee("Alice", "Johnson", 1000, 6)
        self.assertEqual(1700, employee.calculate_salary())


class TestDesigner(unittest.TestCase):

    def test_salary_with_eff_coeff_zero(self):
        designer = Designer("Emily", "Davis", 1200, 4, 0)
        self.assertEqual(1400, designer.calculate_salary())

    def test_salary_with_eff_coeff_positive(self):
        designer = Designer("Emily", "Davis", 1200, 4, 0.9)
        self.assertEqual(2660, designer.calculate_salary())

    def test_salary_with_high_eff_coeff(self):
        designer = Designer("Alice", "Johnson", 1300, 7, 1.0)
        self.assertEqual(4120, designer.calculate_salary())

    def test_eff_coeff_too_high(self):
        with self.assertRaises(ValueError) as context:
            designer = Designer("John", "Doe", 1000, 5, 1.2)

        self.assertEqual("Efficiency coefficient must be between 0 and 1.", str(context.exception))

    def test_negative_eff_coeff(self):
        with self.assertRaises(ValueError) as context:
            Designer("John", "Doe", 1000, 5, -0.5)

        self.assertEqual("Efficiency coefficient must be between 0 and 1.", str(context.exception))

    def test_no_eff_coeff(self):
        with self.assertRaises(ValueError) as context:
            Designer("John", "Doe", 1000, 5, None)

        self.assertEqual("Efficiency coefficient must be provided.", str(context.exception))


class TestManager(unittest.TestCase):

    def test_manager_with_no_team(self):
        manager = Manager("Test", "Manager", 2000, 5, [])
        self.assertEqual(2200, manager.calculate_salary())

    def test_salary_with_under_five_employee_in_team(self):
        manager = Manager("Bob", "Brown", 2000, 6, [Developer("John", "Doe", 1000, 3)])
        self.assertEqual(2900, manager.calculate_salary())

    def test_salary_with_more_than_half_developers(self):
        manager = Manager("Bob", "Brown", 2000, 6, [
            Developer("John", "Doe", 1000, 3),
            Developer("Jane", "Smith", 1200, 4),
            Designer("Charlie", "Wilson", 1400, 5, 0.85),
        ])
        self.assertEqual(3190, manager.calculate_salary())

    def test_salary_with_more_then_five_team_equal_designer_and_developers(self):
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

    @patch('sys.stdout', new_callable=StringIO)
    def test_department_salary_distribution(self, mock_stdout):
        department = Department()
        manager = Manager("John", "Doe", 2000, 6, [
            Developer("John", "Doe", 1000, 3),
            Designer("Jane", "Smith", 1200, 4, 0.9),
            Developer("Charlie", "Wilson", 1500, 5)])
        department.add_manager(manager)

        department.give_salary()

        printed_output = mock_stdout.getvalue()

        self.assertIn(printed_output, "John Doe received 3190 money."
                      "\nJohn Doe received 1200 money."
                      "\nJane Smith received 2660 money."
                      "\nCharlie Wilson received 1700 money.\n")


if __name__ == "__main__":
    unittest.main()
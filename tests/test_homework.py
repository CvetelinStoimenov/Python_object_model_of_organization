import unittest
from models.manager import Manager
from models.developer import Developer
from models.designer import Designer
from models.department import Department


class TestOrganization(unittest.TestCase):

    def setUp(self):
        # Test data for Developer, Designer, and Manager
        self.developer_3_years = Developer("John", "Doe", 1000, 3)
        self.developer_6_years = Developer("Charlie", "Wilson", 1200, 6)
        self.designer_4_years = Designer("Jane", "Smith", 1200, 4, 0.9)
        self.designer_7_years = Designer("Alice", "Johnson", 1400, 7, 0.85)

        # Manager with team
        self.manager_small_team = Manager("Bob", "Brown", 2000, 6, [self.developer_3_years, self.designer_4_years])
        self.manager_large_team = Manager("Emily", "Davis", 2000, 6,
                                          [self.developer_3_years, self.developer_6_years, self.designer_4_years,
                                           self.designer_7_years])
        self.manager_no_team = Manager("Lisa", "Green", 2000, 6)

        # Department with managers
        self.department = Department()

    def test_developer_salary(self):
        # Testing Developer salaries based on different years of experience
        self.assertEqual(round(self.developer_3_years.calculate_salary()), 1200)  # 3 years, base + 200
        self.assertEqual(round(self.developer_6_years.calculate_salary()), 1940)  # 6 years, base * 1.2 + 500

    def test_designer_salary(self):
        # Testing Designer salary based on different experience and efficiency coefficients
        self.assertEqual(round(self.designer_4_years.calculate_salary()), 1260)  # 4 years, base + 200 * eff_coeff (0.9)
        self.assertEqual(round(self.designer_7_years.calculate_salary()),
                         1853)  # 7 years, base * 1.2 + 500 * eff_coeff (0.85)

    def test_manager_salary(self):
        # Testing Manager salary with different team sizes and configurations

        # Manager with small team (team size < 5)
        self.assertEqual(round(self.manager_small_team.calculate_salary()),
                         2900)  # base salary + experience bonus (6 years) + small team (no bonus)

        # Manager with a large team (team size > 5)
        self.assertEqual(round(self.manager_large_team.calculate_salary()),
                         3100)  # base salary + experience bonus + team size > 5 bonus (200)

        # Manager with no team
        self.assertEqual(round(self.manager_no_team.calculate_salary()),
                         2400)  # base salary + experience bonus, no team bonus

    def test_manager_team_bonus(self):
        # Testing the team-related bonuses for Managers
        manager_with_large_team = Manager("Sam", "Owen", 2000, 6,
                                          [self.developer_3_years, self.developer_6_years, self.designer_4_years,
                                           self.designer_7_years, self.developer_3_years, self.developer_6_years])
        self.assertEqual(round(manager_with_large_team.calculate_salary()),
                         3200)  # base salary + experience + team size > 5 + more than half are Developers (10% increase)

    def test_department_salary(self):
        # Adding managers to department and testing salary calculation for the entire department
        self.department.add_manager(self.manager_small_team)
        self.department.add_manager(self.manager_large_team)
        self.department.add_manager(self.manager_no_team)
        self.department.give_salary()  # Check if salary prints correctly for each manager in the department

    def test_save_and_load_employees(self):
        # Test saving and loading employees to/from JSON file
        self.department.add_manager(self.manager_small_team)
        self.department.add_manager(self.manager_large_team)
        self.department.save_employees("employees.json")

        # Now load employees from the file and check if the length of managers is correct
        self.department.load_employees("employees.json")
        self.assertEqual(len(self.department.managers), 2)  # Ensure that two managers were loaded


if __name__ == "__main__":
    unittest.main()

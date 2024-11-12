  
# Organization Management System

## Overview

This project simulates an organization structure, focusing on various types of employees (such as Managers, Developers, and Designers) within a department. The system calculates employee salaries based on their role, experience, and efficiency coefficients for Designers. The project supports serialization and deserialization of employee data, allowing the saving and loading of employee details in/from JSON files.

## Features

-   **Employee Salary Calculation**: Each employee's salary is calculated based on their experience and role:
    
    -   Employees with experience greater than 5 years receive a 20% salary increase and an additional 500.
    -   Employees with 2 to 5 years of experience receive a 200 increase.
    -   Designers have an efficiency coefficient that impacts their salary.
-   **Department Management**: Managers can oversee a team of employees (Designers and Developers). The salary calculation for Managers is influenced by the size of their team and the composition of Designers vs Developers.
    
-   **Data Persistence**: Employee data can be saved to and loaded from JSON files, preserving the structure of the organization.
    
-   **Unit Testing**: Comprehensive unit tests have been written for all classes, ensuring that salary calculations and other functionalities work as expected.
    

## Getting Started

### Prerequisites

-   Python 3.x
-   `unittest` for testing

### Installation

1.  Clone the repository:
    
#
    git clone https://github.com/your-username/organization-management-system.git
    cd organization-management-system
    
2.  Install required dependencies (if any) from `requirements.txt`:
# 
      pip install -r requirements.txt/text here
    

### Running the Application

To run the application, use the following command:


`python main.py` 

This will execute the default functionality, which includes managing employees and calculating their salaries based on their roles and experience.

### Running Tests

To run the tests, you can use the following command:


`python -m unittest discover` 

This will automatically discover and run all the tests in the `tests/` directory.

## Directory Structure


```
organization-management-system/
├── models/
│   ├── employee.py          # Employee class and related logic
│   ├── developer.py         # Developer class
│   ├── designer.py          # Designer class
│   ├── manager.py           # Manager class
│   └── department.py        # Department management logic
├── data/
│   └── employees.json       # File to store employee data
├── tests/
│   └── test_homework.py     # Unit tests for the system
├── .gitignore               # Git ignore file
├── README.md                # Project documentation
├── requirements.txt         # Project dependencies
└── main.py                  # Main script to execute the program` 

```
## Contributing

Contributions are welcome! If you would like to contribute to the project, feel free to open a pull request or submit an issue.

### Steps for Contributing:

1.  Fork the repository.
2.  Create a new branch (`git checkout -b feature-branch`).
3.  Commit your changes (`git commit -am 'Add new feature'`).
4.  Push to the branch (`git push origin feature-branch`).
5.  Create a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
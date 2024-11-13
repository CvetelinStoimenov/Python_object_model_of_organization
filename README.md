  
# Organization Management System

## Overview

This project simulates an organization structure, focusing on various types of employees (such as Managers, Developers, and Designers) within a department. The system calculates employee salaries based on their role, experience, and efficiency coefficients for Designers. The project supports serialization and deserialization of employee data, allowing the saving and loading of employee details in/from JSON files.

## Features

- **Employee Salary Calculation**: 
  - Each employee's salary is calculated based on their experience and role:
    - Employees with experience greater than 5 years receive a 20% salary increase and an additional 500.
    - Employees with 2 to 5 years of experience receive a 200 increase.
    - Designers have an efficiency coefficient that impacts their salary.
  
- **Department Management**: 
  - Managers can oversee a team of employees (Designers and Developers). The salary calculation for Managers is influenced by the size of their team and the composition of Designers vs Developers.

- **Data Persistence**: 
  - Employee data can be saved to and loaded from JSON files, preserving the structure of the organization.

- **Unit Testing**: 
  - Comprehensive unit tests have been written for all classes, ensuring that salary calculations and other functionalities work as expected.

- **Dockerization**: 
  - The application is containerized using Docker, allowing for easy deployment in any environment.

- **CI/CD**: 
  - Continuous Integration and Continuous Deployment (CI/CD) are set up using GitHub Actions, automating the testing and deployment process.

## Getting Started

### Prerequisites

- Python 3.x
- Docker (for containerization)
- `unittest` for testing
- GitHub account (for CI/CD)

### Installation

1.  Clone the repository:
    
#
    git clone https://github.com/CvetelinStoimenov/Python_object_model_of_organization
    cd organization-management-system
    
2.  Install required dependencies (if any) from `requirements.txt`:
# 
      pip install -r requirements.txt/text here
    
3. (Optional) If you want to run the application in a containerized environment, follow the Docker instructions below.
### Running the Application

To run the application, use the following command:

#
    python main.py

This will execute the default functionality, which includes managing employees and calculating their salaries based on their roles and experience.

### Running Tests

To run the tests, you can use the following command:


#
    python -m unittest discover

This will automatically discover and run all the tests in the `tests/` directory.


### Running the Application with Docker

If you'd like to run the application inside a Docker container, follow these steps:

1.  **Build the Docker image**:
#
    docker build -t yourusername/organization-app .
    
2.  **Run the Docker container**:
#
    
    docker run -it yourusername/organization-app:latest
    

This will run the application inside a container, providing the same functionality as running it natively.

## Directory Structure


```
organization-management-system/
├── models/
│   ├── employee.py          # Employee class and related logic
│   ├── developer.py         # Developer class
│   ├── designer.py          # Designer class
│   ├── manager.py           # Manager class
│   └── department.py        # Department management logic
├── .github
│   └── workflows
│       └── ci.yml           # CI/CD- GitHub Actions file
├── tests/
│   └── test_homework.py     # Unit tests for the system
├── .gitignore               # Git ignore file
├── .dockerignore            # Docker ignore file
├── README.md                # Project documentation
├── requirements.txt         # Project dependencies
├── docker-compose.yml       # Docker Compose file for running the application
└── main.py                  # Main script to execute the program

```

### Docker Setup

The project has been containerized using Docker to ensure easy deployment. It includes a `Dockerfile` that defines the environment for the application.

#### Docker Commands

-   **Build the Docker image**:
#
    docker build -t yourusername/organization-app .
    
-   **Run the Docker container**:
#
    
    docker run -it yourusername/organization-app:latest
    
-   **Push the image to Docker Hub**:
    
    If you want to push the Docker image to Docker Hub, use the following command:
#
    
    docker push yourusername/organization-app:latest
    

## CI/CD with GitHub Actions

Continuous Integration and Continuous Deployment (CI/CD) are set up using GitHub Actions. This allows for automated testing and deployment whenever changes are pushed to the repository.

### GitHub Actions Workflow

The GitHub Actions workflow is defined in the `.github/workflows/ci.yml` file. It includes steps for:

1.  Checking out the code.
2.  Setting up Docker.
3.  Logging in to Docker Hub.
4.  Building and pushing the Docker image.
5.  Running tests.

The workflow is triggered on `push` and `pull_request` events to the `main` branch.

### Setting up GitHub Secrets

For the Docker login action to work, you'll need to add your Docker Hub credentials as GitHub Secrets:

1.  Go to **Settings** → **Secrets** → **Actions**.
2.  Add the following secrets:
    -   `DOCKER_USERNAME`: Your Docker Hub username.
    -   `DOCKER_PASSWORD`: Your Docker Hub personal access token.

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

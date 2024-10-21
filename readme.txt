Rule Engine with AST
Project Overview
This Django-based application is a Rule Engine that dynamically evaluates user-defined conditions using an Abstract Syntax Tree (AST). It allows users to create, combine, and modify rules to determine eligibility based on attributes like age, department, income, and more.

The system provides a simple web-based interface to manage rules, uses SQLite for data storage, and leverages Django for handling the backend logic.

Features
Dynamic Rule Creation: Users can define rules using conditions such as age, salary, experience, etc.
AST Representation: Rules are parsed into an AST structure, allowing dynamic manipulation and efficient evaluation.
Rule Combination: Multiple rules can be combined logically (using AND/OR) to create more complex eligibility criteria.
UI-based Interaction: The application provides a web interface to create, manage, and evaluate rules.
SQLite Storage: Uses SQLite for storing rules and related metadata for easy local development.
Design Choices
Abstract Syntax Tree (AST):

The rules are parsed into an AST where nodes represent operators (AND/OR) and operands (conditions).
This allows for efficient evaluation and dynamic modification of the rules.
SQLite Database:

Chosen for its simplicity and ease of use for local development.
It fits well with Django’s ORM, making database management straightforward.
Django Framework:

Django handles web requests, database interactions, and business logic.
Django forms are used for UI interactions, without the need for a separate REST API.
No Django REST Framework:

The project does not utilize Django REST Framework, as it focuses on UI-based rule management rather than a full-fledged API.
Prerequisites
Before starting, ensure you have the following installed:

Python 3.8+
pip (Python package installer)



Setup Instructions
Step 1: Clone the Repository

git clone https://github.com/your-github-handle/rule-engine-ast.git
cd rule-engine-ast
Step 2: Create a Virtual Environment
It’s recommended to use a virtual environment for managing dependencies:


python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Step 3: Install Dependencies
Install the required Python packages by running:


pip install -r requirements.txt
Step 4: Configure the Database
Django uses SQLite as the default database. You don't need any additional setup for SQLite, but ensure that migrations are applied to create the necessary tables.

Run the following commands to apply migrations:


python manage.py migrate
Step 5: Create a Superuser (Optional)
If you want to access the Django Admin interface for managing rules:


python manage.py createsuperuser
Step 6: Run the Application
Start the Django development server:


python manage.py runserver
You can access the application at http://localhost:8000.

Usage Instructions
1. Rule Creation
Navigate to the Create Rule page to define new rules.
You can specify conditions like age > 30 AND department == 'Sales'.
The system will parse this string into an AST and store it in the database.
2. Combining Rules
Combine multiple rules using logical operators (AND/OR).
The combined rules will be represented in the AST and can be evaluated for specific user attributes.
3. Rule Evaluation
Provide user data (e.g., {"age": 35, "department": "Sales", "salary": 60000}) and evaluate the rules to check if the conditions are met.
The system will return True if the data matches the rule conditions or False otherwise.
Testing
The project includes basic tests to ensure functionality of rule creation, combination, and evaluation.

To run the tests, use:

python manage.py test
Project Structure

rule-engine-ast/
├── manage.py             # Django management script
├── rule_engine/          # Main application directory
│   ├── models.py         # Database models (AST representation)
│   ├── views.py          # Rule creation, combination, and evaluation logic
│   ├── urls.py           # URL routing
│   ├── forms.py          # Django forms for user input
│   └──         # HTML templates for the UI
├── db.sqlite3            # SQLite database (auto-generated after migration)
    templates/
└── requirements.txt      # Project dependencies
Key Components:
models.py: Contains the database schema for storing the rules and their AST representations.
views.py: Defines the business logic for creating, combining, and evaluating rules.
forms.py: Handles input validation for rule creation.
templates/: Contains HTML templates for the front-end UI.
Dependencies
The project relies on the following Python packages:

Django: Web framework used for building the application.
SQLite: Default database for Django (no additional setup required).
To install dependencies:


pip install -r requirements.txt

Build Instructions

Clone the repository from GitHub.

Install dependencies using the provided requirements.txt.

Apply database migrations to initialize the SQLite database.

Run the Django server to launch the application.

Design Considerations

Dynamic AST Handling: Rules are parsed into an AST structure to enable flexibility in rule evaluation. Each node represents either an operator (AND/OR) or an operand (condition).
Efficient Rule Combination: When combining rules, redundant checks are minimized by efficiently merging the AST nodes.
UI for Rule Management: The project leverages Django’s form handling to provide a simple interface for rule creation and evaluation.
Future Enhancements

Enhanced Error Handling: Improve handling of invalid rule strings or malformed input data.
Support for Custom Functions: Add support for user-defined functions within rules for advanced conditions.
Advanced Rule Management: Provide more options for modifying existing rules (e.g., adding/removing conditions dynamically).
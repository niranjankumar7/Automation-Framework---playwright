Python Automation Framework

This repository contains a Python-based automation framework using Behave, Playwright, and Cucumber. Follow the steps below to set up the framework on your system and get started.

Prerequisites

Ensure the following are installed on your system:

Python 3.7+ - Download Python
Git - Download Git
pip (Python package manager) - Comes with Python installation.
Node.js (required for Playwright) - Download Node.js.
Setup Instructions

Step 1: Clone the Repository
Use the following command to clone the repository to your local machine:

git clone <repository-url>
Replace <repository-url> with the URL of this repository.

Navigate to the project directory:

cd <project-directory>
Step 2: Create a Virtual Environment
Create and activate a virtual environment to isolate dependencies:

python3 -m venv venv
source venv/bin/activate  # For Mac/Linux
venv\Scripts\activate     # For Windows
Step 3: Install Dependencies
Install all required Python libraries using pip:

pip install -r requirements.txt
Install Playwright browser binaries:

playwright install
Step 4: Run Tests
Run the framework to verify the setup.

Using Behave

behave
Using Pytest

If your tests are configured to work with pytest, use:

pytest
Framework Structure

features/: Contains all feature files written in Gherkin syntax.
steps/: Includes step definitions corresponding to the feature files.
utilities/: Utility functions or helper modules for the framework.
reports/: Test execution reports (e.g., HTML, JSON).
Common Issues

1. Behave Unknown Formatter
If you encounter an error like format=behave_html_formatter:HTMLFormatter is unknown, install the required formatter:

pip install behave-html-formatter
2. Playwright Browser Installation
Ensure Playwright browser binaries are installed:

playwright install
Contributing

Feel free to fork this repository and submit pull requests for any enhancements or bug fixes.

License

This project is licensed under the MIT License.

Contact
For any issues or questions, please create a GitHub issue or contact - Niranjan Kumar A - niranjan.arkalgud@gmail.com
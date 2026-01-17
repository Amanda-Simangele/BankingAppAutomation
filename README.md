# Banking Application Automation Framework

## Overview
This project is a UI automation test framework built using **Python, Selenium WebDriver, and Pytest**.  
The framework automates core customer banking functionalities on the Way2Automation demo banking application.

Application Under Test:  
http://www.way2automation.com/angularjs-protractor/banking/#/login

The framework is designed following **Object-Oriented Programming (OOP)** principles and the **Page Object Model (POM)** to ensure maintainability, readability, and reusability.

---

## Tools & Technologies Used
- **Python**
- **Selenium WebDriver**
- **Pytest**
- **WebDriver Manager**
- **ConfigParser** (for configuration management)
- **HTML Reporting (pytest-html)**

---

## Framework Design
The framework follows best practices for test automation:

- **Page Object Model (POM)**  
  All page interactions and locators are encapsulated within page classes.

- **Pytest Fixtures**  
  Browser setup and teardown are managed centrally using `conftest.py`.

- **Configuration Driven**  
  Application URLs and environment details are stored in `configs.ini`.

- **Reusable Utilities**  
  Common actions and helper methods are placed under the `Utils` package.

---

## Project Structure
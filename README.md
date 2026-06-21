# Selenium Python Automation Framework

## 📌 Project Overview

This project is a Selenium WebDriver Automation Framework built using Python and the Page Object Model (POM) design pattern.

The framework automates the following user journey:

* Launch EventHub application
* Login with valid credentials
* Navigate to the Events page
* Verify Events page URL
* Validate Events page content
* Capture screenshots during execution
* Generate execution logs
* Generate HTML test reports using PyTest

---

## 🚀 Features

* Selenium WebDriver Automation
* Python-based Test Framework
* Page Object Model (POM)
* Explicit Waits
* Logging Framework
* Screenshot Capture
* PyTest Integration
* HTML Reporting (pytest-html)
* Automatic Browser Setup using WebDriver Manager

---

## 🛠️ Tech Stack

| Technology         | Purpose                  |
| ------------------ | ------------------------ |
| Python             | Programming Language     |
| Selenium WebDriver | Web Automation           |
| PyTest             | Test Execution Framework |
| PyTest HTML        | HTML Reporting           |
| WebDriver Manager  | Driver Management        |
| Logging            | Execution Logs           |
| Git & GitHub       | Version Control          |

---

## 📂 Project Structure

```text
EventHubAutomation
│
├── pages
│   ├── login_page.py
│   ├── event_page.py
│   └── __init__.py
│
├── tests
│   └── test_pages1.py
│
├── utilities
│   ├── logger.py
│   └── __init__.py
│
├── screenshots
│   ├── login_success.png
│   └── event_page.png
│
├── reports
│   └── report.html
│
├── logs
│   └── automation.log
│
├── conftest.py
├── requirements.txt
└── README.md
```

---

## 📄 Test Scenario

### Login Validation

* Open EventHub application
* Enter valid username
* Enter valid password
* Click Login button
* Verify successful login
* Capture login success screenshot

### Event Page Validation

* Click Events tab
* Verify Event page URL
* Verify Event page text
* Capture Event page screenshot

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/PallabiBhowmick13/<repository-name>.git
```

### Navigate to Project

```bash
cd EventHubAutomation
```

### Create Virtual Environment

```bash
python -m venv .venv
```

### Activate Virtual Environment

Windows:

```bash
.venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Execute Test

Run PyTest:

```bash
pytest tests/test_pages1.py
```

---

## 📊 Generate HTML Report

```bash
pytest tests/test_pages1.py --html=reports/report.html --self-contained-html
```

Generated Report:

```text
reports/report.html
```

Open the report in your browser to view:

* Passed Tests
* Failed Tests
* Execution Time
* Error Details
* Test Summary

---

## 📸 Screenshots

Screenshots are automatically captured during execution.

Example:

```text
screenshots/
├── login_success.png
└── event_page.png
└── test_failur.png
```

---

## 📝 Logs

Execution logs are stored in:

```text
logs/automation.log
```

Sample Log Output:

```text
INFO - Starting Test Execution
INFO - Login successful and Home page loaded
INFO - Event URL Verified
INFO - Event Page Text Verified
INFO - EVENT TEST PASSED
```

---

## 🔄 Automation Flow

```text
Launch Browser
      |
      ↓
Open Login Page
      |
      ↓
Login with Valid Credentials
      |
      ↓
Verify Home Page
      |
      ↓
Click Events Tab
      |
      ↓
Verify URL
      |
      ↓
Verify Page Content
      |
      ↓
Capture Screenshots
      |
      ↓
Generate Logs & HTML Report
      |
      ↓
Test Passed
```

---

## 🎯 Future Enhancements

* Data Driven Testing
* Cross Browser Testing
* Jenkins CI/CD Integration
* Allure Reporting
* Parallel Test Execution
* API Testing Integration

---

## 👩‍💻 Author

**Pallabi Bhowmick**

QA Automation Engineer

### Skills

* Selenium WebDriver
* Python
* Java
* PyTest
* TestNG
* API Testing
* Manual Testing
* Automation Framework Development
* Git & GitHub

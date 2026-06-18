# Selenium Python Automation Framework

## 📌 Project Overview

This project is a Selenium WebDriver automation framework built using **Python** and the **Page Object Model (POM)** design pattern.

The framework automates the following user flow:

* Open EventHub application
* Login with valid credentials
* Navigate to the Events page
* Verify the Events page URL
* Validate Events page content

This project demonstrates real-world QA Automation practices including:

* Page Object Model (POM)
* Selenium WebDriver
* Explicit Waits
* Assertions
* Test Flow Automation

---

## 🛠️ Technologies Used

| Technology         | Purpose                   |
| ------------------ | ------------------------- |
| Python             | Programming Language      |
| Selenium WebDriver | Web UI Automation         |
| PyTest             | Test Execution Framework  |
| WebDriver Manager  | Browser Driver Management |
| Chrome Browser     | Test Execution            |
| Git & GitHub       | Version Control           |

---

## 📂 Project Structure

```
EVENTHUBAUTOMATION
│
├── pages
│   ├── login_page.py
│   └── event_page.py
│
├── test_pages.py
│
├── requirements.txt
│
└── README.md
```

---

## 📄 Page Object Model Design

### Login Page

Contains:

* Username field
* Password field
* Login button
* Login functionality

### Event Page

Contains:

* Events navigation tab
* Event page verification
* Page text validation

---

## ⚙️ Installation & Setup

### 1. Clone Repository

```bash
git clone <your-github-repository-url>
```

Navigate into the project folder:

```bash
cd Selenium-Python-Automation
```

---

### 2. Create Virtual Environment

```bash
python -m venv venv
```

Activate the environment:

Windows:

```bash
venv\Scripts\activate
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run Test

Execute the test using:

```bash
python test_pages.py
```

---

## 🔄 Automation Flow

```
Launch Browser
       |
       ↓
Open Login Page
       |
       ↓
Enter Username
       |
       ↓
Enter Password
       |
       ↓
Click Login
       |
       ↓
Navigate to Events
       |
       ↓
Verify URL
       |
       ↓
Verify Page Content
       |
       ↓
Test Passed
```

---

## ✅ Test Scenarios Covered

| Test Case                    | Status |
| ---------------------------- | ------ |
| Launch Application           | ✔      |
| Login with valid credentials | ✔      |
| Navigate to Events page      | ✔      |
| Verify Event URL             | ✔      |
| Verify Event page text       | ✔      |

---

## 📸 Test Execution Output

Example:

```
Login Test Passed

Event URL Verified

Event Page Text Verified

EVENT TEST PASSED
```

---

## 🚀 Future Enhancements

* Add PyTest fixtures
* Add HTML test reports
* Add screenshots on failure
* Add logging framework
* Add CI/CD pipeline using GitHub Actions or Jenkins
* Add Data-Driven Testing

---

## 👩‍💻 Author

**Pallabi**

QA Automation Engineer

### Skills

* Selenium Python
* Java Selenium
* API Testing
* Manual Testing
* Test Automation Frameworks

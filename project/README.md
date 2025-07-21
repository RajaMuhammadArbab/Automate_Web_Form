# Automated Web Form Submission with Selenium

## Project Description
This project automates the task of filling out and submitting a web form multiple times using data from a CSV file. It uses Python and Selenium WebDriver to simulate user interactions in a Chrome browser.

---

## ✅ Features
- Reads data from `form_data.csv`
- Automatically fills out a local HTML form
- Handles text inputs, radio buttons, checkboxes, and dropdowns
- Logs submission status for each row
- Includes a styled `form.html` for local testing

---

## Folder Structure
```
form_automation_project/
├── main.py                    # Python automation script
├── form_data.csv              # CSV file with test data
├── form.html                  # Local form for testing
├── chromedriver.exe           # ChromeDriver (must match your Chrome version)
├── submission_log.txt         # Generated log file
├── requirements.txt           # Python dependencies
```

---

##  Setup Instructions

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Download ChromeDriver
Download ChromeDriver that matches your Chrome browser version:  
🔗 https://googlechromelabs.github.io/chrome-for-testing/

Extract `chromedriver.exe` into the project folder.

---

### 3. Run the Script
```bash
python form_auto_submitter.py
```

This will open Chrome, fill the form using data from the CSV, and submit it for each row.

---

##  Sample CSV Data (`form_data.csv`)
```csv
name,email,address,gender,subscribe,city
Hamza,hamza@gmail.com,bismillahtown,Male,yes,karachi
Qayoom,Qayoom@gmail.com,latifabadno12,Male,yes ,Hyd
anas,anas@gmail.com,latifabadno10,Male,no,lahore
Hassan,hassan@gmail.com,latifabad no 05,Male,yes,Hyd
Hadi,hadi@gmail.com0,latifabad no 09,Male,no,lahore
nimra,nimra@gmail.com,korangi,female,yes,karachi
zarnab,zarnab@gmail.com,zealpak,female,no,Hyd

```

---

##  Notes
- Make sure `form.html`, `form_data.csv`, and `chromedriver.exe` are in the **same folder**.
- The browser will reload the form after each submission.
- Check `submission_log.txt` for results or errors.

---

##  Contact
Developed by Raja Muhammad Arbab

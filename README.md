# Red Team Toolkit Manager

A centralized and efficient GUI-based toolkit designed for Red Team operators, ethical hackers, and penetration testers.  
Built using **Python (Tkinter)** and **MySQL**, this project streamlines offensive security workflows by managing targets, exploits, payloads, credentials, and more — all in one unified system.

---

## Features

### Dashboard  
A clean and responsive interface providing access to all modules.

### Attack Recommendation System  
Recommends the best attack methods based on:
- Target OS  
- Attack type  
- Open ports  
- Available tools  

### Target Manager  
Add, delete, edit, and manage:
- Target name  
- IP address  
- OS  
- Description  
- Notes  

### Wordlist Generator  
Generate personalized password wordlists using custom fields:
- Name  
- DOB  
- Pet name  
- Favorites  
- Nicknames  
- Patterns  
Supports saving templates.

### Exploit Database  
Search, add, and update exploit entries including:
- CVE  
- Category  
- Severity  
- Description  
- Usage commands  

### Payload Generator  
Generate Metasploit payloads for:
- Windows  
- Linux  
- Android  
- macOS  
Automatically saves payload commands to the database.

### Toolkit Inventory  
Manage all tools with:
- Name  
- Type  
- Version  
- Description  

### Success Probability Calculator  
Estimates probability using:
- Attack type  
- Target OS  
- Open ports  
- Tool availability  

---

## Tech Stack

- **Python (Tkinter GUI)**
- **MySQL**
- **Pyperclip**
- **CSV / itertools / OS modules**

---

## Installation

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/RedTeamToolkitManager.git
cd RedTeamToolkitManager
```
### 2. Install Dependencies
```bash
pip install mysql-connector-python pyperclip
```
### 3. Configure MySQL
```bash
CREATE DATABASE RTTM;
```
**Create required tables:**

- users

- target_manager

- exploit_database

- payloads

- toolkit_inventory

- attack_recommendation

### 4. Run the Application
```bash
python login.py
```

 ## Project Structure
 ``` bash
/RTTM
│── login.py
│── dashboard.py
│── attack_recommendation.py
│── target_manager.py
│── exploit_database.py
│── payload_generator.py
│── wordlist_generator.py
│── success_probability_calculator.py
│── profile.py
└── README.md
```

## Author

### Aditya Sharma
- Aspiring Red Teamer • Cybersecurity Enthusiast
- Skilled in Python, Networking, JS, PHP, SQL & Offensive Security Concepts.

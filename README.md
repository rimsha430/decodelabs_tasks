 ✅ To-Do List App

A simple console-based To-Do List application built with Python, where users can add, view, and manage their daily tasks efficiently. The program provides an interactive menu and keeps track of all tasks until the user chooses to exit.

 Project Overview:

This project demonstrates the fundamentals of Python programming through an interactive command-line to-do list manager. It utilizes loops, conditional statements, lists, and user input handling to create a simple and practical productivity tool.

 ✨ Features

- ➕ Add new tasks to the list
- 📋 View all current tasks
- ✔️ Mark tasks as completed
- 🗑️ Delete tasks from the list
- 🔁 Continuous menu-driven interaction until the user exits

 🛠️ Technologies Used

- Python 3

 ▶️ How to Run

```bash
python "to do list.py"

 

Task 2: Expense Tracker

A simple console-based Expense Tracker application built with Python, where users can enter multiple expenses and get the running total. The program keeps track of the total amount spent until the user chooses to stop.

**File:** `expense tracker.py`

 Features
- Enter expense amounts one by one
- Displays the current running total after each entry
- Validates input (rejects negative numbers and invalid text)
- Type `done` to stop entering expenses and see the final total

 How to Run
```bash
python "expense tracker.py"

 Task 3: Secure Password Generator

A cryptographically secure password generator built with Python. It uses the `secrets` module (instead of `random`) to generate strong, unpredictable passwords, and calculates the password's entropy to mathematically demonstrate its strength.

**File:** `password_generator.py`

 Features
- Validates user input to ensure a minimum password length of 8 characters
- Generates passwords using letters (uppercase & lowercase) and digits
- Uses `secrets.choice()` for cryptographically secure randomness (safer than the standard `random` module)
- Efficient string building using `.join()` for optimal performance
- Calculates and displays password entropy (in bits) using the formula `E = L × log2(R)`, where L is password length and R is the character pool size

 How to Run
```bash
python password_generator.py

👤 Author

Rimsha Sheraz — DecodeLabs Intern

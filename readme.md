# Square Calculator

A simple, user-friendly Python script that calculates the square of a number provided by the user. This project demonstrates basic input handling, arithmetic operations, and the difference between numeric data types in Python.

---

## 🚀 Features
* **User Interaction:** Prompts the user for numerical input.
* **Dual Calculation Methods:** Demonstrates squaring via multiplication (`a * a`) and the exponentiation operator (`a ** 2`).
* **Flexibility:** Uses `float` to support both whole numbers and decimals.
  
## 📋 How It Works

The script follows a logical flow to transform user input into a mathematical result. Here is a breakdown of the process:

### 1. Data Type Selection: `int` vs `float`
The program must decide how to "read" the user's typing. In Python, there is a key difference between these two types:
* **Integers (`int`):** Used for whole numbers (e.g., `5`, `-10`).
* **Floats (`float`):** Used for numbers with decimal points (e.g., `5.0`, `3.14`).

By using `float(input())`, the script becomes more inclusive. It can process a whole number like `7` (by treating it as `7.0`) while also supporting decimal inputs like `2.5`, which would otherwise cause an error if `int()` were used.

### 2. Squaring Logic
The script demonstrates that there is often more than one way to solve a problem in programming. It offers two methods for squaring:

* **Multiplication Method:** Multiplying the variable by itself (`a * a`). This is the most basic algebraic approach.
* **Exponentiation Method:** Using the power operator (`a ** 2`). In Python, `**` represents "to the power of."

### 3. The Execution Flow
1.  **Greeting:** A "Welcome" message is printed to the console.
2.  **Capture:** The `input()` function pauses execution to wait for the user.
3.  **Conversion:** The text entered by the user is converted from a string to a `float`.
4.  **Math:** The calculation is performed instantly.
5.  **Output:** The final result is concatenated with a string and displayed to the user.

## 💻 Usage

To get the calculator running on your local machine, follow these steps:

### 1. Save the Script
Copy the code and save it into a file on your computer. You can use any text editor (like Notepad, VS Code, or TextEdit).
* **Filename:** `square_calculator.py`

### 2. Open Your Terminal
You need to use a command-line interface to run the script.
* **Windows:** Search for `cmd` or `PowerShell`.
* **Mac/Linux:** Open the `Terminal` app.

### 3. Navigate and Run
Use the `cd` command to move to the folder where you saved your file, then execute the script using Python:

```bash
# Navigate to your folder (example)
cd path/to/your/folder

# Run the script
python square_calculator.py

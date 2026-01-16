

**Name:** Olanusi Oluwaseyitan  
**Matric No:** 24/15032  
**Department:** Computer Science  

**GitHub Repository:**  
[Electricity-bill-calculator](https://github.com/Oluwaseyitan-dot/Electricity-bill-calculator.git)

---

## 1. Requirement Analysis

This stage focuses on clearly understanding the problem.

### Project Requirements
- The system should calculate electricity bills.
- The user should enter the number of units consumed.
- The system should use a fixed rate of **₦50 per unit**.
- The system should display the total bill.
- The system should keep running until the user chooses to exit.

### Functional Requirements
- Accept user input (units).
- Multiply units by the fixed rate.
- Display the calculated bill.
- Provide menu options (Calculate Bill / Exit).

### Non-Functional Requirements
- Program should be simple and user-friendly.
- Program should be fast and accurate.
- Program should not crash on wrong menu input.

---

## 2. System Design

This stage describes how the program will work internally.

### Design Decisions
- Use **Python** as the programming language.
- Use functions to organize the program:
  - `calculate_bill()` → handles bill calculation.
  - `main()` → handles menu and program flow.
- Use a `while` loop to keep the program running.
- Use a fixed rate of **₦50 per unit**.

### Logical Design (Algorithm)
1. Display menu  
2. Ask user for choice  
3. If choice = 1:
   - Ask for units
   - Calculate bill
   - Display bill  
4. If choice = 2:
   - Exit program  
5. Else:
   - Display **"Invalid option"**  
6. Repeat until user exits  

---

## 3. Implementation (Coding Stage)

This is where the system design is converted into code.

### Implemented Features
- Input handling using `input()`
- Arithmetic calculation using `units * rate`
- Menu display using `print()`
- Looping using `while True`
- Decision making using `if`, `elif`, `else`
- Modular programming using functions

---

## 4. Testing

Testing ensures the program works as expected.

### Test Cases

| Test Case             | Input        | Expected Output        |
|----------------------|--------------|------------------------|
| Normal case          | Units = 10   | Bill = ₦500            |
| Zero units           | Units = 0    | Bill = ₦0              |
| Decimal input        | Units = 2.5  | Bill = ₦125            |
| Invalid menu choice  | 5            | "Invalid option"       |
| Exit option          | 2            | Program exits          |

### Testing Types Used
- **Unit Testing:** Testing the `calculate_bill()` function
- **System Testing:** Running the full program
- **Manual Testing:** User enters inputs manually

---

## 5. Deployment

This stage makes the software available for use.

### Deployment Details
- The program can be run from:
  - Terminal
  - Command Prompt
  - Python IDEs (VS Code, PyCharm, etc.)
- The `.py` file can be shared with others.

### Example Command
```bash
python electricity_bill.py
6. Maintenance
Maintenance involves improving or fixing the program after deployment.

Possible Future Improvements
Allow different rates per unit.

Add error handling for negative inputs.

Store bills in a file or database.

Add a graphical user interface (GUI).

Support multiple customers.

Example Maintenance Update
python
Copy code
if units < 0:
    print("Invalid units entered")
7. Documentation
This section explains how the system works.

User Documentation
Run the program.

Choose option 1 to calculate the bill.

Enter the number of units consumed.

Choose option 2 to exit the program.

Technical Documentation
Program is written in Python.

Uses functions and control structures.

Copy code


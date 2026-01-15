# Electricity-bill-calculator
* Name : Olanusi Oluwaseyitan
* Matric no : 24/15032
* Department : Computer science

# The URL: https://github.com/Oluwaseyitan-dot/Electricity-bill-calculator.git


# 1. Requirement Analysis

This is where the problem is clearly understood.

Requirements for this project:
	•	The system should calculate electricity bill.
	•	The user should enter the number of units consumed.
	•	The system should use a fixed rate (₦50 per unit).
	•	The system should display the total bill.
	•	The system should keep running until the user chooses to exit.

Functional Requirements:
	•	Accept user input (units).
	•	Multiply units by rate.
	•	Display result.
	•	Provide menu options (Calculate Bill / Exit).

Non-Functional Requirements:
	•	Program should be simple and user-friendly.
	•	Program should be fast and accurate.
	•	Program should not crash on wrong menu input.


# 2. System Design

This stage decides how the program will work internally.

Design Decisions:
	•	Use Python as the programming language.
	•	Use functions to organize the program:
	•	calculate_bill() → handles bill calculation.
	•	main() → handles menu and program flow.
	•	Use a while loop to keep the program running.
	•	Use a fixed rate (₦50 per unit).

Logical Design (Algorithm):
	1.	Display menu
	2.	Ask user for choice
	3.	If choice = 1:
	•	Ask for units
	•	Calculate bill
	•	Display bill
	4.	If choice = 2:
	•	Exit program
	5.	Else:
	•	Display “Invalid option”
	6.	Repeat until exit
  
 3. Implementation (Coding Stage)

This is where the design is converted into actual code.

Implemented Features in Your Code:
	•	Input handling using input()
	•	Arithmetic calculation using units * rate
	•	Menu using print()
	•	Loop using while True
	•	Conditional statements using if, elif, else
	•	Modular programming using functions

#  4. Testing

Testing ensures the program works as expected.
# Test Cases:

Test Case
Input
Expected Output
Normal case
Units = 10
Bill = 500
Zero units
Units = 0
Bill = 0
Decimal input
Units = 2.5
Bill = 125
Invalid menu choice
5
“Invalid option”
Exit option
2
Program exits

 Testing Type Used:
	•	Unit Testing → testing calculate_bill() function
	•	System Testing → running the full program
	•	Manual Testing → user enters inputs manually


5. Deployment

This stage makes the software available for use.

 For this project:
	•	The program is run from:
	•	Terminal
	•	Command Prompt
	•	Python IDE (VS Code, PyCharm, etc.)
	•	The .py file can be shared with others.

 # Example:
  python electricity_bill.py

 # 6. Maintenance

This involves improving or fixing the program after deployment.

Possible Future Improvements:
	•	Allow different rates per unit.
	•	Add error handling for negative input.
	•	Store bills in a file or database.
	•	Add GUI interface.
	•	Support multiple customers.

Example Maintenance Update:
if units < 0:
    print("Invalid units entered")


   # 7. Documentation

This explains how the system works.

User Documentation:
	•	Run the program
	•	Choose option 1 to calculate bill
	•	Enter units
	•	Choose option 2 to exit

Technical Documentation:
	•	Written in Python
	•	Uses functions
	•	Menu-driven program
	•	Fixed rate billing system

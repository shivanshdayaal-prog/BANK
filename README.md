Banking System 

Overview of the Project

This project is an application developed in Python that simulates the core functionality of a bank's account management and transaction system. The system uses a simple in-memory dictionary (bank_record) to store account data, focusing on demonstrating procedural logic, user input validation, and fundamental security checks.
The application operates through an interactive menu loop that runs in the console.

Features

The system offers the following functionalities, with security enforced through PIN verification for most operations:

Create New Account: Generates a unique 5-digit account number and allows the user to set a 4-digit PIN, name, mobile number, and initial deposit.
Deposit Amount: Adds funds to an existing account after verifying the PIN.
Withdraw Amount: Removes funds from an account, verifying the PIN and checking for sufficient balance to prevent overdrafts.
Check Balance: Displays the current balance and account type after successful PIN verification.
All Account Holder List: An administrative function that displays all active accounts (requires admin_pin).
Close Account: Permanently deletes an account from the system after PIN verification.
Change Mobile No.: Allows the user to update their contact number after PIN verification.
Exit: Shuts down the application.

Technologies/Tools Used

Language: Python 3.x (Standard Library)
Data Storage: Python Dictionary (In-Memory)
Modules: random

Steps to Install & Run the Project

Since this project uses only standard Python libraries, installation is simple:

Save the file: Save the source code content into a file named cli_bank_system_v2.py.
Open Terminal/Command Prompt: Navigate to the directory where you saved the file.
Run the script: Execute the program using the Python interpreter:
cs final code.py

Instructions for Testing

Test the application by focusing on input robustness and transaction security:
Account Creation: Create a test account (e.g., Account 12345, PIN 9999).
Input Validation (Reliability):
Attempt to enter text for the PIN, Account Number, and Deposit fields. The program should catch the ValueError and prompt for re-entry (or return to the menu).
Attempt to deposit a negative amount.
Security Check:
Try to check the balance of Account 12345 using an incorrect PIN (e.g., 1111). Verification should fail.
Transaction Flow:
Deposit 200 into the account.
Withdraw 50 (Successful).
Attempt to withdraw an amount larger than the current balance (Overdraft check).
Admin Access: Access option 5 using the hardcoded admin_pin (pass123) to view all created records.

Screenshots

Provided in the document in repository.

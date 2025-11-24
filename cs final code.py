import random

bank_record = {}
created_accounts = set()
admin_pin = "pass123"

def account_number_generation():
    while True:
        acc_no = random.randint(10000, 99999)
        if acc_no not in created_accounts and acc_no not in bank_record:
            created_accounts.add(acc_no)
            return acc_no
       
def account_number_input():
    while True:
        account = int(input("Enter Account Number: "))
        if len(str(account))== 5:
            return account
        else:
            print("Invalid account number. Please enter a 5-digit number.")

def pin_input():
    while True:
        pin = int(input("Set a 4-digit PIN: "))
        if len(str(pin)) == 4:
            return pin
        else:
            print("Invalid PIN")

def create_account():
    print("\n--- CREATE NEW ACCOUNT ---")

    name= input("Enter Your Name: ")
    mobile= int(input("Enter Your Mobile No: "))
    if len(str(mobile)) > 10:
        print("Invalid Mobile Number. Please enter a valid number.")
        return
    acc_type= input("Enter Account Type (Savings/Current): ")
    deposit= int(input("Enter Initial Deposit Amount: "))
    pin= pin_input()
    acc_num= account_number_generation()

    bank_record[acc_num] = {
        "name": name,
        "mobile": mobile,
        "pin": pin,
        "type": acc_type,
        "balance": deposit
    }

    print(f"\nAccount Successfully Created.")
    print(f"IMPORTANT: Your Account Number is: {acc_num} and PIN is: {pin}")

def deposit_amount():
    print("\n--- DEPOSIT AMOUNT ---")
    
    acc_num = account_number_input()
    entered_pin= int(input("Enter Account PIN: "))

    if acc_num not in bank_record:
        print("Sorry, Account not found.")
        return
    
    elif acc_num in bank_record and entered_pin != bank_record[acc_num]['pin']:
        print("Incorrect PIN.")

    elif acc_num in bank_record and entered_pin == bank_record[acc_num]['pin']:
        amount = int(input("Enter Amount to be Deposited: "))
        
        if amount > 0 :
            bank_record[acc_num]['balance'] += amount
            print(f"Success!\nDeposited amount: {amount}\nNew Balance: {bank_record[acc_num]['balance']}")
        else:
            print("Deposit amount must be greater than zero.")
        
def withdraw_amount():
    print("\n--- WITHDRAW AMOUNT ---")
    
    acc_num = account_number_input()
    entered_pin= int(input("Enter Account PIN: "))

    if acc_num not in bank_record:
        print("Sorry, Account not found.")
        return
    
    elif acc_num in bank_record and entered_pin != bank_record[acc_num]['pin']:
        print("Incorrect PIN.")

    elif acc_num in bank_record and entered_pin == bank_record[acc_num]['pin']:        
        amount = int(input(("Enter Amount to Withdraw: ")))
        current_balance = bank_record[acc_num]['balance']
        
        if amount <= current_balance and amount > 0:
            bank_record[acc_num]['balance'] -= amount
            print(f"Success. Withdrawn: {amount}")
            print(f"Remaining Balance: {bank_record[acc_num]['balance']}")
        else:
            print(f"Insufficient Funds.\nCurrent Balance: {current_balance}")

def balance_enquiry():
    print("\n--- BALANCE ENQUIRY ---")

    acc_num = account_number_input()
    entered_pin= int(input("Enter Account PIN: "))

    if acc_num not in bank_record:
        print("Sorry, Account not found.")
        return
    
    elif acc_num in bank_record and entered_pin != bank_record[acc_num]['pin']:
        print("Incorrect PIN.")
        
    elif acc_num in bank_record and entered_pin == bank_record[acc_num]['pin']:
        bal = bank_record[acc_num]['balance']
        name = bank_record[acc_num]['name']
        print(f"\nAccount Holder: {name}")
        print(f"Account Type: {bank_record[acc_num]['type']}")
        print(f"Current Balance: {bal}")

def display_all_accounts():
    print("\n--- ALL ACCOUNTS ---")

    password = input("Enter Password: ")
    
    if password == admin_pin:
        if not bank_record:
            print("No accounts exist in the system.")
        else:
            print("---------------------------------------------")
            print("Account No, Name, Mobile, Type, Balance")
            print("---------------------------------------------")
            for acc_num, details in bank_record.items():
                print(f"{acc_num}, {details['name']}, {details['mobile']}, {details['type']}, {details['balance']}")
                print("--------------------------------------------------")
    else:
        print("Incorrect Password.")

def close_account():
    print("\n--- CLOSE ACCOUNT ---")

    acc_num = account_number_input()
    entered_pin= int(input("Enter Account PIN: "))

    if acc_num not in bank_record:
        print("Sorry, Account not found.")
        return
    
    elif acc_num in bank_record and entered_pin != bank_record[acc_num]['pin']:
        print("Incorrect PIN.")

    elif acc_num in bank_record and entered_pin == bank_record[acc_num]['pin']:
        confirm = input(f"Are you sure you want to delete account {acc_num}? (y/Y/n//N): ").lower()
        if confirm == 'y'or 'Y':
            del bank_record[acc_num]
            created_accounts.discard(acc_num)
            print("Account closed successfully. Have A Nice Day!")
        else:
            print("Operation cancelled.")

def modify_account():
    print("\n--- MODIFY ACCOUNT ---")

    acc_num = account_number_input()
    entered_pin= int(input("Enter Account PIN: "))

    if acc_num not in bank_record:
        print("Sorry, Account not found.")
        return
    
    elif acc_num in bank_record and entered_pin != bank_record[acc_num]['pin']:
        print("Incorrect PIN.")

    elif acc_num in bank_record and entered_pin == bank_record[acc_num]['pin']:
        print(f"Current Mobile for {acc_num}: {bank_record[acc_num]['mobile']}")

        new_mobile = int(input(("Enter New Mobile Number: ")))
        if len(str(new_mobile)) > 10:
            print("Invalid Mobile Number. Update failed.")
            return
        else:
            bank_record[acc_num]['mobile']= new_mobile
            print("Mobile number updated successfully")

while True:
    print("\nWelcome to the Online Banking System.")
    print("\n====================================")
    print("             MAIN MENU                     ")
    print("====================================")
    print("1. CREATE NEW ACCOUNT")
    print("2. DEPOSIT AMOUNT")
    print("3. WITHDRAW AMOUNT")
    print("4. CHECK BALANCE")
    print("5. ALL ACCOUNT HOLDER LIST")
    print("6. CLOSE ACCOUNT")
    print("7. CHANGE MOBILE NO.")
    print("8. EXIT")

    choice = input("Enter Your Option (1 to 8): ")

    if choice == '1':
        create_account()
    elif choice == '2':
        deposit_amount()
    elif choice == '3':
        withdraw_amount()
    elif choice == '4':
        balance_enquiry()
    elif choice == '5':
        display_all_accounts()
    elif choice == '6':
        close_account()
    elif choice == '7':
        modify_account()
    elif choice == '8':
        print("Thank you for using the system")
        break
    else:
        print("Invalid Choice. Enter a number between 1 and 8")
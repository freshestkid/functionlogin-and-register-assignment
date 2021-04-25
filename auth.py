import random
import dictionary

database = {}

def init():

    print("Welcome to Access Bank Plc")

    have_an_account = int(input("Do you have an account with us: 1 (Yes) 2 (No) \n")

    if(have_an_account == 1):   
        login()
        
    elif(have_an_account == 2):
        register()

     else:
        print("You have selected an invalid option")
        init()


def login():

    print("*********** Login **********")

    account_number_from_user = int(input("What is your account number \n"))
    password = input("What is your password \n")
     
     for account_number,user_details in database.item():
        if(account_number == account_number_from_user):
             if(user_details[3] == password):
                bank_operation(user_details)
       
       
     print("Invalid account number or Password")
     login()


def register():

    print("****** Register ******")

    email = input("What is your email address? \n")
    first_name = input("What is your first name? \n")
    last_name = input("What is your last name? \n")
    other_name = input("What is your middle name? \n")
    password = input("create a password for yourself \n")

    account_number = genration_account_number()

    database[account_number] = [first_name, last_name, other_name, email, password, 0]

    print("Your account has been successfully created")
    print("====== ====== ============ ==============")
    print("Your account number is: %d" % account_number)
    print("Keep your acount number safe")
    print("======== ============= ==================")

    login()

def bank_operation(user):

    print("Welcome %s %s " % ( user[0], user[1], user[2] ))
    selected_operation = int(input"What would you like to do? (1) Deposit (2) Withdrwal (3)Balance Enquiry (4)Transfer (5) Logout (6) Exit")

    if(selected_operation = 1):
       
        deposit_operation()
    elif(selected_operation = 2):

        withdrawal_operation()
    elif(selected_operation = 3):

        Balance_enquiry_operation()
    elif(selected_operation = 4):

        transfer_operation()
    elif(selected_operation = 5):

        Logout()
    elif(selected_operation = 6):

        exit()

    else:

        print("Invalid option slected")
        bankOperation(user)

def deposit_operation():
    deposit_amount=int(input("please enter deposit_amount \n" ))
        balance=current_balance+deposit_amount
        print(f"{deposit_amount} has been credited to your account")
        print("int(current_balance),  Thank you") 

def withdrawal_operation():
    withdraw_amount=int(input("please enter withdraw_amount \n" ))
        balance=balance-withdraw_amount
        print(f"{withdraw_amount} has been debited from your account")
        print("Take your cash")
        print(f"your current balance is {balance}")

def Balance_enquiry_operation(user_details):
    return usser_details[4]

def generationAccountNumber():

    return randon.randrange(000000000,999999999)


int()
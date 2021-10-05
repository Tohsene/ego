#Simple Python Bank Program
import random
import time
account_det = {"Tosi":"6000"}
bank_user = {"0705566109":"1234"}
account_bal = 0

for i in range(10000):
    
    chat_bot = input("Do you have an account with us Yes or No?\n>").lower()

    if chat_bot == "yes":
        account_no = input("Enter your account number\n>")
        account_pin = input("Enter your account pin\n>")

        time.sleep(3)

        if account_no in bank_user.keys():
            actual_pin = bank_user.get(account_no)

            if actual_pin == account_pin:
                print(f"welcome \n>")
                con = input("press 'w' to withdraw, 'd' to deposit, 't' to transfer\n>")

                if con == 'w':
                    withdraw = int(input("How much do you want to withdraw?\n>"))
                    
                    time.sleep(3)

                    if (withdraw > account_bal):
                        print("Insufficient Funds") 
                    else:
                        account_bal -= withdraw
                        print("Please take your money /n Remaining Account balance is:\n", account_bal)

                elif con == 'd':
                    deposit = int(input("How much do you want to deposit?\n>"))

                    time.sleep(3)

                    account_bal += deposit
                    print("Credit Alert!!!\n Your account has been credited with ", deposit, "\nYour new balance is: ", account_bal)

                elif con == 't':
                    transfer = int(input("How much do you want to transfer?\n"))
                    recipient_no = int(input("Enter recipient's account number?\n"))

                    time.sleep(3)

                    if (transfer > account_bal):
                        print("Insufficient Funds") 
                    else:
                        account_bal -= transfer
                        print("Sent.\n Remaining Account balance is:\n", account_bal) 
                
                else:
                    print("invalid input. Try again")
                
            else:
                print("Your account number/pin is incorrect")

        else:
            print("No active user")

    elif chat_bot == "no":
        full_name = input("Enter your fullname")
        account_pin = input("Enter an account pin.\n Note: it must be numbers and must not be more than four\n>")
        
        if len(account_pin) > 0 and len(account_pin) < 5:
            confirm_pin = input("Enter pin again\n>")

            if account_pin == confirm_pin:
                print(f"Welcome {full_name}!\n Please wait for some seconds to generate your account number")
                
                time.sleep(5)

                mylist = []
                for i in range(0,10):
                    x= random.randint(0,9)
                    mylist.append(x)
                       
                account_no = int(''.join(map(str, mylist)))
                
                print("Your account number is: ", account_no)
                
                bank_user[account_no] = account_pin
                
            else:
                print("Pin is not a match")

        else:
            print("pin is not valid")       

    else:
        print("Please select a valid option")




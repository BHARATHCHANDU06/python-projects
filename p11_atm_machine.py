print("WELCOME TO RBC ATM")
print("select language")
print("1. English")
print("2. Telugu")
print("3. Hindi")
choose=int(input("Enter your choice:(1-3):"))
if choose==1:
    print("You have selected English.")
elif choose==2:
    print("You have selected Telugu.")
elif choose==3:
    print("You have selected Hindi.")
else:
    print("Invalid choice! Please select a valid language.")
secret_number=7616
print("Enter your ATM pin number:")
atm_pin=(int(input()))
if atm_pin==secret_number:
    print("Enter the choice:")
    print("1. Check Balance")
    print("2. Withdraw Cash")
    print("3. Deposit Cash")
    print("4. Change Pin")
    print("5. Exit")
    choice=int(input("Enter your choice(1-5):"))
    if choice==1:
        balance=10000
        print("Your current balance is:",balance)
    elif choice==2:
        print("Enter your Amount to withdraw:")
        amount=int(input())
        if amount<=10000:
         balance=10000-amount
        print("TRANSACTION SUCCESSFUL! Please collect your cash.")  
    elif choice==3:
         print("Enter your Amount to deposit:")
         amount=int(input())
         balance=10000+amount
         print("Your cash has been deposited successfully.")
    elif choice==4:
        print("Enter your new pin number:")
        new_pin=int(input())
        print("Your pin number has been changed successfully.")
    elif choice==5:
        print("==PLEASE TAKE YOUR CARD==")
    print("THANK YOU FOR USING RBC ATM. HAVE A NICE DAY!")
else:
    print("Invalid pin number! Please enter a valid pin number.")

   
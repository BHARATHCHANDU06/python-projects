class BankAccount:
    def __init__(self,account_number,account_holder_name,account_type,balance):
            self.account_number = account_number
            self.account_holder_name = account_holder_name
            self.account_type = account_type
            self.balance = balance
    def deposit(self, amount):
            self.balance=self.balance + amount
            print("Amount deposited sucessfully!.")  
    def withdraw(self, amount):
           if amount > self.balance:
                print("Insufficient balance!.")
           else:
                self.balance = self.balance - amount
                print("Amount withdrawn successfully!.")
                print("New Balance:", self.balance)
    def display_account_details(self):
        print("Account Number:", self.account_number)
        print("Account Holder Name:", self.account_holder_name)
        print("Account Type:", self.account_type)
        print("Balance:", self.balance)
account1 = BankAccount("1234567890", "Chandu", "Savings", 1000)
account1.display_account_details()
account1.deposit(2000)
account1.withdraw(500)
account1.display_account_details()
while True:
        print("1.check balance")
        print("2.deposit")
        print("3.withdraw")
        print("4.display account details")
        print("5.exit")
        choice=int(input("Enter your choice(1-5):"))
        if choice==1:
         print("Current Balance:", account1.balance)
        elif choice==2:
         amount=float(input("Enter the amount to deposit:"))
         account1.deposit(amount)
        elif choice==3:
         amount=float(input("Enter the amount to withdraw:"))
         account1.withdraw(amount)
        elif choice==4:
         account1.display_account_details()      
        elif choice==5:
         print("Exiting the program...")
         break
        else:
         print("Invalid choice! Please try again.")     
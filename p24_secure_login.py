class User:
    def __init__(self,user_name,password):
        self.user_name=user_name
        self.password=password
class LoginSystem:
    def __init__(self):
        self.users=[]
    def register(self):
        user_name=input("Enter username:")
        password=input("Enter password:")
        user=User(user_name,password)
        self.users.append(user)
        print("Registration successful!")
    def login(self):
        user_name=input("Enter username:")
        password=input("Enter password:")
        for user in self.users:
            if user.user_name==user_name and user.password==password:
                print("Login successfull!")
                return
            print("Invalid username or password!")
system=LoginSystem()
system.register()
system.login()

password=input("enter your password:")
length=len(password)
has_upper= False
has_lower= False
has_digit= False
for char in password:
    if char.isupper():
        has_upper= True
    if char.islower:
        has_lower= True
    if char.isdigit():
        has_digit= True
print("\n-----Result-----")
if length>=8 and has_upper and has_lower and has_digit:
    print("Strong Password")
elif length>=6 and has_digit and (has_upper or has_lower):
    print("Medium Password")
else:
    print("Weak Password")
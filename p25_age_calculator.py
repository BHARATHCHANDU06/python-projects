from datetime import date
today=date.today()
print("Today's date:",today)
birth_year=int(input("Enter your birth year:"))
birth_month=int(input("Enter your birth month:"))
birth_day=int(input("Enter your birth day:"))
birth_date=date(birth_year,birth_month,birth_day)
age=today.year-birth_date.year
if (today.month,today.day)<(birth_date.month,birth_date.day):
    age-=1
print("Your age is:",age)
import datetime

print("We're gonna find out what day of the week your birthday falls on!!")
print("Press 'q' at anytime to quit.")

user_year = int(input("\nEnter the year you want to know about: "))
user_month = int(input("Enter your birth month in the following format (mm): "))
user_day = int(input("Enter your day of birth in the following format (dd): "))

user_bday = datetime.datetime(user_year, user_month, user_day)
user_dow = user_bday.strftime("%A")
print(user_dow)
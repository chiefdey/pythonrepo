# Write a program that takes the date of birth of a person and the program outputs the age in terms of years,months,days TODAY.
# import datetime


# dob=input("enter dob (dd/mm/yyy)")
# dmy=dob.split('/')
# if len(dmy)==3:
#     d=int(dmy[0])
    
from datetime import date

def calculate_age(birth_date):
    today = date.today()
    age = today.year - birth_date.year
    full_year_passed = (today.month, today.day) < (birth_date.month, birth_date.day)
    if not full_year_passed:
        age -= 1
    return age

# Example usage:
birth_date = input('enter dob')
age = calculate_age(birth_date)
print(f"Age: {age} years")

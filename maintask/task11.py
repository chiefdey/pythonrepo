# Write a program that takes the date of birth of a person and the program outputs the age in terms of years,months,days TODAY.
import datetime


dob=input("enter dob (dd/mm/yyy)")
dmy=dob.split('/')
if len(dmy)==3:
    d=int(dmy[0])
    
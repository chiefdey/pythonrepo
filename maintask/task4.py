# Write a program which accepts email as form input or from terminal. Validate the email by checking if it's a valid email
email=input('enter email').split("@")
if email.count('a')==1 :
    print(email) 
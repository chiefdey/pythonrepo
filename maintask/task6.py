# Write a program input a password. Give them only 4 attempts to check the passwords entered against “admin@123”. If the password is correct access is granted. After you show them a message , the account is blocked.

for i in range(0,4):
    pswd=input('enter password: ')
    if pswd=="admin@123":
        print(pswd,"login successful")
        break
    else:
        print('invalid password.retry')
    if i==3:
        print("blocked")


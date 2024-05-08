# Write a program that takes the email and password as input from a user and checks if they are equal to “admin@mail.com” and password is “Admin@123” , if so then print  “Login is Successful” and if not print “Invalid username or password”. ONLY accept 3 tries after which it notifies you that you have been blocked.
for i in range(0,4):
    pswd=input('enter password: ')
    eml=input('enter email')
    if pswd=="admin@123" and eml=="admin@mail.com":
        print("login successful")
        break
    else:
        print('invalid credentials.retry')
    if i==3:
        print("blocked")
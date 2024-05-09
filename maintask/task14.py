# Write a program that takes input of 2 values and adds them. The program should only accept numbers and floats only or otherwise display an error “invalid character entered” and take the user to re-enter the inputs .
while True:
    num=float(input("enter number"))
    num2=float(input("enter number2"))
    if  float(num) and float(num2):
        total=num+num2
        print(total)
        break
    else:
        print("invalid character entered")
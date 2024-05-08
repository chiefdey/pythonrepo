# Write a program called stars. It should prompt the user for a number, and it should print the number of stars till the number entered.
num=int(input("enter number"))
for i in range(0,num+1):
    print("*"*i)

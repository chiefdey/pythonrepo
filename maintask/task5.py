# Implement a program that takes 3 form inputs or from the terminal, and stores them in three variables. Return the largest of the three
num1=input('num1: ')
num2=input('num2: ')
num3=input('num3: ')
if num1>num2 and num1>num3:
    print(f'num1 value: {num1} is largest')
if num2>num1 and num2>num3:
    print(f'num2 value: {num2} is largest')
if num3>num1 and num3>num2:
    print(f'num3 value: {num3} is largest')

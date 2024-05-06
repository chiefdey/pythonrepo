num1=int(input('enter number: '))
num2=int(input('enter 2nd number: '))
num3=int(input('enter 3rd number: '))
if num1>num2 and num1>num3:
    print(f'num1:{num1}is largest')
    # can change it to string so that value is displayed

elif num2>num1 and num2>num3:
    print(f'num2 with value: {num2} is largest')
elif num3>num1 and num3>num2:
    print(f'num3 with value: {num3} is largest')
else:
    print('all numbers are equal')


# Take as input from a user the temperature if the temperature is above 30°C display “The temperature is too high”, otherwise display “Normal temperature”
temp=int(input('enter temperature: '))

if temp>30:
    print(f'{temp} :degrees is too high')
else:
    print(f'{temp} :degrees normal temperature')
# Write a program which gets a phone number from a form input or terminal. Validates the phone number by checking if it starts with +254.. or 07.. or 7… or 254.. or 01... or  1.. Convert the number to start with +254… 
phn=input('enter tel.number: ')
if phn[0:5]=='+254' and len(phn)==13:
    print(phn)
elif phn[0:1]=='0':
    phn='+254'+ phn[1:]
    print(phn)
elif phn[0:3]=='01' and len(phn)==10:
    phn='+254'+phn[2:]
    print(phn)
else:
    print('invalid number')
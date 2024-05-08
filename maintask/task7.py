# Write that prompts the user to input student marks. The input should be between 0 and 100.Then output the correct grade: 
# A > 79 , B - 60 to 79, C -  59 to 49, D - 40 to 49, E - less 40
mrks=int(input('enter marks '))
if mrks>=0 and mrks<40:
            print(f'{mrks} :grade E')
elif mrks>=40 and mrks<50:
            print(f'{mrks} :grade D')
elif mrks>=50 and mrks<60:
            print(f'{mrks} :grade C')
elif mrks>=60 and mrks<80:
            print(f'{mrks} :grade B')
elif mrks>=80 and mrks<=100:
            print(f'{mrks} :grade A')
else:
            print("invalid marks")
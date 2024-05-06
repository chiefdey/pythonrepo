# <!-- Create a file called mydstask.py and attempt the below questions:
# my_ds = [23, “Jane”, (560), [“Lesson”, “Maths”, {“currency” : “KES”}], 987, (76,”John”)]
# 1. Print KES
# 2. Print 560
# 3. Print Maths
# 4. In the dictionary with the key currency, add another key “amount” with value 90
# 5. Reverse 987 to 789 without using an inbuilt -method or Assigning 789 manually.
#      Hint: Strings can be reversed using [::]
# 6. Change the name “John” to “Jane” .  -->

my_ds=[23, 'Jane', 560, ['Lesson', 'Maths', {'currency' : 'KES'}], 987, (76,"John")]
print(my_ds[3][2]['currency'])
print(my_ds[2])
print(my_ds[3][1])
my_ds[3][2]['amount']=90
print(my_ds)
# convert 987 to str for reversing then use [::-1] and then convert it back to int.
reve=str(my_ds[4])
reve=reve[::-1]
my_ds[4]=int(reve)
print(my_ds)
# convert it to list then edit and convert back to tuple.
new=list(my_ds[5])
new[1]="jane"
my_ds[5]=tuple(new)
print(my_ds)


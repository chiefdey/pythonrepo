lst=[]
for i in range(1,51):
 lst.append(i)
print(lst)
# 2
ls2=[]
for i in lst:
 if i%7==0 or i%5==0:
  ls2.append(i)
print(ls2)
# 3
l=list(range(10,41))
total=0
for i in l:
 total=total+i
 average=total/len(l)
print(total)
print(average)
# 4
odd=[]
num=range(10,51)
for i in num:
 if i%2!=0:
  odd.append(i)
  if len(odd)==10:
   break
print(odd)
# 5 write a program that takes a number as input and prints its multiplication table up to 10 using a for loop.
num1=int(input("enter number: "))
for i in range(1,11):
    x=i*num1
    print(f'{i}*{num1}={x}')
# 6 write a program that counts and prints the number of even numbers between 1 and 50 using a for loop
even=[]
for i in range(1,51):
    if i%2==0:
      even.append(i)
print(len(even))

# 7
ls2 = [('Jay', 20), ('Mo', 30), ('Mya', 32) ]
total=0
for i in ls2:
    total=total+i[1]
print(total)

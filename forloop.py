# ls1=list(range(200,300))
# print(ls1)
# for i in ls1:
#     print(i)
# display numbers divisible by 7 in a list

ls=list(range(200,300))
lst=[]
for i in ls:
    if i%7==0:
        lst.append(i)
# print(lst)

ls2 = [('Jay', 20), ('Mo', 30), ('Mya', 32) ]
# total=ls2[0][1]+ls2[1][1]+ls2[2][1]
# print(total)
total=0
for i in ls2:
    total=total+i[1]
print(total)

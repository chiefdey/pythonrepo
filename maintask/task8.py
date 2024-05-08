# Write a program that takes as input the speed of a car e.g 80. If the speed is less than 70, it should print “Ok”. Otherwise, for every 5 km/s above the speed limit (70), it should give the driver one demerit point and print the total number of demerit points.
# . If the driver gets more than 12 points, the function should print: “License suspended”.
spd=int(input("enter car speed"))
if spd<=70:
    print('okay')
elif spd>70:
    demerit=(spd-70)/5
    print(demerit,"demerits")
    if demerit>12:
        print("license suspended")

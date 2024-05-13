# #  function checking if number is even or odd.
# def check_num():
#     a=int(input("enter number"))
#     if a%2==0:
#         print(f"{a} is even")
#     else:
#         print(f"{a} is odd")
# check_num()
def cheknum(a):
    if a%2==0:
        print("even")
    else:
        print("odd")
a=int(input("enter number"))
cheknum(a)
# write a function to calculate triangle area
def t_area():
    a=int(input('enter height'))
    b=int(input('enter base'))
    c=a*b/2
    print(c,"is the area 0f triangle")
t_area()
def tr_area(x,y):
    area=x*y*0.5
    return area
height=int(input("t height"))
base=int(input("t base"))
t=tr_area(height,base)
# to display on terminal use print()
print(t)
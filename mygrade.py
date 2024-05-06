marks=int(input('enter marks:'))
if marks>=0 and marks<=100:
    if marks>=0 and marks<=25:
        print('e')
    elif marks>25 and marks<=40:
        print('d')
    elif marks>40 and marks<=55:
        print('c')
    elif marks>55 and marks<=65:
        print('b')
    else:
        print('A-')
else:
    print('invalid marks')

    # if marks>=50:
    #     print('pass')
    # else:
    #     print("fail")
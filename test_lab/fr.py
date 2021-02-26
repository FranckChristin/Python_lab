a, b, c = 0, 1, 0
while c<20:
    a = a+1
    a, b, c = a, a*7, c+1
    print(b, c)
    if b % 3 == 0:
        print('*')
    else:
        print(b)

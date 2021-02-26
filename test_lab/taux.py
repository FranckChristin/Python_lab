a, b, c = 1, 0, 0
a = 100*(4.3/100)
while c<20 :
    a, b, c = a, b+a, c+1
    print ('le montant obtenue est:',(c) ,  b)

# -*- coding : utf-8 -*-


import math
import pickle

"""
try :
    hours = int(input("enter your hour\n"))
    rate = float(input('your rate per hour\n'))

    print("your pay is: ", math.sqrt(hours*rate))

except:
    print('enter a valid number ')
"""
# ------------------------- functions ---------
"""
def min(values):
    smallest = None
    largest = None
    for value in values :
        if smallest is None or value < smallest:
            smallest = value
        if largest is None or value > largest :
            largest = value
    return smallest , largest
x = min([4,45,1,52])

print ('The smaller and largest value on a list is : \n', x)
"""
# ------------------------- files ---------
"""
text = open('info.txt')
count = text.read()
print('the number of string in this file is :', len(count))

 if we wanted to read a file and only print out lines which started with
the prefix “From:”, we could use the string method startswith to select only those lines with the desired prefix:

text = open('info.txt')
count = 0
for line in text:
    line = line.rstrip()    #enlever les espaces entre les sorti 'From'
    if line.find('umich.edu') == -1:   # find all the line where we have 'umich.edu'
        continue
    print(line) """
try :
    text = input('please enter your file name : \n')
    opentest = open(text)
    count = 0
    for line in opentest:
        line = line.rstrip()
        if line.startswith('From : '):
            count =+ 1
        print('the were', line, 'in text')

except FileNotFoundError:
    print('enter the filname that are exist in your sytem\n')

# create and write the file :

"""
file = input("open your file, if doesn't exist the system can create : \n\t")
test = open(file)
"""
line1 = "bonjour je m'appelle Franck Nguekam et voici mes infos personnel"
line2 = {
    "jour" : 30,
    "mois": 1,
    "année" : 1999,
    "lieux" : 'Douala',
}

with open ('donnees.txt', 'wb') as test:
    mon_pickler = pickle.Pickler(test)
    mon_pickler.dump(line2 ,)
test.close()
print('the file is : \n', test)
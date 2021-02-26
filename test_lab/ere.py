
def th():
    f=input('enter a numeric number : ')
    f=int(f)
    if f % 2 == 0:
        print ('pair')
    else :
        print ('impaire')
th()

def greet(lang):
    if lang == 'es':
        return 'Hola'
    elif lang == 'fr':
        return 'Bonjour'
    else:
        return 'Hello'

print(greet('fr'),'Michael')

def addtwo(a, b):
    added = a + b
    return a

x = addtwo(2, 7)
print(x)

n = 82
count = 0
for i in [2,54,42,87,56,89,92,56]:
    count = count + 1
    if i > n :
        n=i
        print ( n )
print(count, 'largest', n)

n = 0
while n > 0 :
    print('Lather')
    print('Rinse')
print('Dry off!')



fruit = 'orange'
index = 0
while index < len(fruit) :
    letter = fruit[index]
    index = index + 1
    print(letter, index)
    

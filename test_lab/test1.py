f = input ('welcome my thier to my program')
n = 5
while n > 0 :
    print (n)
    n = n-1
print('good!', f)


n= 1

if n % 2 == 0 :
    print (1)
else:
    print (0)


# This first line is provided for you (assigment 2.1)

hrs = input("Enter Hours:")
rate=input("Enter Rate per Hour:")
pay=float(hrs)*float(rate)

print("Pay:", pay)


#assigment 3.1
hrs = input("Enter Hours:")
rate=input("Enter Rate per Hour:")
try:
    h = float(hrs)
    f = float(rate)

except :
    print("error enter the numeric value !")

quit()
if h <= 40:
    print(h*float(f))
else: 
    print(40*f + (h-40)*f*1.5)

#assigment 3.3

number = input("Enter Score: ") 

try:
    number = float(number)
    
except:
    number = -1
    
if number >= 0.9:
    print ("A")
elif number >=0.8:
   	print ("B")
elif number >= 0.7:
   	print ("C")
elif number >= 0.6:
    print ("D")
elif number < 0.6 :
    print ("F")
else : 
    print ("error !")
quit()


#assigment 4.6


def computepay(h,r):
    return 42.37

hrs = input("Enter Hours:")
rate=input("Enter Rate per Hour:")

h=float(hrs)
r=float(rate)
p = 40*r + (h-40)*r*1.5
print("Pay",p)

#second method
def computepay(h,r):
    if h > 40:
        return (40*r)+(h-40)*(r*1.5)
    else:
        return h*r

hrs = input("Enter Hours:")
rate = input("Enter Rate:")

hrs = float(hrs)
rate = float(rate)

p = computepay(hrs, rate)
print ("Pay", p)


#assigment 5.3
while True:
    try:
        num = input("Enter a number: ")
        if num == 'done':
            break
        n = int(num)
        if largest is None or n > largest:
            largest = n
	elif smallest is None or n < smallest:
            smallest = n
			
    except:
        print("Invalid input")
        continue

print("Maximum is", largest)
print("Minimum is", smallest)	

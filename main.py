# -------------------------------------Day 1------------------------------------------------


# basic calcutalor program  


print("-------calculator-------")
print("\n")
num1 = int(input("enter first number ="))
num2 = int(input("enter second number="))
print("enter 1 for additon\nenter 2 for subtraction\nenter 3 for multiplication\nenter 4 for division")
entervalue =  int(input("enter value from 1 to 4="))
if entervalue == 1:
    print(num1 + num2)

elif entervalue == 2:
    print(num1 - num2)

elif entervalue == 3:
    print(num1 * num2)

elif entervalue == 4:
    print(num1 / num2)
else:
    print("invalid input")


#---------------------------Type casting in python ------------------------------------------------

# Typecasting is the conversion of one data type into another data type is called typecasting 

# Their are two type of typecasting in python 

# 1 = Explicit  = it is performed by the user 

a = "1"
b = "2"
print(a+b)
print(int(a)+int(b)) #this is the type conversion

## 2 = Implicit  = this is built in feature which is provide by the python to prevent data loss

a = "1.2"
b = "2"
print(a+b) # built in feature prventing the data loss

# -------------------------------------Day 2------------------------------------------------


# using for loop for reading the string character-by-characters

name = "jatin"
description = "this is the string read the data character by character"
for character in name : 
    print(character)

for letter in description :
    print(letter)

# we can find the length of a string using len() function 

fruit = "apple"
print(fruit[-4:-2])
ans = len(fruit)
print (ans)

# String slicing

print(fruit[0:4])
print(fruit[3:5])
print(fruit[:3])
print(fruit[:-3])
print(fruit[-3:3])


num = int(input("enter the value :"))
 
if(num > 100):
    print("yes")
elif(num < 100):
    print("no")
else:
    print("invalid input")    

if(num < 0):
    print(num ,"is negetive value")
elif(num > 0):
    if(num <= 10):
        print(num ,"lies between 1-10")
    elif(num > 10 and num <= 20):
        print(num ,"lies between 11-20")
    else:
        print(num ,"greater than 20")
else:
    print("invalid input")    


# this  is the way we can split an string 



fruit = "apple"
baskett = ["apple","mango","banana"]
words = []
print(fruit.split(" "))
print(list(fruit))

## splitint array of strings  

for string in baskett:
    words.extend(string.split())
print(words)


import time
tiemstap=time.strftime('%H:%M:%S')
print(tiemstap)
hours=int(time.strftime('%H'))
print(hours)
mint=int(time.strftime('%M'))
print(mint)
scnd=int(time.strftime('%S'))
print(scnd)
if(hours>=0 and hours<12):
    print("Good morning")
elif(hours>=12 and hours<=17):
    print("Good afternoon")
elif(hours>=18 and hours<=22):
    print("Good evening")
else:
    print("good night")




import time 
timestamp = time.strftime('%H:%M:%S')
hours = int(time.strftime("%H"))
minutes = int(time.strftime("%M"))
seconds = int(time.strftime("%S"))
print(timestamp,hours,minutes,seconds)

if(hours>=0 and hours<12):
    print("good morning ji")
elif(hours>= 12 and hours<=17):
    print("good afternoon ji")
elif(hours >=18 and hours <=17):
    print("good evening ji")
else:
    print("good night ji")

# using match statement 

x = int(input("enter the value : "))

match x:
    case 0:
        print("the value of x is ",x)
    case 10:
        print("the value is greater than 0 and less then 11")    
    case _ if x<90:
        print("the value is of x is less then 90" , x)    
    case _ if x>90:
        print("the value is of x is greater then 90" , x)    

for k in range (1,12,3):
    print(k)


for i in range(1,101):
    print(i)

# while loop 

i = int(input("enter the value :"))
while(i<100):
    print(i)
else:
    print("value is greater than 100")

# Break is used for breaking the loop and terminate the process 

for i in range(1,12):
    if(i==10):
        break
    print("5 X" , i , "=" , 5*i)
print("component breaked")

# continue is used for stop the iteration according to the condition and execute the remaining code 

for i in range(1,12):
    if(i==10):
        continue
    print("5 X" , i , "=" , 5*i)

# do while loop

i = 0
while True:
    print(i)
    i = i + 1
    if(i%100 == 0):
        break

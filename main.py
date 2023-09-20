## basic calcutalor program  


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


##---------------------------Type casting in python ------------------------------------------------

# # Typecasting is the conversion of one data type into another data type is called typecasting 

## Their are two type of typecasting in python 

## 1 = Explicit  = it is performed by the user 

a = "1"
b = "2"
print(a+b)
print(int(a)+int(b)) #this is the type conversion

# 2 = Implicit  = this is built in feature which is provide by the python to prevent data loss

a = "1.2"
b = "2"
print(a+b) # built in feature prventing the data loss


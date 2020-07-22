# Back Slash
print("Hello \
      Python")

#Triple Quotes
# Use of Triple Quotes is to produce the Text Art
print("""(")....(")
(' o ')
(")-(")
(""')-(""')""")
# 2nd use of Triple Quotes is to produce DocString
print("""This program is written in python""")
#3rd use of Triple Quotes is to prouce SQL statements
a = """select * from student"""
print(a)


#String Inside the Quotes
print("Python's World")


#Escape sequence of String
#\t is used as tab
#\n is used as new line
#\ is used as continuation point
#\a will give us the bell which os it has.....a ring of bell will be soundened..it will give alert sound in your computer if you run this command in shell
print("Hello\tWorld")
print("Hello\nWorld")
print('Python\'s World')
print("hello\aWorld")


#Formatted Output
#Here %s is string , %f is float , %d is integer and here in %f 10.2 ,10 is used for space and if we want exact value upto 2 decimal then we use .2
name = "Aarti"
marks = 98.899
age = 21
print("The name of person is %10s and the marks is %10.2f and age is %10d"%(name , marks , age))

#2nd method to write same string(this method can be used only in version greater than 3.4)
print(f"The name of person is {name} the marks is {marks} the age is {age}")

#3rd method to write same string
print("The name of person is" , name ,"marks is" , marks ,"age is" , age)


#VARIABLES
#Variables are linking of data to a name
#python  variable is case sensitive
#if we want to check the address of RAM we use id()
x = 20
id(x) # to check the address of RAM
#Deletion means not deleting but deletion means cutting the bindings

#OPERATORS
#Arithmetic Operators 1)** -> Power  2)/ -> Division  3)% -> Remainder after division(Modulus)  4)// -> Floor Division(return the lowest value )
a = 10 / 3
print(a)
b = 10 // 3
print(b)
c = 5 ** 5
print(c)

#Comparison Operator
a = 10
b = 20
c = 30
d = a == b
print(d)

#Assignment Operator
h = 10
g = 20
h = h + g # also write it as h+=g
print(h)

#Bitwise Operator 1)| -> OR operator  2)& -> AND operator  3)~ -> one's complement  4)^ -> XOR operator  5)<< -> Left Shift Operator  6)>> -> Right Shift Operator
a = 240
b = 1
print(bin(a))

#Logical Operator
#1)T or T = T
#2)T or F = T
#3)F or T = T
#4)F or F = F
# if AND operator finds the first value FALSE then python never goes to 2nd element , it will return FALSE only
#But if the AND operator finds the first value TRUE then python will check 2nd statement and later declare the result

#Membership Operator
#1) in -> weather the string is present in string or not
str1 = "pythonprogramming"
if "a" in str1:
    print(a)
#2) not in -> weather the string is present in string or not
if "a" not in str1:
    print(a)

#is operator checks weather they are pointing to same memory location or not
# both are pointing to same memory object or  not
x = 20
y = 10
if x is y:
    print(True)

#for integer case -5 to 256 , it has same memory
# if a = 257 it does not belong to same memory location


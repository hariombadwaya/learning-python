sher = "hariom badwaya"
print(sher)

# namimg convention 

SheryiansSchool = "students"    #pascal case 
sheryiansSchool = "students"    #camel case
sheriyans_school = "students"   #snake case

"""variables in python"""

a=12
print(a)

b = 12/4
print(b);
print(type(b))  # class float 

"""Strings in python"""

a="sher"
print(a[2])
print(a[-1])

# slicing  
b = "hey guys how you doing"
print(b[0:8:1]) # start, end , step size
print(b[0:10:2])

print(b[5::])  # it means complete string from 5 because we didn't mention end and step size overthere

"""type conversion"""

a=12
a=str(a)
print(type(a));
b=0
print(bool(b))
# False , 0 , 0.0 , "", [],(), {} always give us falsy values 

name = "hariom"
age= "23"
print(f"my name is {name} and  i am {age} ") # this is called formated string

# how to take input in python
#a= int(input("hello what is your age"))
#print(a); 

# operator in python
a=12
b=20
# print(a+b)
# print(a-b)
# print(a*b)
# print(b/a)
# print(b%a)
# print(b//a)  this is called floor division it means it exclude the digit after point unlike division which gives value in float
#print(a**b)  this is exponent used to give a power


# compound assignment operator in 
a=20
a= a+20
a= a+40
print(a)

# logical operator in python
print(12>10 and 30>20)


# money = int(input("please provide me money"))
# if money ==10:
#     print("i will have a choco bar")
# elif money == 20:
#     print("i will have a pohaa")    
# else:
#     print("i will have a ek rupee wali goli")

# a = int(input("enter NO1 "))
# b= int(input("enter NO2 "))
# if a>b:
#     print("A is greater")
# else:
#     print("B is greater")

# c= input("enter your gender ")
# if c=="male":
#     print("good morning sir")
# elif c=="female":
#     print("good morning mam")
# else:
#     print("you have no gender because i belive in male or female")

# d = int(input("enter the no. "))
# if d%2==0:
#     print("the number is even")
# else:
#     print("the number is odd")

# name = input("enter your name :")
# age = int(input("enter your age :"))
# if age>=18:
#     print(f"{name} you are eligible for vote")
# else:
#     print(f"{name} you are teenager pahle bade ho jao")

year = int(input("Enter the year: "))

if year % 4 == 0:
    print(f"{year} is a leap year")
elif year % 100 == 0:
    print(f"{year} is not a leap year")
elif year % 400 == 0:
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")
# a=input("enter the name:")
# ch=""
# # for i in a:
# #    ch=i+ch
# # print(ch)

# while a:
#     ch=a[0]+ch
#     a=a[1:]
# print(ch)

# a=input("enter name:")
# i=len(a)-1
# while i>=0:
#     print(a[i],end="")
#     i-=1

# Write a program to check whether a character entered is a vowel or a consonant.

# a=input("enter letter:b")
# if a=="a" and "e" and "i" and "o" and "u":
#     print("vowels")
# else:
#     print("consonant")

#Check whether a number is a 2-digit, 3-digit, or 4-digit number.

# a=int(input("enter num:"))
# if 10<=a<=99 or -10<=a<=-99:
#     print("2 digit num")
# elif 100<=a<=999 or -100<=a<=-999:
#     print("3 digit num")
# elif 1000<=a<=9999 or -1000<=a<=-9999:
#     print("4 digit num")

#Check whether a number lies between 10 and 50.

# a=int(input("enter a num:"))
# if 11<=a<=49:
#     print("num lies between 10 and 50 ")
# else:
#     print("not in between the number 10 and 5")
#Create a simple calculator using
# num1=float(input("enter num1:"))
# op=input("enter operator (+,-,*,/)")
# num2=float(input("enter the num2:"))
# if op=="+":
#     print("Result =", num1+num2)
# elif op=="-":
#     print("Result =",num1-num2)
# elif op=="*":
#     print("Result =", num1*num2)
# elif op=="/":
#     if num2!=0:
#         print("Result =",num1/num2)
#     else:
#         print("Error: Division by zero is not allowed")
# else:
#     print("invalid operator")

# n=input("enter num")
# if n==n[::-1]:
#     print("palindrome")
# else:
#     print("not paalindrom")

# letter = input("Enter a letter: ")

# text = input("Enter a letter or word: ")

# for y in range(15, -15, -1):
#     for x in range(-30, 30):
#         formula = ((x * 0.05) ** 2 + (y * 0.1) ** 2 - 1) ** 3 - (x * 0.05) ** 2 * (y * 0.1) ** 3

#         if formula <= 0:
#             print(text, end="")
#         else:
#             print(" ", end="")
#     print()

import random

words = ["apple", "tiger", "table", "chair", "beach"]

word = random.choice(words)
print(word)
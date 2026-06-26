# def greet():
#     print("welcome")
# greet ()

# import math
# # sqrt computes the square root
# square_root = math.sqrt(4)
# print("Square Root of 4 is", square_root)
# # pow() comptes the power
# power = pow(2, 3)
# print("2 to the power 3 is", power)

# amstrong number


# num = int(input("Enter a number: "))
# n = num
# digits = len(str(num))
# total = 0

# while n > 0:
#     digit = n % 10
#     total += digit ** digits
#     n //= 10

# if total == num:
#     print("Armstrong Number")
# else:
#     print("Not an Armstrong Number")

# def armstrong(num):
#     temp = num
#     digits = len(str(num))
#     total = 0

#     while temp > 0:
#         digit = temp % 10
#         total = total + digit ** digits
#         temp = temp // 10

#     if total == num:
#         return True
#     else:
#         return False


# # Main program
# n = int(input("Enter a number: "))

# if armstrong(n):
#     print(n, "is an Armstrong number")
# else:
#     print(n, "is not an Armstrong number")


# def is_amstrong(a):
#     n=str(a)
#     c=len(a)
#     total=0
#     for i in n:
#         total+=int(i)**c

# def show(a,b):
#     print(a,b)
# show(10,20) #positional

# show(b=20,a=10) #key word


# def greet(name="student"):
#     print("hello",name)
# greet()

# def show_number(*num):
#     print(num)
# show_number(1,2,3,4)
#     
# def display(**details):
#     print(details)
# display(name="Anu", age=24, city="Kochi")


# lamda

# sum=lambda a,b:a+b
# print(sum(5,4))

# a=int(input("enter a num:"))
# if a%2==0:
#     print("num is even")
# else:
#     print("num is odd")

# even= lambda a:a%2==0
# print(even(5))


# check=lambda x: "positove" if x>0 else "negative" if x<0 else "zero"
# check=lambda x: "positove" if x>0 else "negative"  x==0  "zero"
# print(check(3))
# print(check(-3))
# print(0)


# map_

# a=[1,2,3,4,5]
# square=list(map(lambda x:x**2,a))
# print(square)

# filter

# a=[1,2,3,4,5]
# even=list(filter(lambda x:x%2==0,a))
# print(even)
# odd=list(filter(lambda x:x%2==1, a))
# print(odd)

# a=[1,2,3,4,5,6,7,8,9,10]
# mul=list(filter(lambda x:x%3==0,a))
# print(mul)

# a=[1,2,3,4,5,6,7,8,9,10]

# from functools import reduce
# sum=reduce(lambda acc,y:acc+y,a)
# print("natural num",sum)
# b=list(filter(lambda x:x%2==0,a))
# even=reduce(lambda acc,y:acc+y,b)
# print("even",even)
# c=list(filter(lambda x:x%2==1, a))
# odd=reduce(lambda acc,y:acc+y,c)
# print("odd",odd)


func = [lambda arg=x: arg * 10 for x in range(1, 5)]
for i in func:
    print(i())


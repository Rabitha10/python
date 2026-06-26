# a=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23]
# print (a[1])
# print (a[-1])
# print (a[0:2])
# print (len(a))
# print(a.append(4))
# print(a.insert(1,10))
# print(a.extend([5,6]))
# print(a+[7,8])
# print(a.remove(2))
# print(a.pop())
# print(a.pop(1))
# # del a[0]
# # print (a.clear())
# print(a.index(11))
# # print(a.count())
# print(2 in a)
# print(a.sort())
# print(a.sort(reverse=True))
# print(a.reverse())
# print(sorted(a))
# print(a.copy())
# print (list("abc"))
# print(a*2)

# square=[x**2 for x in  range(10)]
# print(square)

# even=[x for x in range(10) if x%2==0]

# fruits = ["apple", "banana", "cherry"]
# upper_fruits = [fruit.upper() for fruit in fruits]
# print(upper_fruits)

# tags=["Even" if x % 2 ==0 else "Odd" for x in range(5)]
# print(tags)

# fruits = ["apple", "cherry","banana"]
# fruits.sort()
# print(fruits)

# fruits.sort(reverse=True)
# print(fruits)

# print(sorted(fruits))


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


num = int(input("Enter a number: "))
reverse = 0
while num > 0:
    digit = num % 10          # Get the last digit
    reverse = reverse * 10 + digit
    num = num // 10           # Remove the last digit
print("Reversed number:", reverse)



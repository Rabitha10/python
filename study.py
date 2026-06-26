# # n=int(input("enter a number:"))
# # # a=str(len(n))
# # for i in range(n):
# #     print(n)
# #     n=n-1
    

# class Solution(object):
#     def twoSum(self, nums, target):
#         seen = {}

#         for i, num in enumerate(nums):
#             difference = target - num

#             if difference in seen:
#                 return [seen[difference], i]

#             seen[num] = i
# nums = list(map(int, input("Enter numbers separated by space: ").split()))
# target = int(input("Enter target: "))

# s = Solution()
# result = s.twoSum(nums, target)

# print("Indices:", result)


# s = input("Enter a string: ")

# for i in (s):
#     print(i, ":", s.count(i))

# s = input("Enter a string: ")

# letters = digits = special = 0

# for i in s:
#     if i.isalpha():
#         letters += 1
#     elif i.isdigit():
#         digits += 1
#     else:
#         special += 1

# print("Letters:", letters)
# print("Digits:", digits)
# print("Special Characters:", special)

s = input("Enter sentence: ")
print(" ".join(s.split()[::-1]))

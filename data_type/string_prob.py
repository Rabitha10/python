# Count the number of vowels and consonants in a string.

# a=input("enter the word: ")
# v=0
# c=0
# if a.isalpha()==True:
#     for i in a:
#         if i in "aeiouAEIOU":
#             v+=1
#         else:
#             c+=1
#     print("cout of vowels:",v)
#     print("count of consonant:",c)
# else:
#     print("invalid")                

# Convert a string to uppercase and lowercase.

# name = input("Enter a name: ")

# if name.isupper():
#     print(name.lower())
# else:
#     print(name.upper())

#Reverse a string.

# name=input("enter name: ")
# a=""
# for i in name:
#     a=i+a
# print(a)

# name=input("enter name:")
# a=""
# while name:
#     a=name[0]+a
#     name=name[1:]
# print(a)    


# Check whether a string is a palindrome.

# a=input("enter name")
# if a==a[::-1]:
#     print("palindrom")
# else:
#     print("not palindrom")
    
# Remove all vowels from a string.

n=input("enter name: ")
a=" "
for i in n:
    if i not in "aeiouAEIOU":
        a+=i
    
print(a)
       

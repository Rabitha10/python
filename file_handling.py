# 1. Write a program to create a text file.
# file = open("sample.txt", "w")
# file.close()
# print("File created successfully")

# 2. Write a program to write your name and age into a file.

# file = open("details.txt", "w")

# name = input("Enter your name: ")
# age = input("Enter your age: ")
# file.write("Name: " + name + "\n")
# file.write("Age: " + age)
# file.close()
# print("Data written successfully")

# 3. Write a Python program to read data from a file.

# file = open("details.txt", "r")
# data = file.read()
# print(data)
# file.close()

# 4. Write a program to append new content into an existing file.

# file = open("details.txt", "a")
# file.write("\nAddress: Kerala")
# file.close()
# print("Content appended")

# 5. Write a program to count the number of characters in a file.

# file = open("details.txt", "r")
# data = file.read()
# print("Characters =", len(data))
# file.close()

# 6. Write a program to count the number of words in a file.

# file = open("details.txt", "r")
# data = file.read()
# words = data.split()
# print("Words =", len(words))
# file.close()

# 7. Write a program to count the number of lines in a file.

# file = open("details.txt", "r")
# lines = file.readlines()
# print("Lines =", len(lines))
# file.close()

# 8. Write a program to display only the first 5 lines of a file.

# file = open("details.txt", "r")
# for i in range(5):
#     line = file.readline()
#     print(line, end="")
# file.close()

# 9. Write a program to copy contents from one file to another.

# source = open("details.txt", "r")
# target = open("copy.txt", "w")
# data = source.read()
# target.write(data)
# source.close()
# target.close()
# print("File copied")

# 10. Write a program to merge two text files.

# file1 = open("details.txt", "r")
# file2 = open("sample.txt", "r")
# merged = open("merged.txt", "w")
# merged.write(file1.read())
# merged.write("\n")
# merged.write(file2.read())
# file1.close()
# file2.close()
# merged.close()
# print("Files merged")

# 11. Write a program to find the number of vowels in a file.

# file = open("details.txt", "r")
# data = file.read().lower()
# count = 0
# for ch in data:
#     if ch in "aeiou":
#         count += 1
# print("Vowels =", count)
# file.close()

# 12. Write a program to replace a specific word in a file.

# file = open("details.txt", "r")
# data = file.read()
# data = data.replace("Kerala", "India")
# file.close()
# file = open("details.txt", "w")
# file.write(data)
# file.close()
# print("Word replaced")

# 13. Write a program to remove all spaces from a file.

# file = open("details.txt", "r")
# data = file.read()
# data = data.replace(" ", "")
# file.close()
# file = open("sample.txt", "w")
# file.write(data)
# file.close()
# print("Spaces removed")

# 14. Write a program to convert all text into uppercase and store it in another file.

# file = open("details.txt", "r")
# data = file.read()
# file.close()
# newfile = open("upper.txt", "w")
# newfile.write(data.upper())
# newfile.close()
# print("Uppercase file created")

# 15. Write a program to find the longest word in a file.

# file = open("details.txt", "r")
# words = file.read().split()
# longest = max(words, key=len)
# print("Longest word =", longest)
# file.close()

# 16. Write a program to print only unique words from a file.

# file = open("details.txt", "r")
# words = file.read().split()
# unique_words = set(words)
# for word in unique_words:
#     print(word)
# file.close()

# 17. Write a program to remove duplicate lines from a file.

# file = open("details.txt", "r")
# lines = file.readlines()
# file.close()
# unique_lines = list(set(lines))
# file = open("unique.txt", "w")
# file.writelines(unique_lines)
# file.close()
# print("Duplicate lines removed")



# file=open("para.txt","r")
# data=file.read()
# count=0
# vowels= ""
# for ch in data:
#     if ch in "aeiou":
#         count+=1
#         vowels+=ch.upper()
#     else:
#         vowels+=ch    
      
# print("Vowels =",count)
# print(vowels)
# file.close()


vowels = "aeiouAEIOU"
vowel_count = 0

# Read the file
with open("para.txt", "r") as f:
    content = f.read()

# Count vowels
for char in content:
    if char in vowels:
        vowel_count += 1

# Change vowels to uppercase
new_content = ""
for char in content:
    if char in "aeiou":
        new_content += char.upper()
    else:
        new_content += char

# Write back to file
with open("para.txt", "w") as f:
    f.write(new_content)

print(f"Vowels found: {vowel_count}")
print("Vowels changed to uppercase")

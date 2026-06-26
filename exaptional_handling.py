# try:
#     x=10/0
# except:
#     print("error occur")
# else:
#     print("no error")

# 18. Write a program to handle division by zero.

# try:
#     a=int(input("enter numerator:"))
#     b=int(input("enter denominator:"))
#     result=a/b
#     print("result:",result)
# except:
#     print("error: division by zero not possible")


# 19. Write a program to handle invalid integer input.

# try:
#     a=int(input("enter a num:"))
#     print(a)
# except:
#     print("invali integer input")

# 20. Write a program to handle file not found exception.

# try:
#     file = open("file.txt", "r")
#     content = file.read()
#     print(content)
#     file.close()

# except:
#     print("Error: The file does not exist.")

# 21. Write a program to handle index out of range exception.

# try:
#     numbers = [10, 20, 30, 40, 50]

#     index = int(input("Enter index: "))
#     print("Element:", numbers[index])

# except IndexError:
#     print("Error: Index is out of range.")

# except ValueError:
#     print("Error: Please enter a valid integer index.")

# 22. Write a program to handle key errors in dictionary.
# try:
#     student = {
#         "name": "Arjun",
#         "age": 20,
#         "course": "Python"
#     }

#     key = input("Enter key to search: ")
#     print("Value:", student[key])

# except KeyError:
#     print("Error: Key not found in dictionary.")

# 23. Write a program to handle type errors.
# try:
#     age = "20"
#     print(age * "2")
# except TypeError:
#     print("Error: Invalid operation between data types.")

# 24. Write a program using multiple except blocks.

# try:
#     num1 = int(input("Enter first number: "))
#     num2 = int(input("Enter second number: "))

#     result = num1 / num2
#     print("Result =", result)

# except ZeroDivisionError:
#     print("Error: Cannot divide by zero.")

# except ValueError:
#     print("Error: Please enter valid integers.")

# except Exception as e:
#     print("Some other error occurred:", e)

# finally:
#     print("Program finished.")


# 25. Write a program using nested try blocks.

# try:
#     num1 = int(input("Enter first number: "))

#     try:
#         num2 = int(input("Enter second number: "))
#         result = num1 / num2
#         print("Result =", result)

#     except ZeroDivisionError:
#         print("Error: Cannot divide by zero.")

# except ValueError:
#     print("Error: Please enter valid integers.")

# finally:
#     print("Program finished.")

# 26. Write a program using finally for cleanup operations.

# try:
#     f = open("sample.txt", "r")
#     print(f.read())
# except FileNotFoundError:
#     print("File not found")
# finally:
#     print("Closing file / Cleanup done")

# 27. Write a program using else block.

# try:
#     num = int(input("Enter a number: "))
# except ValueError:
#     print("Invalid input")
# else:
#     print("You entered:", num)

# 28. Create a login system with exception handling.

# username = "admin"
# password = "1234"

# try:
#     u = input("Enter username: ")
#     p = input("Enter password: ")

#     if u == username and p == password:
#         print("Login Successful")
#     else:
#         raise ValueError("Invalid Username or Password")

# except ValueError as e:
#     print(e)

# 29. Create an ATM withdrawal system with validations.


# 30. Create a calculator with exception handling.
# 31. Write a program to validate age input.
# 32. Write a program to validate email format.
# 33. Write a program to retry user input until valid.
# 34. Write a program to safely open and read files.
# 35. Create a custom exception for insufficient balance.
# 36. Create a custom exception for invalid password.
# 37. Create a custom exception for voting age eligibility.
# 38. Create a custom exception for negative marks.
# 39. Create a custom exception for product out of stock.
# 40. Delete All Contents Inside a File
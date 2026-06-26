# # Creating a dictionary
# student = {
#     "name": "Alice",
#     "age": 21,
#     "course": "Computer Science"
# }

# # Accessing values
# print(student["name"])   # Output: Alice
# print(student["age"])    # Output: 21

# # Adding a new key-value pair
# student["grade"] = "A"

# # Updating a value
# student["age"] = 22

# # Removing an item
# del student["course"]


# # Looping through dictionary
# for key, value in student.items():
#     print(key, ":", value)

# 1.
# Find the total salary before tax.
# 2.
# Find the final salary after tax deduction.
# 3.
# Multiply the final salary by 12 to find yearly salary.
# 4.
# Divide yearly salary by 12 using floor division.

# salry={"basic_salary":35000, "bonus":5000, "tax":2000}
# total_salary=salry["basic_salary"]+salry["bonus"]
# print(dict([("the total salary before tax:",total_salary)]))
# final_salary=total_salary-salry["tax"]
# print(dict([("the final salary after tax deduction:",final_salary)]))
# yearly_salary=final_salary*12
# print(dict([("the final salary by 12 to find yearly salary:",yearly_salary)]))
# print(dict([("yearly salary by 12 using floor division:",yearly_salary//12)]))

# 1. Calculate the discounted price.
# 2. Add GST to the discounted price.
# 3. Find half of the final amount.
# 4. Find the remainder when the final amount is divided by 3.

# mobile={"mobile_price":45000,"discount":5000,"gst":2000}
# mobile["discounted_price"]=mobile["mobile_price"]-mobile["discount"]
# mobile["final_amount"]=mobile["discounted_price"]+mobile["gst"]
# mobile["half_amount"]=mobile["final_amount"]/2
# mobile["remainder"]=mobile["half_amount"]%3
# print(mobile)


# Tasks
# 1.
# Find total marks.
# 2.
# Find average marks.
# 3.
# Check whether Python marks are greater than SQL marks.
# 4.
# Check whether Power BI marks are equal to Python marks.

# python_marks = 85
# sql_marks = 78
# powerbi_marks = 90

# total_mark=(python_marks+sql_marks+powerbi_marks)
# print("totalmark:",total_mark)
# print("avarage:", total_mark//3)
# print("Python marks greater than SQL marks:", python_marks > sql_marks)
# print("Power BI marks equal to Python marks:", powerbi_marks == python_marks)

# 1.Find total product cost.
# 2.Add delivery charge.
# 3.Check whether total bill is greater than 5000.
# 4.Find square of quantity purchased.

# product_price = 1200
# quantity = 4
# delivery_charge = 150

# total_product_cost=(product_price)*quantity
# print(total_product_cost)
# total_bill=total_product_cost+delivery_charge
# print(total_bill)
# print("total bill is greater than 5000.", total_bill > 5000)
# print("Square of quantity:", quantity ** 2)

# 1.Find monthly data usage.
# 2.Multiply usage by 1024 to convert to MB.
# 3.Check whether usage is greater than 50 GB.
# 4.Use assignment operator to add 10 GB extra usage.

# daily_usage = 2.5
# days = 30
# monthly_usage = daily_usage * days
# print("monthly data usage:", monthly_usage)
# usage_mb = monthly_usage * 1024
# print("Monthly Usage MB:", usage_mb)
# print("Usage > 50 GB:", monthly_usage > 50)
# monthly_usage += 10
# print("Usage after adding 10 GB:", monthly_usage, "GB")

# 1.Add deposit to balance.
# 2.Subtract withdrawal amount.
# 3.Double the final balance.
# 4.Check whether balance is less than 100000.

# balance = 50000
# deposit = 12000
# withdraw = 7000
# deposit_balance= balance+deposit
# print("Balance after deposit:", deposit_balance)
# sub_witra_amnt= deposit_balance - withdraw
# print("Balance after withdrawal:", sub_witra_amnt)
# double_balance = balance * 2
# print("Double Balance:", double_balance)
# print("Balance < 100000:", balance < 100000)

# 1.Find EMI amount per month.
# 2.Find remainder when divided by 7.
# 3.Check whether EMI is greater than 5000.
# 4.Use assignment operator to increase EMI by 500.

# laptop_price = 80000
# months = 10

# emi = laptop_price / months
# print("EMI per month:", emi)
# remainder = emi % 7
# print("Remainder when EMI is divided by 7:", remainder)
# print("EMI > 5000:", emi > 5000)
# emi += 500
# print("EMI after increase:", emi)

# Tasks
# 1.Find total followers.
# 2.Find difference between Instagram and LinkedIn followers.
# 3.Check whether YouTube followers are not equal to LinkedIn followers.
# 4.Multiply total followers by 2.

# instagram = 25000
# youtube = 18000
# linkedin = 12000

# total_followers = instagram + youtube + linkedin
# print("Total Followers:", total_followers)
# difference = instagram - linkedin
# print("Difference:", difference)
# print("YouTube != LinkedIn:", youtube != linkedin)
# double_followers = total_followers * 2
# print("Double Total Followers:", double_followers)




# 1.
# Print the student name.
# 2.
# Print the course name.
# 3.
# Update marks to 95.
# 4.
# Add a new key "email".
# 5.
# Remove "city" from dictionary.
# 6.
# Print all dictionary values.

# student = {
# "name": "Rahul",
# "course": "Data Science",
# "marks": 88,
# "city": "Bangalore"
# }
# print(student["name"])
# print(student["course"])
# student.update({"marks":95})
# student["email"]="@123"
# student.pop("city")
# print(student)

# 1.
# Access employee salary.
# 2.
# Increase salary by 5000.
# 3.
# Add "location": "Kochi".
# 4.
# Remove department information.
# 5.
# Print all keys.

# employee = {
# "id": 101,
# "name": "Anjali",
# "department": "HR",
# "salary": 45000
# }

# print(employee["salary"])
# employee["salary"]=employee["salary"]+5000
# employee["location"]="kochi"
# employee.pop("department")
# print(employee)


# 1.Print mobile model.
# 2.Update price to 70000.
# 3.Add "color": "Black".
# 4.Remove storage information.
# 5.Print complete dictionary.

# mobile = {
#     "brand": "Samsung",
#     "model": "S24",
#     "price": 75000,
#     "storage": "256GB"
# }

# print("Model:", mobile["model"])
# mobile["price"] = 70000
# mobile["color"] = "Black"
# del mobile["storage"]
# print("Updated Dictionary:", mobile)
\
# 1.
# Print movie title.
# 2.
# Update rating to 9.1.
# 3.
# Add "director": "Lokesh".
# 4.
# Remove language.
# 5.
# Print all items.

movie = {
"title": "Leo",
"hero": "Vijay",
"rating": 8.5,
"language": "Tamil"
}

print("Movie Title:", movie["title"])
movie["rating"] = 9.1
movie["director"] = "Lokesh"
del movie["language"]
print("All Items:", movie)

# Tasks
# 1.
# Find total salary after bonus.
# 2.
# Add "department": "AI Team".
# 3.
# Increase salary by 5000.
# 4.
# Check whether total salary is greater than 60000.



# employee = {
# "name": "Akhil",
# "salary": 50000,
# "bonus": 10000
# }

# total_salary=employee["salary"]+employee["bonus"]
# print("total salary",total_salary)
# employee["departmrnt"]="AI teams"
# employee["salary"]+=5000
# print("Updated Salary:", employee["salary"])
# if total_salary>60000:
#     print("Total salary greater than 60000")
# elif total_salary==60000:
#     print("total salary equal 60000")
# else:
#     print("tatal salary less than 60000")
# print(employee)

# Tasks
# 1.
# Calculate total cart amount.
# 2.
# Add "delivery": 100.
# 3.
# Find final bill amount.
# 4.
# Check whether final bill is greater than 5000.


# cart = {
#     "item": "Keyboard",
#     "price": 1500,
#     "quantity": 3
# }


# total_amount = cart["price"] * cart["quantity"]
# print("Total Cart Amount:", total_amount)

# cart["delivery"] = 100
# print("Delivery Charge:", cart["delivery"])

# final_bill = total_amount + cart["delivery"]
# print("Final Bill Amount:", final_bill)

# if final_bill > 5000:
#     print("Final bill is greater than 5000")
# else:
#     print("Final bill is not greater than 5000")
# print(cart)

# Tasks
# 1.
# Find remaining fee amount.
# 2.
# Add "course": "Python Full Stack".
# 3.
# Update paid amount to 30000.
# 4.
# Check whether paid amount is equal to total fee.

# student = {
#     "name": "Diya",
#     "course_fee": 45000,
#     "paid": 20000
# }

# remaining_fee = student["course_fee"] - student["paid"]
# print("Remaining Fee:", remaining_fee)

# student["course"] = "Python Full Stack"

# student["paid"] = 30000
# print("Updated Paid Amount:", student["paid"])

# if student["paid"] == student["course_fee"]:
#     print("Paid amount is equal to total fee")
# else:
#     print("Paid amount is not equal to total fee")

# print(student)


# company_name = "TechNova Solutions"
# employee_name = "Arjun Menon"
# employee_id = "TNX2026"
# department = "Data Analytics"
# skills = ["Python", "SQL", "Excel", "Power BI", "Tableau"]
# monthly_salary = 45000
# bonus = 5000
# working_days = 26
# absent_days = 2
# project_details = (
# "Customer Churn Analysis",
# "Completed",
# "Power BI Dashboard"
# )
# email = "arjun.menon@technova.com"

# 1.
# # Print the company name in:uppercase, lowercase, title case
# print(company_name.upper())
# print(company_name.lower())
# print(company_name.title())

# # Find the total number of characters in employee name.
# print(len(employee_name))

# # Replace "Analytics" with "Science" in department.
# print(department.replace("Data Analytics","Data Science"))

# Extract: first name, last name, using slicing.

# print("first name:",employee_name[:5])
# print("last name:",employee_name[-5:])

# # Print first 5 characters from employee ID.
# print(employee_id[:5])

# # Check whether "Nova" exists in company name using membership operator.
# print("Nova" in company_name)

# # Create a professional message:
# # "Employee Arjun Menon works in Data Analytics department."
# # using concatenation.

# print("Employee "+employee_name+ " Works in " +department+ " department.")

# # Print email without domain name. Expected: arjun.menon

# print(email.split("@")[0])


# list
# Print: first skill, last skill

# print("first skill:",skills[0])
# print("last skill:",skills[-1])

# # Add "Machine Learning" to skills list.

# skills.append("Machine Learning")
# print(skills)

# Insert "Statistics" at 2nd posrition.

# skills.insert(2,"Statistics")
# print(skills)

# # 12. Remove "Excel" from list.

# skills.remove("Excel")
# print(skills)

# # Sort skills alphabetically.
# skills.sort()
# print(skills)

# # Reverse the skills list.

# skills.reverse()
# print(skills)

# # 15. Find total number of skills.

# print(len(skills))

# # 16. Create another list:
# # tools = ["Git", "Jupyter Notebook"]
# # Merge it with skills list.

# tools = ["Git", "Jupyter Notebook"]
# skills.extend(tools)
# print(skills)


# # Check whether "SQL" exists in skills list.

# print("SQL" in skills)

# # Print skills from index 1 to 4 using slicing.
# print(skills[0:4])

# # tuple

# # Print all project details.
# print(project_details)

# # Print project status only.
# print(project_details[1])

# # Find total number of elements in project_details tuple.
# print(len(project_details))

# # Check whether "Completed" exists in tuple.
# print("Completed" in project_details)

# # Create another tuple:
# # project_manager = ("Rahul",)
# # Combine both tuples.

# project_manager = ("Rahul",)
# print(project_details + project_manager)

# #operator
# # 24.Calculate:
# # total_salary = monthly_salary + bonus
# total_salary = monthly_salary + bonus
# print(total_salary)

# # Calculate salary per working day.

# print(total_salary//working_days)

# # Calculate salary deduction for absent days.
# # Formula:
# # (monthly_salary / working_days) * absent_days

# print((monthly_salary//working_days)*absent_days)

# # Use assignment operator: Increase salary by 3000.

# print(monthly_salary+3000)

# # Check: monthly_salary > bonus

# print(monthly_salary > bonus)

# # Check identity operator:
# # skills is tools

# print(skills is tools)

# # Check logical operator:
# # monthly_salary > 40000 and bonus > 3000

# print(monthly_salary > 40000 and bonus > 3000)

# summary = (
#     "Employee Summary\n"
#     "-----------------\n"
#     "Company: " + company_name + "\n"
#     "Employee Name: " + employee_name + "\n"
#     "Department: {}\n"
#     "Skills: {}\n"
#     "Project: {}\n"
#     "Total Salary: ₹{}\n"
# ).format(department, skills, project_details, total_salary)

# print(summary)
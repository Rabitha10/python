# s={1,2,3}
# print(type(s))

# s=frozenset([1,2,3,4])
# print(s)

# s={1,2,3,4}
# s=set()
# print(s)
# s={1,2,2,3}
# print(s)
# print(len(s))
# s.add(4)
# print(s)

# s.update([4,10])
# print(s)

# s.remove(2)
# s.discard(2)
# s.pop()
# s.clear()
# print(s)

# A={1,2,3,4,5}
# B={4,5,6,7,8}
# print(A.union(B))
# print(A|B)
# print(A&B)
# print(A-B)
# print(A^B)
# print(A.intersection(B))
# print(A.difference(B))
# print(A.symmetric_difference(B))

# x={"Rabi","anu"}
# y={1.2,390,6,20}
# A.update(x,y)
# print(A)

# B.intersection_update({"hi",6,7,20,21,22})
# print(B)

# A.difference_update({1,2,45,"rani"})
# print(A)

# B.symmetric_difference_update({7,8,6,"doi"})
# print(B)

# print(A.issubset(B))
# print(A.issuperset(B))

# s={1,2,3,4}
# # b=s.copy()
# # print(b)
# print(sorted(s))
# print(max(s))
# print(min(s))
# print(sum(s))

# 1. Find students enrolled in both courses.
# 2. Find students enrolled only in Python.
# 3. Find students enrolled only in Data Analytics.
# 4. Find all unique students.
# 5. Find students enrolled in exactly one course.


# python_students = {"Arun", "Megha", "Rahul", "Sneha"}
# analytics_students = {"Sneha", "Rahul", "Aman", "Diya"}

# print("students enrolled in both courses:",python_students.union(analytics_students))
# print("students enrolled only in Python:",python_students-analytics_students)
# print("students enrolled only in Data Analytics:",analytics_students-python_students)
# print("all unique students:", python_students&analytics_students)
# print("students enrolled in exactly one course:",python_students^analytics_students)


# Tasks
# 1. Find common brands purchased by both customers.
# 2. Find all brands purchased.
# 3. Find brands purchased only by customer1.
# 4. Find brands purchased by only one customer.


# customer1 = {"Samsung", "Apple", "OnePlus", "Realme"}
# customer2 = {"Apple", "Vivo", "Oppo", "Samsung"}

# print("common brands purchased by both customers:",customer1&customer2)
# print("all brands purchased:",customer1|customer2)
# print("brands purchased only by customer1:",customer1-customer2)
# print("Find brands purchased by only one customer:",customer1^customer2)


# #1. Find tools used by both teams.
# 2.Find tools exclusive to the design team.
# 3.Find all software tools used in the company.
# 4.Find tools used by only one team.


# design_team = {"Figma", "Photoshop", "Canva", "Illustrator"}
# marketing_team = {"Canva", "Excel", "Photoshop", "PowerBI"}

# print("Tools used by both teams:",design_team&marketing_team)
# print("tools exclusive to the design team:",design_team-marketing_team)
# print("all software tools used in the company:",design_team|marketing_team)
# print("tools used by only one team.:",design_team^marketing_team)

# Tasks
# 1.Find students who like both sports.
# 2.Find students who like only cricket.
# 3.Find students who like only football.
# 4.Find all sports fans.

# cricket_fans = {"Ajay", "Kiran", "Rohit", "Nisha"}
# football_fans = {"Nisha", "Rahul", "Ajay", "David"}

# print("students who like both sports:",cricket_fans&football_fans)
# print("students who like only cricket:",cricket_fans-football_fans)
# print("students who like only football:", football_fans-cricket_fans)
# print("all sports fans:",cricket_fans|football_fans)


# Tasks
# 1.Find common purchased products.
# 2.Find products only in electronics.
# 3.Find all purchased items.
# 4.Find products available in only one category.

# electronics = {"Laptop", "Headphones", "Mouse", "Keyboard"}
# accessories = {"Keyboard", "Mouse Pad", "Laptop Stand", "Headphones"}

# print("common purchased products:",electronics&accessories)
# print("products only in electronics:",electronics-accessories)
# print("all purchased items:",electronics|accessories)
# print("products available in only one category:",electronics^accessories)

# Tasks
# 1.Find common programming languages.
# 2.Find languages known only by employee1.
# 3.Find all unique languages.
# 4.Find languages known by only one employee.

# employee1 = {"Python", "Java", "SQL", "C"}
# employee2 = {"Python", "JavaScript", "SQL", "Go"}

# print("common programming languages:",employee1&employee2)
# print("languages known only by employee1:",employee1-employee2)
# print("all unique languages:",employee1|employee2)
# print("Find languages known by only one employee:", employee1^employee2)


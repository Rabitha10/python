# class Student:
#     def greet(self):
#         print("Hello Student")
# s = Student()
# s.greet()

# class car:
#     def colour(self):
#         print("blue")
# c=car()
# c.colour()

# class operator:
#     def arithamatic_operator(self):
#         print("a+b")
#     def substraction(self):
#         print("a-b")
#     def division(self):
#         print("a/b")
# c=operator()
# c.arithamatic_operator()
# c.substraction()
# c.division()


# class Student:
#     a="biriyani"
#     def food(self):
#         print(self.a)
        
# x=Student()
# x.food()


# class Student:
#     def __init__(self,a,b):
#        self.x=a
#        self.y=b
#     def arithmetic(self):
#         print(self.x+self.y)

# x=Student(5,10)
# x.arithmetic()

# class Student:
#     def __init__(self, name, age, course):
#         self.x = name
#         self.y = age
#         self.z = course

#     def details(self):
#         print("Name:", self.x)
#         print("Age:", self.y)
#         print("Course:", self.z)

#         print()
# s1 = Student("Rabitha", 25, "Data Science")
# s2 = Student("Anu", 22, "Python")
# s3 = Student("Rahul", 24, "Machine Learning")

# s1.details()
# s2.details()
# s3.details()

        
# class Mobile:
#     def __init__(self, brand, model, price):
#         self.x = brand
#         self.y = model
#         self.z = price

#     def details(self):
#         print("Brand:", self.x)
#         print("Model:", self.y)
#         print("Price:", self.z)

#         print()
# m1 = Mobile("Sumsung", "M31s", 120000)
# m2 = Mobile("Apple", "16promax", 1300000)


# m1.details()
# m2.details()


# class Employee:
#     def __init__(self, emp_id, name, salary):
#         self.emp_id = emp_id
#         self.name = name
#         self.salary = salary

#     def display(self):
#         print(self.emp_id, self.name, self.salary)

# employees = [
#     Employee(101, "Rabitha", 50000),
#     Employee(102, "Anu", 45000),
#     Employee(103, "Rahul", 55000),
#     Employee(104, "Akhil", 48000),
#     Employee(105, "Meera", 60000)
# ]

# for emp in employees:
#     emp.display()

# class Book:
#     def __init__(self, title, author, price):
#         self.title = title
#         self.author = author
#         self.price = price

#     def display(self):
#         print("Title :", self.title)
#         print("Author:", self.author)
#         print("Price :", self.price)
#         print()

# b1=(Book("A Tale of Two Cities","Charles Dickens",340))
# b2=(Book("Alice in Wonderland","Lewis Carroll",2999))
# b3=(Book("Animal Farm","George Orwell",4500))
# b4=(Book("Crime and Punishment","Fyodor Dostoevsky",4664))

# b1.display()
# b2.display()
# b3.display()
# b4.display()

# class BankAccount:
#     def __init__(self, account_holder_name , account_number , balance):
#         self.a = account_holder_name
#         self.b = account_number
#         self.c = balance

#     def display(self):
#         print("account holder name :", self.a)
#         print("account number:", self.b)
#         print("balance :", self.c)
#         print()

# a1=(BankAccount("rabitha",12334555,340))
# a2=(BankAccount("Alice",887777777,2999))


# a1.display()
# a2.display()

# class car:
#     def __init__(self, brand , model , price):
#         self.a = brand
#         self.b = model
#         self.c = price

#     def display(self):
#         print("Brand :", self.a)
#         print("Model:", self.b)
#         print("Price :", self.c)
#         print()

# a1=(car("toyota","K10",3400000))
# a2=(car("BMW","X11",29999999))


# a1.display()
# a2.display()

# class movieticket:
#     def __init__(self,movie_name,seat_number,ticket_price):
#         self.a=movie_name
#         self.b=seat_number
#         self.c=ticket_price
#     def display(self):
#         print("Movie name :", self.a)
#         print("Seat number: ",self.b)
#         print("ticket price:",self.c)
#         print()

# a1=(movieticket("balan","e32",160))
# a2=(movieticket("atiradi","a20",180))

# a1.display()
# a2.display()


# class Patient:
#     def __init__(self,patient_name,age,disease):
#         self.a=patient_name
#         self.b=age
#         self.c=disease

#     def display(self):
#         print("patient name:",self.a)
#         print("age:",self.b)
#         print("disease:",self.c)
#         print()
        
# a1=(Patient("rabitha",25,"fever"))
# a2=(Patient("anu",26,"cough"))

# a1.display()
# a2.display()



# class Calculator:
#     def __init__(self,n1,n2):
#         self.a=n1
#         self.b=n2
#     def display(self):
#         print("addition:",self.a + self.b)
#         print("substraction:", self.a-self.b)
#         print("multiplication:", self.a*self.b)
#         if self.b!=0:
#             print("divion:",self.a//self.b)
#         else:
#             print("division by zero not allowed")
        
# z=Calculator(8,2)
# z.display()




# class ATM:
#     def __init__(self,deposit,withdraw,check_balance):
#         self.a=deposit
#         self.b=withdraw
#         self.c=check_balance

#     def display(self):
#         self.c += self.a
#         self.c -= self.b
#         print("Balance:", self.c)

# atm = ATM(500, 300, 1000)
# atm.display()


# class ATM:
#     def __init__(self,balance):
#         self.balance=balance
#     def deposit(self,amount):
#         self.balance+=amount
#         print("deposit amount:",amount)
#     def widraw(self,amount):
#         if amount<=self.balance:
#             self.balance-=amount
#             print("widraw:",amount)
#         else:
#             print("insufficient amount")
#     def display(self):
#         print("current balance:",self.balance)

# a=ATM(1000)
# a.deposit(500)
# a.widraw(200)
# a.display()


# class shoppingcart:
#     def __init__(self):
#         self.cart=[]
#     def add_product(self,product):
#         self.cart.append(product)
#         print(product,"added to the cart")
        

#     def remove_product(self,product):
#         if product in self.cart:
#             self.cart.remove(product)
#             print(product,"removed from the cart")
#         else:
#             print("product not in the cart")
            

#     def show_cart(self):
#         print("product in cart")
#         for item in self.cart:
#             print(item)
            

# c=shoppingcart()

# c.add_product("book")
# c.add_product("pen")
# c.add_product("box")
# c.add_product("bag")

# c.show_cart()

# c.remove_product("pen")
# c.remove_product("pencil")

# c.show_cart()

# class vehicle:
#     def __init__(self,name):
#         self.name=name

# class car(vehicle):
#     def display(self):
#         print("thos is a car:",self.name)
# class bike(vehicle):
#     def display(self):
#         print("this is a bike:",self.name)
# class truck(vehicle):
#     def display(self):
#         print("this is truck",self.name)

# c=car("BMW")
# b=bike("Himalaya")
# t=truck("Volvo")

# c.display()
# b.display()
# t.display()


# class employee:
#     def __init__(self,designation,salary):
#         self.designation=designation
#         self.salary=salary

# class manager(employee):
#     def display(self):
#         print("designation:",self.designation)
#         print("salary:",self.salary)
# class developer(employee):
#     def display (self):
#         print("designation:",self.designation)
#         print("salary:",self.salary)

# class tester(employee):
#     def display (self):
#         print("designation:",self.designation)
#         print("salary:",self.salary)

# m=manager("manager",550000)
# d=developer("developer",646479)
# t=tester("tester",378838)
# m.display()
# print()
# d.display()
# print()
# t.display()

# class person:
#     def __init__(self,name):
#         self.name=name
# class teacher(person):
#     def __init__(self, name,subject):
#         super().__init__(name)
#         self.subject=subject

#     def display(self):
#         print("name:",self.name)
#         print("role: teacher")
#         print("subject:",self.subject)

# class student(person):
#     def __init__(self, name,course):
#         super().__init__(name)
#         self.course=course
#     def display(self):
#         print("name:",self.name)
#         print("role: student")
#         print("course:",self.course)

# t=(teacher("rabi","maths"))
# s=(student("anu","data science"))

# t.display()
# print()
# s.display()


# Person
# ↓
# Student
# ↓
# GraduateStudent

# class person:
#     def __init__(self,name):
#         self.name=name
# class student(person):
#     def __init__(self, name,course,):
#         super().__init__(self,name)
#         self.course=course


# class parent:
#     def __init__(self,name):
#         self.name=name
# class child(parent):
#     def __init__(self, name,age):
#         super().__init__(name)
#         self.age=age
#     def display(self):
#         print("name:",self.name)
#         print("age:",self.age)


# user=(child("alice","25"))
# user.display()


# class person:
#     def __init__(self,name):
#         self.name=name
# class student(person):
#     def __init__(self, name,course,):
#         super().__init__(name)
#         self.course=course
#     def display(self):
#         print("name:",self.name)
#         print("course:",self.course)

# class Demo:
#     def __init__(self):
#         self.__x = 10
#     def show(self):
#         print(self.__x)
# d = Demo()
# d.show()

# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.__marks = marks   # Private variable

#     def display(self):
#         print("Name:", self.name)
#         print("Marks:", self.__marks)

#     def set_marks(self, marks):
#         self.__marks = marks

#     def get_marks(self):
#         return self.__marks


# s = Student("Rahul", 85)
# s.display()
# s.set_marks(90)
# print("Updated Marks:", s.get_marks())

# class Demo:
#     def __init__(self):
#         self.public = 10
#         self._protected = 20
#         self.__private = 30
#     def show(self):
#         print(self.public, self._protected, self.__private)
# obj = Demo()
# obj.show()
# print(obj.public)
# # public accessible
# print(obj._protected)
# #protected (accessible but not recommended)
# # print(obj.__private)
# # error (private)


# from abc import ABC, abstractmethod
# class Vehicle (ABC):
#     @abstractmethod
#     def start(self):
#         pass

# class Car(Vehicle):
#     def start(self):
#         print("Car is starting...")
# c = Car()
# c.start()

# class Animal:
#     def speak(self):
#         return"some generic sound"
# class Dog(Animal):
#     def speak(self):
#         return"Woof!"
# class Cat(Animal):
#     def speak(self):return "Meow!"
# animals=[Dog(),Cat(),Animal()]
# for i in animals:
#     print(i.speak())


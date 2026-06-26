# Student Grade Calculator & Report Card (Short Explanation)

# This project is a command-line application (CLI) used to manage student marks and generate report cards.

# What it does:
# Add student names and test scores.
# Calculate each student's average score.
# Assign a letter grade:
# A → 90 and above
# B → 80–89
# C → 70–79
# D → 60–69
# F → Below 60
# View all student records.
# Generate a class report showing:
# Highest average
# Lowest average
# Class average
# Continue running until the user chooses Exit.
# Python Concepts Used:
# Data Types
# str → Student name
# int/float → Scores
# list → Store scores
# dict → Store student details
# Functions
# add_student()
# calculate_average()
# get_letter_grade()
# show_class_report()
# Loops
# while → Menu keeps running
# for → Process scores and students
# Conditions
# if/elif/else → Assign grades and validate input

# Student Grade Calculator & Report Card

students = []


# Function to calculate average score
def calculate_average(scores):
    if len(scores) == 0:
        return 0
    return sum(scores) / len(scores)


# Function to determine letter grade
def get_letter_grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 80:
        return "B"
    elif avg >= 70:
        return "C"
    elif avg >= 60:
        return "D"
    else:
        return "F"


# Function to add a student
def add_student():
    name = input("Student name: ")
    scores = []

    while True:
        score = input("Enter score, or 'done': ")

        if score.lower() == "done":
            break

        try:
            score = float(score)

            if 0 <= score <= 100:
                scores.append(score)
            else:
                print("Score must be between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a number or 'done'.")

    average = calculate_average(scores)
    grade = get_letter_grade(average)

    student = {
        "name": name,
        "scores": scores,
        "average": average,
        "grade": grade
    }

    students.append(student)

    print(f"\nAdded {name} - Average: {average:.2f} - Grade: {grade}\n")


# Function to display all students
def view_all_students():
    if len(students) == 0:
        print("\nNo students added yet.\n")
        return

    print("\n--- Student List ---")
    for student in students:
        print(f"Name    : {student['name']}")
        print(f"Scores  : {student['scores']}")
        print(f"Average : {student['average']:.2f}")
        print(f"Grade   : {student['grade']}")
        print("-" * 25)
    print()


# Function to show class report
def show_class_report():
    if len(students) == 0:
        print("\nNo student data available.\n")
        return

    highest = students[0]
    lowest = students[0]
    total_average = 0

    for student in students:
        total_average += student["average"]

        if student["average"] > highest["average"]:
            highest = student

        if student["average"] < lowest["average"]:
            lowest = student

    class_average = total_average / len(students)

    print("\n--- Class Report ---")
    print("Total Students :", len(students))
    print(f"Highest Average: {highest['name']} with {highest['average']:.2f}")
    print(f"Lowest Average : {lowest['name']} with {lowest['average']:.2f}")
    print(f"Class Average  : {class_average:.2f}\n")


# Main menu function
def main():
    while True:
        print("===== Grade Calculator =====")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Class Report")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_all_students()
        elif choice == "3":
            show_class_report()
        elif choice == "4":
            print("Thank you for using the Grade Calculator!")
            break
        else:
            print("Invalid choice. Please try again.\n")


# Start the program
main()
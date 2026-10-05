students = []


def calculate_grade(percentage):
    if percentage >= 90:
        return "A"
    elif percentage >= 75:
        return "B"
    elif percentage >= 50:
        return "C"
    else:
        return "Fail"


number_of_students = int(input("Enter number of students: "))

for i in range(number_of_students):

    print(f"\nEnter information for Student {i + 1}")

    name = input("Enter student name: ")

    marks1 = float(input("Enter marks for Information Security: "))
    marks2 = float(input("Enter marks for Database Management: "))
    marks3 = float(input("Enter marks for English: "))
    marks4 = float(input("Enter marks for Algorithm Analysis: "))
    marks5 = float(input("Enter marks for Data Structure: "))

    total = marks1 + marks2 + marks3 + marks4 + marks5

    percentage = total / 5

    grade = calculate_grade(percentage)

    student = {
        "name": name,
        "total": total,
        "percentage": percentage,
        "grade": grade
    }

    students.append(student)


print("\nStudent Results")

for student in students:

    print("Name:", student["name"])
    print("Total Marks:", student["total"])
    print("Percentage:", student["percentage"], "%")
    print("Grade:", student["grade"])
 
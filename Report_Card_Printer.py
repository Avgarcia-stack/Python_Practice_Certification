"""Simple Report Card Printer"""
print("Welcome to the Report Card Printer".center(45))
# Student Information
name = 'Avgarcia'
student_id = 'STU-001'
grade_level = '10th Grade'

# Display student info with type checking
print("\n" + "="*45)
print("STUDENT INFORMATION".center(45))
print("="*45)
print(f"Name: {name}")
print(f"  Type: {type(name).__name__}, isinstance(str): {isinstance(name, str)}")
print(f"ID:{student_id}")
print(f"Type:{type(student_id).__name__}, isinstance(str): {isinstance(student_id,str)}")
print(f"Grade: {grade_level}")
print(f"  Type: {type(grade_level).__name__}, isinstance(str): {isinstance(grade_level, str)}")

# Grades (Subject: Score)
grades = {
    'Mathematics': 85.5,
    'English': 92,
    'Science': 88.5,
    'History': 79,
    'Physics': 91,
    'Chemistry':100, 
    'Programming':85,
    'Portuguese': 75,
}
print("\n" + "="*45)
print("GRADES".center(45))
print("Report CARD".center(45))
print("="*45)
print(f"Name:{name} | ID:{student_id} ")

print(f"Grade Level: {grade_level}")
print("-"*45)
print(f"{'Subject':<20} {'Score':<10}")
print("-"*45)

for subject, score in grades.items():
    print(f"{subject:<20} {score}")

# Calculate average
average = sum(grades.values()) / len(grades)

print("-"*45)
print(f"{'AVERAGE:':<20} {average:.2f}")
print(f"  Type: {type(average).__name__}, isinstance(float): {isinstance(average, float)}")
print("="*45)
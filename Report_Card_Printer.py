"""This code demonstrates the use of different data types in Python, including strings, integers, floats, and booleans.
 It also shows how to check the type of a variable using the `type()` function and how
 to check if a variable is an instance of a specific type using the `isinstance()` function."""

name = 'Alice'
print(name, type(name))

#is_student = True
#print(is_student, type(is_student))

age = 20
print(age, type(age))

score = 80.5
print(isinstance(score, float))
print(isinstance(score, int))
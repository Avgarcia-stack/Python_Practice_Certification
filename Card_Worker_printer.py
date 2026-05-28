import datetime
"""Worker Card Printer"""
print("Welcome to the Worker Card Printer".center(45))
"""Skills"""
first_skill = str(input("Enter your first skill: "))
second_skill = str(input("Enter your second skill: "))
experience_1 = str(input("Enter your first work experience: "))
experience_2 = str(input("Enter your second work experience: "))
years_of_experience1 = int(input("Enter your years of experience on your firts work: "))
years_of_experience2 = int(input("Enter your years of experience on your second work: "))

"""Worker Information"""
name = 'Avgarcia'
worker_id = 'WRK-001'
department = 'Engineering'

print("\n" + "="*45)
print("WORKER INFORMATION".center(45))
print("="*45)
print(f"Name: {name}")
print(f"ID: {worker_id}")
print(f"Department: {department}")
print("="*45)
print("Worker Skills".center(45))
print("="*45)
print(f"Skill 1: {first_skill}")
print(f"Skill 2: {second_skill}")
print("="*45)
"""Experience Works"""
print("="*45)
print("Experience Works".center(45))
print("="*45)
print(f"Experience 1: {experience_1}")
print(f"Experience 2: {experience_2}")
"""Calculate years of experience"""
print("="*45)
print("Calculate years of experience".center(45))
print("="*45)
print(f"Years of Experience: {years_of_experience1}")
print(f"Years of Experience: {years_of_experience2}")
total_experience = years_of_experience1 + years_of_experience2
print(f"Total Years of Experience: {total_experience}")
online_worker = (f"is this worker is online right now? {True}")
print(online_worker)
is_online_worker = True
if is_online_worker:
    print("worker is online")
else : print("worker is offline")
timestamp = datetime.datetime.now().strftime("%H:%M:%S")
print(f"Worker Online Status: {is_online_worker} (Checked at {timestamp})")
from datetime import datetime, timedelta

print("-" * 50)
print("         Student Attendance System      ")
print("-" * 50)


current = datetime.now()

print("Today's Date :", current.strftime("%d/%m/%Y"))
print("Current Time :", current.strftime("%I:%M:%S %p"))
print()

student_name = input("Enter Student Name: ")
study_duration = int(input("Enter Study Duration (minutes) : "))


login_time = current
logout_time = login_time + timedelta(minutes=study_duration)
duration = logout_time - login_time
print()
print("-" * 50)
print("Attendance Summary")
print("-" * 50)
print()
print("Student Name  :", student_name)
print("Login Time    :", login_time.strftime("%I:%M:%S %p"))
print("Logout Time   :", logout_time.strftime("%I:%M:%S %p"))


total_seconds = int(duration.total_seconds())
hours = total_seconds // 3600
minutes = (total_seconds % 3600) // 60
seconds = total_seconds % 60

print(f"Study Duration: {hours:02}:{minutes:02}:{seconds:02}")
print()
print("Thank You!")
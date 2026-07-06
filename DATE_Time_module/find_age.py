from datetime import datetime
birthday = datetime(1992,4,25)
today =datetime.now()
print(f'person age:{today.year-birthday.year} years')
from datetime import datetime, timedelta
today = datetime.now()
print(f'today: {today}')
print(f'Date before 100 days :{today-timedelta(days=100)}')


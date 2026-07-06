from datetime import datetime, timedelta
today = datetime.now()
print(f'today: {today}')
print(f'replace year :{today-timedelta(days=100)}')


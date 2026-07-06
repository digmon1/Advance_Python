from datetime import datetime
today= datetime.now()
date_format1=today.strftime(f'%d/%B/%Y (%A)')
time_format=today.strftime(f'%I:%M:%S %p')
print(today)
print(date_format1)
print(time_format)
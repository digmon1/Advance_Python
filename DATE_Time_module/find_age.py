from datetime import datetime
from dateutil.relativedelta import relativedelta
birthday = datetime(1992,4,25)
today =datetime.now()
print(f'person age:{today.year-birthday.year} years')
age=relativedelta(today, birthday)
print(f"Age: {age.years} Years, {age.months} Months, {age.days} Days")

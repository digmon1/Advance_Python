from datetime import datetime
date_string = "20/07/2026"
d = datetime.strptime(date_string, "%d/%m/%Y")
print(date_string)
print(type(date_string))
print()
print(d)
print(type(d))


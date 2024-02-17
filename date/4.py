from datetime import datetime
day1 = datetime(2024, 2, 10, 3, 25)
day2 = datetime(2024, 2, 12, 3, 25)
d = day2 - day1
print(d.total_seconds())
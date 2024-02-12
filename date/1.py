from datetime import datetime, timedelta
d = datetime.now()
days = timedelta(days= 5)
result = d - days
print (result)
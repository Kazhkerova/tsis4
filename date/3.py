from datetime import datetime
now = datetime.now()
date = now.replace(microsecond=0)
print (now)
print (date)
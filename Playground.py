from datetime import datetime

print("today:", datetime.today())
print("now:", datetime.now())
print("utcnow:", datetime.utcnow())

from datetime import time

t = time(14, 53)
print(t.strftime("%H:%M:%S"))

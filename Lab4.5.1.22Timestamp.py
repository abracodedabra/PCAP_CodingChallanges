import time
from datetime import datetime

tts = datetime(2020, 11, 4, 14, 53, 00)

print(tts.strftime('%Y/%m/%d %H:%M:%S'))
print(tts.strftime('%y/%B/%d %H:%M:%S %p'))
print(tts.strftime('%a, %Y %b %d'))
print(tts.strftime('%A, %Y %B %d'))
print(tts.strftime("Weekday: %w"))
print(tts.strftime("Day of the year: %j"))
print(tts.strftime("Week number of the year: %U"))
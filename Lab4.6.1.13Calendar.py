import calendar

class myCalendar(calendar.Calendar):

    def count_weekday_in_year(self, year, weekday):
        currMonth = 0
        countDays = 0

        for month in range(12):
            currMonth += 1
            for day in self.monthdays2calendar(year, currMonth):
                sZ = 0
                for i in day:
                    if day[sZ][0] == 0:
                        sZ += 1
                        continue
                    elif day[sZ][1] == weekday:
                        countDays += 1
                        sZ += 1
                    else:
                        sZ += 1
                        continue

        print(countDays)

objekt = myCalendar()
objekt.count_weekday_in_year(2000, calendar.SUNDAY)

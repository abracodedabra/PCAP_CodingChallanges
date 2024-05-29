class WeekDayError(Exception):
    pass


class Weeker:
    dayStorage = ('Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun')

    def __init__(self, day):
        if day in self.dayStorage:
            self.chosenDay = day
        else:
            raise WeekDayError

    def __str__(self):
        return self.chosenDay

    def add_days(self, n):
        indexChosenDay = self.dayStorage.index(self.chosenDay)
        newIndex = (indexChosenDay + n) % 7
        self.newDay = self.dayStorage[newIndex]
        self.__init__(self.newDay)


    def subtract_days(self, n):
        indexChosenDay = self.dayStorage.index(self.chosenDay)
        newIndex = (indexChosenDay - n) % 7
        self.newDay = self.dayStorage[newIndex]
        self.__init__(self.newDay)


try:
    weekday = Weeker('Mon')
    print(weekday)
    weekday.add_days(15)
    print(weekday)
    weekday.subtract_days(23)
    print(weekday)
    weekday = Weeker('Monday')
except WeekDayError:
    print("Sorry, I can't serve your request.")
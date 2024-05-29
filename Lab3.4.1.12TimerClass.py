class Timer:
    def __init__(self, hour = 0, minute = 0, second = 0):
        self.timeHour = hour
        self.timeMinute = minute
        self.timeSecond = second
        self.timeToSeconds()


    def __str__(self):
        if self.timeHour < 10:
            tmpH = "0" + str(self.timeHour)
        else:
            tmpH = str(self.timeHour)
        if self.timeMinute < 10:
            tmpM = "0" + str(self.timeMinute)
        else:
            tmpM = str(self.timeMinute)
        if self.timeSecond < 10:
            tmpS = "0" + str(self.timeSecond)
        else:
            tmpS = str(self.timeSecond)
        self.displayTime = tmpH + ":" + tmpM + ":" + tmpS

        return self.displayTime

    def timeToSeconds(self):
        minInSec = self.timeMinute * 60
        hrInSec = (self.timeHour * 60) * 60
        self.timeInSec = hrInSec + minInSec + self.timeSecond
        return self.timeInSec

    def next_second(self):
        tmp = self.timeInSec + 1
        if tmp > 86399:
            tmp = tmp - 86400
        self.timeHour = tmp // 3600
        tmp = tmp % 3600
        self.timeMinute = tmp // 60
        tmp = tmp % 60
        self.timeSecond = tmp
        self.__str__()

    def prev_second(self):
        tmp = self.timeInSec - 1
        if tmp < 0:
            tmp = tmp + 86400
        self.timeHour = tmp // 3600
        tmp = tmp % 3600
        self.timeMinute = tmp // 60
        tmp = tmp % 60
        self.timeSecond = tmp % 60
        self.__str__()


timer = Timer(23, 59, 59)
print(timer)
timer.next_second()
print(timer)
timer.prev_second()
print(timer)
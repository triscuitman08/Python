class WeekDayError(Exception):
    pass
	

class Weeker:
    __listDays = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
    

    def __init__(self, day):
        if day not in Weeker.__listDays:
            raise WeekDayError()
        self.__day = day

    def __str__(self):
        return self.__day

    def add_days(self, n):
        dayIndex = Weeker.__listDays.index(self.__day)
        newIndex = (dayIndex + n) % 7
        self.__day = Weeker.__listDays[newIndex]

    def subtract_days(self, n):
        dayIndex = Weeker.__listDays.index(self.__day)
        newIndex = (dayIndex - n) % 7
        self.__day = Weeker.__listDays[newIndex]


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
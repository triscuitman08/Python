class Timer:
    def __init__( self, h = 0, m = 0, s = 0 ):
        self.__hours = h
        self.__minutes = m
        self.__seconds = s

    def __str__(self):
        return formatTime(self.__hours) + ":" + formatTime(self.__minutes) + ":" + formatTime(self.__seconds)

    def next_second(self):
        if self.__seconds == 59:
            if self.__minutes == 59:
                if self.__hours == 23:
                    self.__hours = 0
                else:
                    self.__hours +=1
                self.__minutes = 0
            else:
                self.__minutes +=1
            self.__seconds = 0
        else:
            self.__seconds +=1

    def prev_second(self):
        if self.__seconds == 0:
            if self.__minutes == 0:
                if self.__hours == 0:
                    self.__hours = 23
                else:
                    self.__hours -=1
                self.__minutes = 59
            else:
                self.__minutes -=1
            self.__seconds =0
        else:
            self.__seconds -=1

def formatTime(number):
    if number < 10:
        return(f"0{number}")
    else:
        return(str(number))

timer = Timer(23, 59, 59)
print(timer)
timer.next_second()
print(timer)
timer.prev_second()
print(timer)
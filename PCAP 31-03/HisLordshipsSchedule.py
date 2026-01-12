class ScheduleError(Exception):
    pass

class TimeSlot:
    def __init__(self,hour,activity):
        if hour <= 23 and hour >= 0:
            self.__hour = hour
        else:
            raise ScheduleError("Bertram may be omnicient, but he can't alter the flow of time! We need a real hour value!")
        self.__activity = activity
    
    def description(self):
         return (f"{self.__hour:02d}:00 - {self.__activity}")

class DailySchedule:
    def __init__(self, name):
        self.__name = name
        self.__activities = []
    
    def add_activity(self, hour, activity):
        self.__activities.append(TimeSlot(hour,activity))
    
    def show_schedule(self):
        for obj in self.__activities:
            print(obj.description())
    
    def count_activities(self):
        return len(self.__activities)
    
bertram_day = DailySchedule("Lord Bertram")
bertram_day.add_activity(23, "Yowl for breakfast")
bertram_day.add_activity(7, "Ignore breakfast")
bertram_day.add_activity(9, "Nap on keyboard")
bertram_day.add_activity(14, "Judge humans silently")
bertram_day.add_activity(18, "Demand second breakfast")

bertram_day.show_schedule()
print(f"Total activities: {bertram_day.count_activities()}")
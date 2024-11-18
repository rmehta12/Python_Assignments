class Time:
    def __init__(self, hours, minutes):
        self.hours = hours
        self.minutes = minutes

    def addTime(self, t):
        total_minutes = self.minutes + t.minutes
        total_hours = self.hours + t.hours + total_minutes // 60
        return Time(total_hours, total_minutes % 60)

    def displayTime(self):
        print(f"{self.hours} hours and {self.minutes} minutes")

    def displayMinute(self):
        print(f"Total minutes: {self.hours * 60 + self.minutes}")


t1 = Time(2, 50)
t2 = Time(1, 20)
t3 = t1.addTime(t2)
t3.displayTime()
t3.displayMinute()

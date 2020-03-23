class Clock(object):

    def __init__(self,hours=0, minutes=0, seconds=0):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds


    def tick(self):
        """ Time will be advanced by one second """
        if self.seconds == 59:
            self.seconds = 0
            if (self.minutes == 59):
                self.minutes = 0
                self.hours = 0 if self.hours==23  else self.hours + 1
            else:
                self.minutes += 1;
        else:
            self.seconds += 1;

    def display(self):
        print("%d:%d:%d" % (self.hours, self.minutes, self.seconds))

    def __str__(self):
        return "%2d:%2d:%2d" % (self.hours, self.minutes, self.seconds)

class Calendar(object):
    months = (31,28,31,30,31,30,31,31,30,31,30,31)

    def __init__(self, day=1, month=1, year=1900):
        self.day = day
        self.month = month
        self.year = year

    def leapyear(self,y):
        if y % 4:
	   # not a leap year
           return 0;
        else:
           if y % 100:
               return 1;
           else:
               if y % 400:
                  return 0
               else:
                  return 1;

    def advance(self):
        months = Calendar.months
        max_days = months[self.month-1]
        if self.month == 2:
            max_days += self.leapyear(self.year)
        if self.day == max_days:
            self.day = 1
            if (self.month == 12):
                self.month = 1
                self.year += 1
            else:
                self.month += 1
        else:
            self.day += 1


    def __str__(self):
       return str(self.day)+"/"+ str(self.month)+ "/"+ str(self.year)


class CalendarClock(Clock, Calendar):

   def __init__(self, day,month,year,hours=0, minutes=0,seconds=0):
        Calendar.__init__(self, day, month, year)
        Clock.__init__(self, hours, minutes, seconds)

   def __str__(self):
       return Calendar.__str__(self) + ", " + Clock.__str__(self)



x = CalendarClock(24,12,57)
print(x)
for i in range(1000):
      x.tick()
for i in range(1000):
      x.advance()
print(x)
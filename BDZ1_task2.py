import calendar
from tabulate import tabulate

calendar.setfirstweekday(calendar.SUNDAY)
month = calendar.monthcalendar(*[int(input()), int(input())][::-1])
print(tabulate(month, headers=['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']))

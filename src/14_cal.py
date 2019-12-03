"""
The Python standard library's 'calendar' module allows you to
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `14_cal.py month [year]`
and does the following:
 - If the user doesn't specify any input, your program should
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.
"""

import sys
import calendar
from datetime import datetime

userInput = input("gimmi a month(as a number), and a year. \n separated by commas.  unless you dont want to: ").split(',')

def get_calendar(aMonth=datetime.now().month, aYear=datetime.now().year):
    calendar.setfirstweekday(calendar.SUNDAY)
    return calendar.monthcalendar(aYear, aMonth)

def calendarStlyes(userInput):
  if (userInput.len() == 2):
    get_calendar(userInput[0], userInput[1])
  elif (userInput.len() == 0):
    get_calendar()
  elif (userInput.len() == 1):
    get_calendar(userInput[0], datetime.now().year)
  else:
    print("WHAT ARE YOU EVEN DOING!? \n first, enter a number 1-12 for the month \n then a comma \n then enter a 4-digit number for the year. \n TRY IT AGAIN, DINGUS.")
  
  

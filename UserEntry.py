#UserEntry.py
#M.Campbell
#31/08/2024

from datetime import datetime

print('Welcome to the Sleep Calculator!')

#ask for users year of birth
yob = int(input('Please enter your year of birth..\n\n'))

#calculates the current year minus users year of birth
age = datetime.now().year - yob

hours = age * 2555

print('You have slept a total of ', hours, 'hours')

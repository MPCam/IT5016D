#LearningActivity23Q2.py
#M.Campbell
#01/09/2024

from datetime import datetime
from datetime import timedelta

date = input('Please senter at date in format DD Mmm YYYY...\n\n')

#converting to datetime
date_object = datetime.strptime(date, '%d %b %Y')

#converting to same format as input
future_date = datetime.strftime(date_object + timedelta(weeks=2), '%d %b %Y')

print('\nThe date in two weeks will be ', future_date)

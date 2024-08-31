#LearningActivity23Q1.py
#M.Campbell
#01/09/2024

from datetime import datetime
from datetime import timedelta

date = input('Please senter at date in format DD Mmm YYYY...\n\n')

date_object = datetime.strptime(date, '%d %b %Y')

print('\nThat date 125 days ago is ', date_object - timedelta(days=125))

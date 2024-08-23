from datetime import datetime
from datetime import timedelta

date_input = input('Please enter your DOB in the format DD MMM YYYY: \n')

date_object = datetime.strptime(date_input, '%d %b %Y')

print('The year entered is', date_object.year, '\n')

my_age = datetime.today() - date_object

print('My exact age is', my_age, '\n')
print('My exact age just in days is', my_age.days, 'days\n')
print('My exact age just in years is', int(my_age.days/365), 'years\n')
print('In 10 days time my age will be', datetime.today() + timedelta(days=10), '.\n')
print('I will be double my age in', datetime.today() + my_age, '.')

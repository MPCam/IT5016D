from datetime import datetime, timedelta

duration = 5

run = input('Enter s to begin...')

period = timedelta(seconds=1)

next_time = datetime.now() + period

counter = 0

while run == 's' and counter < duration:
    if next_time <= datetime.now():
        print('..', counter)
        counter += 1
        next_time += period

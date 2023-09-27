hourNow = int(input('What is the hour currently? '))
hoursAdded = int(input('How many hours after this hour you want to wait? '))
finalHour = (hoursAdded + hourNow) % 24
print('The time the clock will go off is', finalHour)


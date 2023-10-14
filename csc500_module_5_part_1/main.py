months = [
    'January',
    'February',
    'March',
    'April',
    'May',
    'June',
    'July',
    'August',
    'September',
    'October',
    'November',
    'December'
]
monthCounter = 0
totalInchesOfRain = 0

numberOfYears = int(input('To calculate the rainfall stats please tell me the number of years for consideration '))

for year in range(1, numberOfYears+1):
    for month in range(12):
        inches = int(
            input(
                'Enter the inches of rain for the month of ' +
                str(months[month]) +
                ' and of year ' +
                str(year) +
                ' '
            )
        )

        monthCounter = monthCounter + 1
        totalInchesOfRain = totalInchesOfRain + inches

averageRainfallPerMonth = totalInchesOfRain/monthCounter
print('The number of months is ', monthCounter)
print('The total inches of rainfall is ', totalInchesOfRain)
print('The average rainfall per month for the entire period is ', averageRainfallPerMonth)

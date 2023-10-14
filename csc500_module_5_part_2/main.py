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

for month in range(12):
    numberOfBooks = int(
        input(
            'Please enter the number of books you have purchased for the month of ' +
            str(months[month]) +
            ' '
        )
    )

    if numberOfBooks < 0:
        print("That was a wrong entry.")

    elif numberOfBooks <= 1:
        print('You earned 0 points for the month of ' + str(months[month]))

    elif numberOfBooks <= 3:
        print('You earned 5 points for the month of ' + str(months[month]))

    elif numberOfBooks <= 5:
        print('You earned 15 points for the month of ' + str(months[month]))

    elif numberOfBooks <= 7:
        print('You earned 30 points for the month of ' + str(months[month]))

    else:
        print('You earned 60 points for the month of ' + str(months[month]))

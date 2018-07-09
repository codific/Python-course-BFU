day_of_week = input('Enter the day of the week: ')

# Classical approach using multiple if/elif statements
# since Python doesn't have switch/case
if day_of_week == 'Monday':
    print('Oh, no! It is Monday again...')
elif day_of_week == 'Tuesday':
    print('It is only Tuesday?')
elif day_of_week == 'Wednesday':
    print('Halfway there.')
elif day_of_week == 'Thursday':
    print('We almost did it.')
elif day_of_week == 'Friday':
    print('Woohoo! Party time!')
elif day_of_week == 'Saturday' or day_of_week == 'Sunday':
    print('Time for some rest.')
else:
    print('What day is that?')
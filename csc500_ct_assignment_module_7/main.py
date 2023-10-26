room_num_dic = {
    'csc101': 3004,
    'csc102': 4501,
    'csc103': 6755,
    'net110': 1244,
    'com241': 1411
}

instructors_dic = {
    'csc101': 'Haynes',
    'csc102': 'Alvarado',
    'csc103': 'Rich',
    'net110': 'Burke',
    'com241': 'Lee'
}

meeting_time_dic = {
    'csc101': '8:00 a.m.',
    'csc102': '9:00 a.m.',
    'csc103': '10:00 a.m.',
    'net110': '11: a.m.',
    'com241': '1:00 p.m.'
}

c_num = str(input('Please enter the course number...')).casefold()

if c_num in room_num_dic.keys():
    print(
        'The course room number is ' + str(room_num_dic.get(c_num)) +
        ' the instructor is ' + str(instructors_dic.get(c_num)) +
        ' and the meeting time is ' + str(meeting_time_dic.get(c_num))
    )
else:
    print('That course doesn\'t exist!')

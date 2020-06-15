#task seasons
my_list = ['winter', 'spring', 'summer', 'autumn']
my_dict = {'winter': (12, 1, 2), 'spring': (3, 4, 5), 'summer': (6, 7, 8), 'autumn': (9, 10, 11)}
while True:
    month = input('write month')
    if month.isdigit():
        month = int(month)
        if month > 0 and month < 13:
            break
    print('write digit num ot 1 do 12')
for i in my_dict.keys():
    if month in my_dict[i]:
        print(i)
if month == 12 or month == 1 or month == 2:
    print(my_list[0])
elif month == 3 or month == 4 or month == 5:
    print(my_list[1])
elif month == 6 or month == 7 or month == 8:
    print(my_list[3])
else:
    print(my_list[4])

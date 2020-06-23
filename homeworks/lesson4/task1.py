from sys import argv

name, clockwork, time, award = argv
try:
    clockwork = float(input('Введите выроботку в часах:\n'))
    time = float(input('введите количество часов:\n'))
    award = float(input('введите премию:\n'))
    res = clockwork * time + award
    print(f'Заработная плата сотрудника составляет:\n {res}')
except ValueError:
    print('напечатано не число')

def my_func():
    try:
        clockwork = float(input('Введите выроботку в часах:\n'))
        time = float(input('введите количество часов:\n'))
        award = float(input('введите премию:\n'))
        res = clockwork * time + award
        print(f'результат:\n{res}')
    except ValueError:
        print('введено не число')
my_func()
#1'st task
def my_div(*args):
    print('this function will count division 1 argument by 2')
    arg_1 = float(input('write 1 arg: '))
    arg_2 = float(input('write 2 arg: '))
    while arg_2 == 0:
        print('Enter non zero arg: ')
        arg_2 = float(input('write arg: '))
    return(arg_1 / arg_2)
print(f'{my_div()}')
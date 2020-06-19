def my_sum(arg_1, arg_2, arg_3):
    if arg_1 > arg_3 and arg_2 > arg_3:
        return arg_1 + arg_2
    elif arg_2 > arg_1 and arg_3 > arg_1:
        return arg_2 + arg_3
    else:
        return arg_3 + arg_1
print(f'{my_sum(int(input("write first arg: ")), int(input("write 2 arg: ")), int(input("write 3 arg: ")))}')

def mu_func(name, surname, y , city,email, phone):
    return (name, surname, y , city,email, phone)
print(f'{mu_func(input("введите имя"), input("введите фамилию"), int(input("введите год рождения")) , input("введите город проживания"),input("введите email"), input("введите телефон"))}')

#task exchange of index elements
while True:
    amount = input('enter string length')
    if amount.isdigit():
        amount = int(amount)
        break
    print('write integer num')
counter = 0
i = 0
my_list = []
while counter < amount:
    my_list.append(input('enter string character'))
    counter += 1
for id in range(int(len(my_list)/2)):
    my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
    i += 2
print(my_list)

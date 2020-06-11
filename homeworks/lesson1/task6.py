#this is a training calculation program
while True:
    useranswer1 = input("write The result of the first day in kilometers: ")
    if useranswer1.isdigit():
        useranswer1 = int(useranswer1)
        break
    print("error, write a integer number")
while True:
    useranswer2 = input("introducing the distance you want to run in the future: ")
    if useranswer2.isdigit():
        useranswer2 = int(useranswer2)
        break
    print("error, write a integer number")
days = 1
while useranswer1 < useranswer2:
    useranswer1 = useranswer1 * 1.1
    days = days + 1
print(f" you need {days} days to achieve the desired result")

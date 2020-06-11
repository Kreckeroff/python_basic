#program to convert time to format hh:mm:ss
print("this program is designed to convert time into a format hh:mm:ss")
while True:
    time = input("write the time in seconds: ")
    if time.isdigit():
        time = int(time)
        break
    print("error, write a integer number")
hours = time // 3600
minute = (time - hours * 3600) // 60
seconds = (time - hours * 3600 - minute * 60)
result = ('time format hh:mm:ss {hours} : {minute} : {seconds}').format(hours=hours, minute=minute, seconds=seconds)
print(result)

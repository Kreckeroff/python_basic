#This program is looking for the largest digit in the number that the user enters
while True:
    n = input("write the number: ")
    if n.isdigit():
        n = int(n)
        break
    print("error, write a integer number")
max = n % 10
while n >= 1:
    n = n // 10
    if n % 10 > max:
        max = n % 10
    if n > 9:
        continue
    else:
        print(max)
        break

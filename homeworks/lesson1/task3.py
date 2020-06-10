#this program is looking for the sum n+nn+nnn of the number n
while True:
    n = input("write the number: ")
    if n.isdigit():
        n = int(n)
        break
    print("error, write a integer number")
result = (n + int(str(n)+str(n)) + int(str(n) + str(n) +str(n)))
print("n + nn + nnn = ",result)
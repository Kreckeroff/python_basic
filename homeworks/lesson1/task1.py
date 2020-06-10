str_name = "UserName"
result_hello = 'Hello {name}\n'.format(name=str_name)
print(result_hello)
while True:
    age = input('how old are you :')
    if age.isdigit():
        age=int(age)
        break
    print("Error, write number")
name = input("write you name :")
surname = input("write you surname :")
result = f'{name} {surname}, you are {age} years old'
print(result)
int_num1 = 10
int_num2 = 5
conclusion = int_num1 // int_num2  #integer division result
print(conclusion)

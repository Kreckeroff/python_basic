#this program considers companies profitability
while True:
    profit = input("enter your company profit: ")
    if profit.isdigit():
        profit = int(profit)
        break
    print("write integer num")
while True:
    loss = input("enter your company losses: ")
    if loss.isdigit():
        loss = int(loss)
        break
    print("write integer num")
if profit > loss:
    result = profit - loss
    print(f"Your company makes a profit. your company’s profit is {result}")
elif profit == loss:
    print("your company runs at 0")
else:
    result = loss - profit
    print(f"Your company brings losses. your company’s losses will amount to {result}")
while True:
    employee = input("enter the number of employees: ")
    if employee.isdigit():
        employee = int(employee)
        break
    print("write integer num")
if profit > loss:
    print(f"profit per employee: {result/employee}")
else:
    print("your company is operating at a loss, we cannot calculate the company's profit per employee")

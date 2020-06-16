while True:
    user_answer = input('write num: ')
    if user_answer.isdigit():
        user_answer = int(user_answer)
        break
    print('write digit num')
rating = [7, 5, 3, 3, 2]
rating.append(user_answer)
rating.sort(reverse=True)
print(rating)

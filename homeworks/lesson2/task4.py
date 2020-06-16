line = input('write string')
num_line = 0
line1 = []
for id in range(line.count(' ') + 1):
    line1 = line.split()
    num_line += 1
    if len(str(line1)) < 11:
        print(f'{num_line}: {line1[id]}')
    else:
        print(f'{num_line}: {line1[id] [0:10]}')

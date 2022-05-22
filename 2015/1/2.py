floor = 0
i = 0
with open('input', 'r') as reader:
    for line in reader:
        for char in line:
            if char == "(":
                floor += 1
            else:
                floor -= 1
            i += 1
            if floor == -1:
                break
print(i)
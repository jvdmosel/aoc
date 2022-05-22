floor = 0
with open('input', 'r') as reader:
    for line in reader:
        for char in line:
            if char == "(":
                floor += 1
            else:
                floor -= 1
print(floor)
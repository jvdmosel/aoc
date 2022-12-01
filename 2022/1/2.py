with open("input", 'r') as reader:
    root, left, right = 0, 0, 0
    sum = 0
    for line in reader:
        if line.strip():
            sum += int(line)
        else:
            if sum >= root and sum >= left and sum >= right:
                root = left
                left = right
                right = sum
            elif sum >= root and sum >= left:
                root = left
                left = sum
            elif sum >= root:
                root = sum
            sum = 0
    sol = root + left + right
    print(sol)

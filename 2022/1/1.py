with open("input", 'r') as reader:
    max_sum = 0
    sum = 0
    for line in reader:
        if line.strip():
            sum += int(line)
        else:
            max_sum = sum if max_sum < sum else max_sum
            sum = 0
    print(max_sum)

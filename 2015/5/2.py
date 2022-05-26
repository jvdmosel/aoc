result = 0
with open("input", "r") as reader:
    for line in reader:
        repeated = False
        twice = False
        hashmap = {}
        hashmap[line[:2]] = 1
        for i in range(2, len(line)):
            if line[i-1:i+1] not in hashmap:
                hashmap[line[i-1:i+1]] = 1
            elif (line[i-2:i] != line[i-1:i+1]
                    or line[i-3:i-1] == line[i-1:i+1]):
                hashmap[line[i-1:i+1]] += 1
                twice = True
            if line[i-2] == line[i]:
                repeated = True
        if repeated and twice:
            result += 1
print(result)

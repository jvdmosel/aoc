result = 0
with open("input", "r") as reader:
    for line in reader:
        i = j = 0
        hashmap = {}
        hashmap[(i, j)] = 1
        result += 1
        for char in line:
            match char:
                case "^":
                    j += 1
                case ">":
                    i += 1
                case "v":
                    j -= 1
                case "<":
                    i -= 1
            if (i, j) not in hashmap:
                hashmap[(i, j)] = 1
                result += 1
            else:
                hashmap[(i, j)] += 1
print(result)

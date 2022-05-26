result = 0
with open("input", "r") as reader:
    for line in reader:
        repeated = False
        vowels = 0
        disallowed = False
        for i in range(1, len(line)):
            r = 2 * line[i-1]
            match line[i-1:i+1]:
                case "ab" | "cd" | "pq" | "xy":
                    disallowed = True
            if 2 * line[i-1] == line[i-1:i+1]:
                repeated = True
            match line[i-1]:
                case "a" | "e" | "i" | "o" | "u":
                    vowels += 1
        if vowels >= 3 and repeated and not disallowed:
            result += 1
print(result)

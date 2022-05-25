result = 0
with open("input", "r") as reader:
    for line in reader:
        i_s = j_s = i_r = j_r = 0
        hashmap = {}
        hashmap[(i_s, j_s)] = 2
        result += 1
        for k, char in enumerate(line):
            match char:
                case "^":
                    if k % 2 == 0:
                        j_s += 1
                    else:
                        j_r += 1
                case ">":
                    if k % 2 == 0:
                        i_s += 1
                    else:
                        i_r += 1
                case "v":
                    if k % 2 == 0:
                        j_s -= 1
                    else:
                        j_r -= 1
                case "<":
                    if k % 2 == 0:
                        i_s -= 1
                    else:
                        i_r -= 1
            if k % 2 == 0 and (i_s, j_s) not in hashmap:
                hashmap[(i_s, j_s)] = 1
                result += 1
            elif k % 2 == 1 and (i_r, j_r) not in hashmap:
                hashmap[(i_r, j_r)] = 1
                result += 1
print(result)
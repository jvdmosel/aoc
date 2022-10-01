with open("input", "r") as reader:
    for line in reader:
        result = line
        for i in range(40):
            tmp = ""
            prev = result[0]
            cnt = 1
            for digit in result[1:]:
                if digit == prev:
                    cnt += 1
                else:
                    tmp += str(cnt) + prev
                    cnt = 1
                prev = digit
            tmp += str(cnt) + prev
            result = tmp
        print(len(result))

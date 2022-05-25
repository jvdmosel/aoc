sum = 0
with open("input", "r") as reader:
    for line in reader:
        l, w, h = [int(i) for i in line.split("x")]
        lw = l * w
        lh = l * h
        wh = w * h
        sum += 2 * lw + 2 * lh + 2 * wh + min([lw, lh, wh])
print(sum)

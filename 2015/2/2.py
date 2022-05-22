sum = 0
with open("input", "r") as reader:
    for line in reader:
        x, y, z = sorted([int(i) for i in line.split("x")])
        bow = x * y * z
        ribbon = 2 * x + 2 * y
        sum += ribbon + bow
print(sum)
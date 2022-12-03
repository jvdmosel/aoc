rps = {
    "X": {"A": 4, "B": 1, "C": 7},
    "Y": {"A": 8, "B": 5, "C": 2},
    "Z": {"A": 3, "B": 9, "C": 6}
}

with open("input", 'r') as reader:
    score = 0
    for line in reader:
        score += rps[line[2]][line[0]]
    print(score)

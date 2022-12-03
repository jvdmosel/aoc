response = {
    "X": {"A": "S", "B": "R", "C": "P"},
    "Y": {"A": "R", "B": "P", "C": "S"},
    "Z": {"A": "P", "B": "S", "C": "R"}
}

score = {
    "R": {"A": 4, "B": 1, "C": 7},
    "P": {"A": 8, "B": 5, "C": 2},
    "S": {"A": 3, "B": 9, "C": 6}
}

with open("input", 'r') as reader:
    total = 0
    for line in reader:
        total += score[response[line[2]][line[0]]][line[0]]
    print(total)

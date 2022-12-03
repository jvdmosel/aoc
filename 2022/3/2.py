def yield_groups(lines: list):
    for i in range(0, len(lines), 3):
        yield sorted(lines[i:i+3], key=len)


with open("input", 'r') as reader:
    prio = 0
    lines = reader.readlines()
    for group in yield_groups(lines):
        for char in group[0]:
            if char in group[1] and char in group[2]:
                prio += ord(char)-96 if char.islower() else ord(char)-38
                break
    print(prio)

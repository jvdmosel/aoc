with open("input", 'r') as reader:
    prio = 0
    for line in reader:
        compartment_len = int((len(line)-1)/2)
        left = line[:compartment_len]
        right = line[compartment_len:]
        for char in left:
            if char in right:
                prio += ord(char)-96 if char.islower() else ord(char)-38
                break
    print(prio)

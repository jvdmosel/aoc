def is_unique(s: str):
    present = 0
    for c in s:
        # get correspnding bit
        bit = ord(c)-ord("a")

        # check if bit is already present
        if present & (1 << bit) > 0:
            return False

        # set bit
        present |= (1 << bit)
    return True


with open("input", 'r') as reader:
    for line in reader:
        for i in range(len(line)):
            if is_unique(line[i:i+4]):
                print(i+4)
                break

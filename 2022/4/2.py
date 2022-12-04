def fully_contained(A: int, B: int, C: int, D: int) -> bool:
    return (C <= A <= D) or (C <= B <= D) or (A <= C <= B) or (A <= D <= B)


with open("input", 'r') as reader:
    sum = 0
    for line in reader:
        pair = line.split(",")
        range_1 = pair[0].split("-")
        range_2 = pair[1].strip().split("-")
        A = int(range_1[0])
        B = int(range_1[1])
        C = int(range_2[0])
        D = int(range_2[1])
        if fully_contained(A, B, C, D):
            sum += 1
    print(sum)

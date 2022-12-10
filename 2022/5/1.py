stacks = []

with open("input", 'r') as reader:
    lines = reader.readlines()
    # find index of line containing stack indices
    stack_index = 0
    while lines[stack_index][1] != "1":
        stack_index += 1

    # parse stacks and push in correct order (bottom to top)
    for j in range(1, len(lines[stack_index]), 4):
        stacks.append([])
        for i in range(stack_index-1, -1, -1):
            if lines[i][j] != " ":
                stacks[len(stacks)-1].append(lines[i][j])

    # rearrange
    for line in lines[stack_index+2:]:
        items_moved, a, b = [int(s) for s in line.split() if s.isdigit()]
        for i in range(items_moved):
            # stacks are 0-based but rearrangements are 1-based
            stacks[b-1].append(stacks[a-1].pop())

    # join top crate of each stack
    print("".join([crate[-1] for crate in stacks]))

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
        # stacks are 0-based but rearrangements are 1-based
        first_crate = len(stacks[a-1])-items_moved
        stacks[b-1] += stacks[a-1][first_crate:]
        stacks[a-1] = stacks[a-1][:first_crate]
    # join top crate of each stack
    print("".join([crate[-1] for crate in stacks if crate != []]))

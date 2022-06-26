with open("input", "r") as reader:
    code_length = 0
    memory_length = 0
    for line in reader:
        line = line.strip()
        code_length += len(line)
        memory_length += 2
        for c in line:
            if c == "\"" or c == "\\":
                memory_length += 2
            else:
                memory_length += 1
    print(memory_length-code_length)

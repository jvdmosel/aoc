with open("input", "r") as reader:
    code_length = 0
    memory_length = 0
    for line in reader:
        line = line.strip()
        code_length += len(line)
        i = 1
        while i < len(line)-1:
            if line[i:i+2] == "\\x":
                i += 4
            elif line[i:i+2] == "\\\\" or line[i:i+2] == "\\\"":
                i += 2
            else:
                i += 1
            memory_length += 1
    print(code_length-memory_length)


def put(x, t):
    x = int(x) if x.isdigit() else circuit[x]
    circuit[t] = x
    print(f"put {x} into {t}")


def neg(x, t):
    circuit[t] = ~circuit[x] & 0xffff
    print(f"neg {x} into {t}")


def gate(x, op, y, t):
    x = int(x) if x.isdigit() else circuit[x]
    y = int(y) if y.isdigit() else circuit[y]
    match op:
        case "LSHIFT":
            circuit[t] = x << y
            print(f"lshift {x} by {y} into {t}")
        case "RSHIFT":
            circuit[t] = x >> y
            print(f"rshift {x} by {y} into {t}")
        case "AND":
            circuit[t] = x & y
            print(f"{x} and {y} into {t}")
        case "OR":
            circuit[t] = x | y
            print(f"{x} or {y} into {t}")


def not_solved(x):
    return x not in circuit.keys() and not x.isdigit()


def solve(x):
    if not_solved(x):
        if not_solved(g[x][1]):
            solve(g[x][1])
        if g[x][0].__name__ == "gate" and "SHIFT" not in g[x][2] and not_solved(g[x][3]):
            solve(g[x][3])
        g[x][0](*g[x][1:])


circuit = {}
g = {}
with open("input", "r") as reader:
    for line in reader:
        l, r = line.split(" -> ")
        wire = r.strip()
        parts = [part.strip() for part in (l.split(" "))]
        if len(parts) == 1:
            g[wire] = put, parts[0], wire
        elif len(parts) == 2:
            g[wire] = neg, parts[1], wire
        else:
            g[wire] = gate, parts[0], parts[1], parts[2], wire
solve("a")
print(circuit["a"])

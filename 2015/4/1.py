from hashlib import md5

with open("input", "r") as reader:
    for line in reader:
        i = 1
        while md5(f"{line}{i}".encode()).hexdigest()[:5] != "00000":
            i += 1
        print(i)

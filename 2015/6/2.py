import numpy as np

arr = np.zeros((1000, 1000))

with open("testinput", "r") as reader:
    for line in reader:
        splitted = line.split(" ")
        if line.startswith("turn"):
            x1, y1 = tuple(map(int, splitted[2].split(",")))
            x2, y2 = tuple(map(int, splitted[4].split(",")))
            if splitted[1] == "on":
                m = np.full((x2-x1+1, y2-y1+1), 1)
            else:
                m = np.zeros((x2-x1+1, y2-y1+1))
                for i_m, i_arr in enumerate(range(x1, x2+1)):
                    for j_m, j_arr in enumerate(range(y1, y2+1)):
                        if arr[i_arr][j_arr] >= 1:
                            m[i_m][j_m] = -1
        else:
            x1, y1 = tuple(map(int, splitted[1].split(",")))
            x2, y2 = tuple(map(int, splitted[3].split(",")))
            m = np.full((x2-x1+1, y2-y1+1), 2)
        arr[x1:x2+1, y1:y2+1] += m
print(int(arr[arr > 0].sum()))

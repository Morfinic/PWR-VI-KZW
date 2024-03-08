dataPath: str = "Dane/subDane/data."

for i in range(1, 1+1):
    rpqTab = list()
    t: int = 0
    Cmax: int = 0

    with open(dataPath + str(i) + ".txt", 'r') as f:
        print(f"Reading {dataPath + str(i) + ".txt"}")

        for line in f:
            rpqTab.append([int(x) for x in line.strip('\n').split(' ')])

        rpqTab = reversed(rpqTab)

        for proc in rpqTab:
            t = max(t, proc[0])
            t += proc[1]
            Cmax = max(Cmax, t + proc[2])

    print(Cmax)
def liczCmax(procList):
    t: int = 0
    Cmax: int = 0

    for proc in procList:
        t = max(t, proc[0])
        t += proc[1]
        Cmax = max(Cmax, t + proc[2])

    return Cmax


def TabooSearch(tasks, maxIter=1_000):
    bestOrder = tasks.copy()

    for _ in range(maxIter):
        bestCmax = float("inf")
        bestI = 0
        bestJ = 1

        for i in range(0, len(tasks)-1):
            for j in range(i+1, len(tasks)):
                if i == j:
                    continue

                tasks[i], tasks[j] = tasks[j], tasks[i]
                Cmax = liczCmax(tasks)

                if Cmax < bestCmax:
                    bestCmax = Cmax
                    bestI = i
                    bestJ = j

                tasks[i], tasks[j] = tasks[j], tasks[i]

        tasks[bestI], tasks[bestJ] = tasks[bestJ], tasks[bestI]
        if liczCmax(tasks) < liczCmax(bestOrder):
            bestOrder = tasks

    print("Order:", [entry[-1] for entry in bestOrder])

    return liczCmax(bestOrder)


if __name__ == '__main__':
    dataPath: str = "./data/data."

    for i in range(1, 4+1):
        rpqTab = list()

        with open(dataPath + str(i) + ".txt", 'r') as f:
            print(f"\nReading {dataPath + str(i) + '.txt'}")

            for line in f:
                rpqTab.append([int(x) for x in line.strip('\n').split(' ')])
            rpqTab = [entry + [idx+1] for idx, entry in enumerate(rpqTab)]

            print("Cmax: ", TabooSearch(rpqTab))

# Cmax schrage data1: 13981
# Cmax schrage data2: 21529
# Cmax schrage data3: 31683
# Cmax schrage data4: 34444

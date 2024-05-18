import random
from scipy.special import expit
import matplotlib.pyplot as plt
import math


def liczCmax(procList):
    t: int = 0
    Cmax: int = 0

    for proc in procList:
        t = max(t, proc[0])
        t += proc[1]
        Cmax = max(Cmax, t + proc[2])

    return Cmax


def symulowaneWyrzazanie(tasks, T: int, TEnd: int, epochs: int):
    tmp = list()

    while T > TEnd:
        for _ in range(epochs):
            neighbour = 3
            j = random.randint(0, len(tasks) - 1)
            k = random.choice([x for x in range(j-neighbour, j+neighbour+1) if x != j and 0 < x < len(tasks)])

            CMaxPre = liczCmax(tasks)
            tasks[j], tasks[k] = tasks[k], tasks[j]
            CMaxPost = liczCmax(tasks)

            if CMaxPre > CMaxPost:
                pass
            else:
                CMaxDiff = CMaxPost - CMaxPre
                r = random.random()
                if r >= expit(CMaxDiff / T):
                    pass
                else:
                    tasks[j], tasks[k] = tasks[k], tasks[j]

            tmp.append(liczCmax(tasks))

        T -= 1

    plt.plot(tmp)
    plt.show()

    print("Order:", [entry[-1] for entry in tasks])

    return liczCmax(tasks)


def tuning(tasks):
    minVal, maxVal = math.inf, 0

    for _ in range(10 ** 3):
        neighbour = 3
        j = random.randint(0, len(tasks) - 1)
        k = random.choice([x for x in range(j-neighbour, j+neighbour+1) if x != j and 0 < x < len(tasks)])

        CMaxPre = liczCmax(tasks)
        tasks[j], tasks[k] = tasks[k], tasks[j]
        CMaxPost = liczCmax(tasks)

        CMaxDiff = abs(CMaxPre - CMaxPost)

        if CMaxDiff > maxVal:
            maxVal = CMaxDiff
        elif 1 < CMaxDiff < minVal:
            minVal = CMaxDiff

    gongaga = int(math.log(maxVal) * math.floor(math.sqrt(maxVal)))
    gaga = int(gongaga // 2 * math.log(minVal) + minVal)

    return [gongaga, gaga]


if __name__ == '__main__':
    dataPath: str = "./data/data."

    for i in range(1, 4+1):
        rpqTab = list()

        with open(dataPath + str(i) + ".txt", 'r') as f:
            print(f"\nReading {dataPath + str(i) + '.txt'}")

            for line in f:
                rpqTab.append([int(x) for x in line.strip('\n').split(' ')])
            rpqTab = [entry + [idx+1] for idx, entry in enumerate(rpqTab)]

            T, epochs = tuning(rpqTab)
            print(f"T: {T}, epochs: {epochs}")
            print("Cmax: ", symulowaneWyrzazanie(rpqTab, T, 0, epochs))

# Cmax schrage data1: 13981
# Cmax schrage data2: 21529
# Cmax schrage data3: 31683
# Cmax schrage data4: 34444

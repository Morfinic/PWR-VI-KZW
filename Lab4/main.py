import random
import numpy as np
from numpy import exp
from scipy.special import expit


def liczCmax(procList):
    t: int = 0
    Cmax: int = 0

    for proc in procList:
        t = max(t, proc[0])
        t += proc[1]
        Cmax = max(Cmax, t + proc[2])

    return Cmax


def symulowaneWyrzazanie(tasks, T: int, TEnd: int, epochs: int):
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
                if r >= expit(CMaxDiff/T):
                    pass
                else:
                    tasks[j], tasks[k] = tasks[k], tasks[j]

        T -= 1

    return liczCmax(tasks)


if __name__ == '__main__':
    dataPath: str = "./data/data."

    for i in range(1, 4+1):
        rpqTab = list()

        with open(dataPath + str(i) + ".txt", 'r') as f:
            print(f"\nReading {dataPath + str(i) + '.txt'}")

            for line in f:
                rpqTab.append([int(x) for x in line.strip('\n').split(' ')])

            print("Cmax: ", symulowaneWyrzazanie(rpqTab, 200, 0, 100))

# Cmax schrage data1: 13981
# Cmax schrage data2: 21529
# Cmax schrage data3: 31683
# Cmax schrage data4: 34444

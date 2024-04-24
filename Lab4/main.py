import random
from numpy import exp


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
            j = random.randint(0, len(tasks) - 1)
            tmp = 5
            k = random.choice([x for x in range(j-tmp, j+tmp+1) if x != j and 0 < x < len(tasks)])

            CMaxPre = liczCmax(tasks)
            tasks[j], tasks[k] = tasks[k], tasks[j]
            CMaxPost = liczCmax(tasks)

            if CMaxPre > CMaxPost:
                pass
            else:
                CMaxDiff = abs(CMaxPost / CMaxPre)
                r = random.random()
                tmp1 = exp(CMaxDiff * T)
                if r <= tmp1:
                    pass
                else:
                    tasks[j], tasks[k] = tasks[k], tasks[j]

            T = exp()

    return liczCmax(tasks)


if __name__ == '__main__':
    dataPath: str = "./data/data."

    for i in range(1, 1+1):
        rpqTab = list()

        with open(dataPath + str(i) + ".txt", 'r') as f:
            print(f"\nReading {dataPath + str(i) + '.txt'}")

            for line in f:
                rpqTab.append([int(x) for x in line.strip('\n').split(' ')])

            print(symulowaneWyrzazanie(rpqTab, 200, 0, 100))

# Cmax schrage data1: 13981

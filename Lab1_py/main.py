from sortRPQ import *

dataPath: str = "Dane/subDane/data."

for i in range(1, 4+1):
    rpqTab = list()

    with open(dataPath + str(i) + ".txt", 'r') as f:
        print(f"\nReading {dataPath + str(i) + '.txt'}")

        for line in f:
            rpqTab.append([int(x) for x in line.strip('\n').split(' ')])

    print("sort123:", sort123(rpqTab))
    print("sort123_reversed:", sort123_reversed(rpqTab))
    print("sort123_minP:", sort123_minP(rpqTab))
    print("sort123_maxQ:", sort123_maxQ(rpqTab))

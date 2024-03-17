from sortRPQ import *

# sprawko
# skrót nazwy przedmiotu - KZW Wt 13:15 Lab1
# Do następnych zajęć
# opis problemu

dataPath: str = "Dane/subDane/data."
Cmax: int = 0

for i in range(1, 4+1):
    rpqTab = list()

    with open(dataPath + str(i) + ".txt", 'r') as f:
        print(f"\nReading {dataPath + str(i) + '.txt'}")

        for line in f:
            rpqTab.append([int(x) for x in line.strip('\n').split(' ')])

        for i in range(len(rpqTab)):
            rpqTab[i].append(i+1)

        tmp = schrage(rpqTab)

        # print("sort123:", sort123(rpqTab))
        # print("sort123_reversed:", sort123_reversed(rpqTab))
        # print("sort123_minP:", sort123_minP(rpqTab))
        # print("sort123_maxQ:", sort123_maxQ(rpqTab))
        # print("Schrage:", schrage(rpqTab))
        # print("Schrage Heap:", schrageHeap(rpqTab))

        Cmax += tmp

print("\nCmax: ", Cmax)

from WiTi import *

filePath: str = "./Dane/subDane/data."
out_f = open("dane_out.txt", 'w')

for i in range(10 + 1):
    dane: list[list[int]] = list()

    with open(filePath + str(10 + i) + ".txt", 'r') as f:
        # print(f"Otwarto plik data.{10+i}.txt")

        for line in f:
            dane.append([
                int(x)
                for x in line.strip('\n').split(' ')
            ])

    out_f.write(f"Plik: data.{10+i}.txt\nOpt: {WiTi(dane)}\n\n")

out_f.close()

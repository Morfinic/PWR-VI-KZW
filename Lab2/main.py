from WiTi import *
from timeit import timeit


@timeit
def main():
    filePath: str = "./Dane/subDane/data."

    with open("dane_out.txt", 'w') as outFile:
        for i in range(0 + 1):
            dane: list[list[int]] = list()

            with open(filePath + str(10 + i) + ".txt", 'r') as f:
                # print(f"Otwarto plik data.{10+i}.txt")

                for line in f:
                    dane.append([
                        int(x)
                        for x in line.strip('\n').split(' ')
                    ])

            outFile.write(f"Plik: data.{10+i}.txt\nOpt: {WiTi(dane)}\n\n")


if __name__ == "__main__":
    main()

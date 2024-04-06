from WiTi import *
from timeit import timeit


@timeit
def main():
    filePath: str = "./Dane/subDane/data."

    with open("dane_out.txt", 'w') as outFile:
        for i in range(0, 11):
            dane: list[list[int]] = list()

            with open(filePath + str(10 + i) + ".txt", 'r') as f:
                for line in f:
                    dane.append([
                        int(x)
                        for x in line.strip('\n').split(' ')
                    ])

            opt, order = WiTi(dane[::-1])

            outFile.write(f"Plik: data.{10+i}.txt\n"
                          f"Opt: {opt}\n"
                          f"Order: {order}\n\n")


if __name__ == "__main__":
    main()

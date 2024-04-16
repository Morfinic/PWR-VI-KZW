from process import Process


def main():
    # Otwarcie pliku oraz sczytanie danych
    with open("data/neh.data.txt", 'r') as f:
        tmpList = f.read().split("\n\n")

    # Podział danych na osobne zadania
    procList: list = list()
    for i in range( len(tmpList) // 2):
        dataSplit = tmpList[2 * i].split('\n')
        nehAnswer = tmpList[2 * i + 1].split('\n')

        procList.append(
            Process(
                str(dataSplit[0].strip(':')),
                int(dataSplit[1].split(' ')[0]),
                int(dataSplit[1].split(' ')[1]),
                [task.split(' ') for task in dataSplit[2:]],
                int(nehAnswer[1])
            )
        )

    for process in procList:
        order, CMAX = process.NEH()
        print(
            f"Data: {process.name}\n"
            f"CMAX otrzymany: {CMAX}\n"
            f"CMAX opt: {process.NehAnswerCmax}\n"
            f"{order}"
        )


if __name__ == "__main__":
    main()

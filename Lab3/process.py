import numpy as np
from timeit import timeit

class Process:
    name: str = ""
    numOfTask: int = None
    numOfMachines: int = None
    taskList: list = list()
    NehAnswerCmax: int = None

    def __init__(self, name: str,
                 numOfTask: int,
                 numOfMachines: int,
                 taskList: list,
                 NehAnswerCmax: int):
        self.name = name
        self.numOfTask = numOfTask
        self.numOfMachines = numOfMachines
        self.taskList = [list(task) for task in taskList]
        self.NehAnswerCmax = NehAnswerCmax

        self.taskList = np.array(taskList, dtype=np.int32)

    def printData(self):
        print(f"Data: {self.name}\n"
              f"NumOfTask: {self.numOfTask}, NumOfMachines: {self.numOfMachines}\n"
              f"Tasks: \n{self.taskList}\n"
              f"Optimal Cmax: {self.NehAnswerCmax}\n")

    def _calculateWeight(self):
        CmaxList = [sum(task) for task in self.taskList]
        tmp = []

        for _ in range(self.numOfTask):
            tmpVal = CmaxList.index(max(CmaxList))

            tmp.append(tmpVal)
            CmaxList[tmpVal] = -1

        return np.array(tmp)

    def _licz_czas(self, harmonogram):
        zadania_ilosc = harmonogram.shape[0]
        maszyny_ilosc = harmonogram.shape[1]
        czasy = np.zeros((zadania_ilosc + 1, maszyny_ilosc + 1), dtype=int)

        for i in range(1, zadania_ilosc + 1):
            for j in range(1, maszyny_ilosc + 1):
                czasy[i][j] = max(czasy[i - 1][j], czasy[i][j - 1]) + harmonogram[i - 1][j - 1]

        return czasy[zadania_ilosc][maszyny_ilosc]

    def alg123(self):
        return [self._licz_czas(self.taskList), [x + 1 for x in range(self.numOfTask)]]

    @timeit
    def NEH(self):
        ilosc_zadan = self.numOfTask
        ilosc_maszyn = self.numOfMachines
        szeregowane_zadan = self.taskList

        sorted_idx = self._calculateWeight()

        szeregowane_zadan = szeregowane_zadan[sorted_idx]
        harmonogram = np.empty((0, ilosc_maszyn), dtype=int)
        order = list()

        for i in range(ilosc_zadan):
            czas = float('inf')

            for j in range(len(harmonogram) + 1):
                tmp_harmonogram = np.vstack((harmonogram[:j], szeregowane_zadan[i], harmonogram[j:]))
                c_max = self._licz_czas(tmp_harmonogram)

                if c_max < czas:
                    czas = c_max
                    indeks = j

            harmonogram = np.vstack((harmonogram[:indeks], szeregowane_zadan[i], harmonogram[indeks:]))
            order.insert(indeks, sorted_idx[i] + 1)

        return [self._licz_czas(harmonogram), order]

    def goIn(self, harmonogram):
        zadania_ilosc = harmonogram.shape[0]
        maszyny_ilosc = self.numOfMachines
        czasy = harmonogram
        czasy = np.pad(czasy, 1, mode="constant", constant_values=0)

        for i in range(zadania_ilosc + 1):
            for j in range(maszyny_ilosc + 1):
                czasy[i][j] = max(
                    czasy[i][j] + czasy[i - 1][j],
                    czasy[i][j] + czasy[i][j - 1]
                )
        return czasy[1:-1, 1:-1]

    def goOut(self, harmonogram):
        zadania_ilosc = harmonogram.shape[0]
        maszyny_ilosc = self.numOfMachines
        czasy = harmonogram
        czasy = np.pad(czasy, 1, mode="constant", constant_values=0)

        for i in range(0, zadania_ilosc):
            for j in range(0, maszyny_ilosc):
                czasy[zadania_ilosc - i][maszyny_ilosc - j] = (
                    max(
                        czasy[zadania_ilosc - i][maszyny_ilosc - j]
                        + czasy[zadania_ilosc - i][maszyny_ilosc - j + 1],
                        czasy[zadania_ilosc - i][maszyny_ilosc - j]
                        + czasy[zadania_ilosc - i + 1][maszyny_ilosc - j]
                    )
                )
        return czasy[1:-1, 1:-1]

    def timeSplit(self, harmonogram, indeks):
        ilosc_maszyn = self.numOfMachines
        harmonogram = np.vstack((harmonogram, np.zeros((1, ilosc_maszyn), dtype=np.int32)))

        harmonogram[indeks][0] = harmonogram[indeks][0] + harmonogram[indeks - 1][0]

        for i in range(1, ilosc_maszyn):
            harmonogram[indeks][i] = max(
                harmonogram[indeks - 1][i],
                harmonogram[indeks][i - 1]) + harmonogram[indeks][i]

        for i in range(ilosc_maszyn):
            harmonogram[indeks][i] = harmonogram[indeks][i] + harmonogram[indeks + 1][i]

        return max(harmonogram[indeks])

    @timeit
    def QNEH(self):
        ilosc_zadan = self.numOfTask
        ilosc_maszyn = self.numOfMachines
        szeregowane_zadan = self.taskList

        sorted_idx = self._calculateWeight()
        szeregowane_zadan = szeregowane_zadan[sorted_idx]
        harmonogram = np.zeros((1, ilosc_maszyn), dtype=int)
        order = list()
        tmp_wychodzace = np.zeros((1, self.numOfMachines), dtype=int)
        tmp_dochodzace = np.zeros((1, self.numOfMachines), dtype=int)

        for i in range(ilosc_zadan):
            # tmp_harmonogram = np.vstack((harmonogram, szeregowane_zadan[i]))
            # tmp_wychodzace = self.goOut(harmonogram)
            # tmp_dochodzace = self.goIn(harmonogram)

            czas = float('inf')
            indeks = 0

            for j in range(len(harmonogram)+1):
                tmp_harmonogram = np.vstack((tmp_dochodzace[:j], szeregowane_zadan[i], tmp_wychodzace[j:]))
                c_max = self.timeSplit(tmp_harmonogram, j)

                if c_max < czas:
                    czas = c_max
                    indeks = j

            if i == 0:
                harmonogram[0] = szeregowane_zadan[i]
            else:
                harmonogram = np.vstack((harmonogram[:indeks], szeregowane_zadan[i], harmonogram[indeks:]))

            tmp_wychodzace = self.goOut(harmonogram)
            tmp_dochodzace = self.goIn(harmonogram)

            order.insert(indeks, sorted_idx[i] + 1)

        return [self._licz_czas(self.taskList[[x - 1 for x in order]]), order]

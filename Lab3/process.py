import numpy as np


class Process:
    _name: str = ""
    _numOfTask: int = None
    _numOfMachines: int = None
    _taskList: list = list()
    _NehAnswerCmax: int = None

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
        # CmaxList = [[sum(task)] for task in self.taskList]
        # return CmaxList.index(max(CmaxList))

        return np.argsort(
            np.sum(
                self.taskList,
                axis=1
            ),
        )[::-1]

    def _licz_czas(self, harmonogram):
        harmonogram = np.array(harmonogram)
        zadania_ilosc = harmonogram.shape[0]
        maszyny_ilosc = harmonogram.shape[1]
        czasy = np.zeros((zadania_ilosc + 1, maszyny_ilosc + 1), dtype=int)

        for i in range(1, zadania_ilosc + 1):
            for j in range(1, maszyny_ilosc + 1):
                czasy[i][j] = max(czasy[i - 1][j], czasy[i][j - 1]) + harmonogram[i - 1][j - 1]

        return czasy[zadania_ilosc][maszyny_ilosc]

    def NEH(self):
        ilosc_zadan = self.numOfTask
        ilosc_maszyn = self.numOfMachines
        szeregowane_zadan = self.taskList

        sorted_idx = self._calculateWeight()

        szeregowane_zadan = szeregowane_zadan[sorted_idx]
        harmonogram = np.empty((0, ilosc_maszyn), dtype=int)

        for i in range(ilosc_zadan):
            czas = float('inf')
            for j in range(len(harmonogram) + 1):
                tmp_harmonogram = np.vstack((harmonogram[:j], szeregowane_zadan[i], harmonogram[j:]))
                c_max = self._licz_czas(tmp_harmonogram)
                if c_max < czas:
                    czas = c_max
                    indeks = j
            harmonogram = np.vstack((harmonogram[:indeks], szeregowane_zadan[i], harmonogram[indeks:]))

        return harmonogram, self._licz_czas(harmonogram)

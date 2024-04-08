import numpy as np
from timeit import default_timer as timer
from datetime import timedelta

tablica = np.genfromtxt("dane.txt", skip_header=1)


def dochodzaca(harmonogram):
    harmonogram = np.array(harmonogram)
    zadania_ilosc = harmonogram.shape[0]
    maszyny_ilosc = harmonogram.shape[1]
    czasy = np.zeros((zadania_ilosc + 1, maszyny_ilosc + 1), dtype=int)
    for i in range(1, zadania_ilosc + 1):
        for j in range(1, maszyny_ilosc + 1):
            czasy[i][j] = max(czasy[i - 1][j], czasy[i][j - 1]) + harmonogram[i - 1][j - 1]
    czasy = czasy[1:, 1:]
    return czasy


def wychodzaca(harmonogram):
    harmonogram = np.array(harmonogram)
    zadania_ilosc = harmonogram.shape[0]
    maszyny_ilosc = harmonogram.shape[1]
    czasy = np.zeros((zadania_ilosc + 1, maszyny_ilosc + 1), dtype=int)
    for i in range(1, zadania_ilosc + 1):
        for j in range(1, maszyny_ilosc + 1):
            czasy[zadania_ilosc - i][maszyny_ilosc - j] = max(czasy[zadania_ilosc + 1 - i][maszyny_ilosc - j],
                                                              czasy[zadania_ilosc - i][maszyny_ilosc + 1 - j]) + \
                                                          harmonogram[zadania_ilosc - i][maszyny_ilosc - j]
    czasy = czasy[:zadania_ilosc, :maszyny_ilosc]
    return czasy


def czas_ciecie(harmonogram, indeks):
    ilosc_maszyn = harmonogram.shape[1]
    harmonogram[indeks][0] = harmonogram[indeks][0] + harmonogram[indeks - 1][0]
    for i in range(1, ilosc_maszyn):
        harmonogram[indeks][i] = max(harmonogram[indeks - 1][i], harmonogram[indeks][i - 1]) + harmonogram[indeks][i]
    c_max = 0
    for i in range(0, ilosc_maszyn):
        tmp_cmax = harmonogram[indeks][i] + harmonogram[indeks + 1][i]
        harmonogram[indeks][i] = harmonogram[indeks][i] + harmonogram[indeks + 1][i]
        if tmp_cmax > c_max:
            c_max = tmp_cmax
    return c_max


def NEH(zadania):
    poczatek = timer()
    ilosc_zadan = zadania.shape[0]
    ilosc_maszyn = zadania.shape[1]
    szeregowane_zadan = zadania
    row_sums = np.sum(szeregowane_zadan, axis=1)
    sorted_ind = np.argsort(row_sums)[::-1]
    szeregowane_zadan = szeregowane_zadan[sorted_ind]
    harmonogram = np.empty((0, ilosc_maszyn), dtype=int)
    for i in range(ilosc_zadan):
        czas = float('inf')
        for j in range(len(harmonogram) + 1):
            tmp_harmonogram = np.vstack((harmonogram[:j], szeregowane_zadan[i], harmonogram[j:]))
            c_max = licz_czas(tmp_harmonogram)
            if c_max < czas:
                czas = c_max
                indeks = j
        harmonogram = np.vstack((harmonogram[:indeks], szeregowane_zadan[i], harmonogram[indeks:]))

    koniec = timer()
    print("Ile czasu zajelo: " + str(timedelta(seconds=koniec - poczatek)))
    return harmonogram


def licz_czas(harmonogram):
    harmonogram = np.array(harmonogram)
    zadania_ilosc = harmonogram.shape[0]
    maszyny_ilosc = harmonogram.shape[1]
    czasy = np.zeros((zadania_ilosc + 1, maszyny_ilosc + 1), dtype=int)
    for i in range(1, zadania_ilosc + 1):
        for j in range(1, maszyny_ilosc + 1):
            czasy[i][j] = max(czasy[i - 1][j], czasy[i][j - 1]) + harmonogram[i - 1][j - 1]
    return czasy[zadania_ilosc][maszyny_ilosc]


harmonogram_NEH = NEH(tablica)
# print(harmonogram_NEH)
print(licz_czas(harmonogram_NEH))

print(czas)

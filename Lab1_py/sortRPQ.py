import numpy as np
import heapq


def sort123(procList: list):
    t: int = 0
    Cmax: int = 0

    for proc in procList:
        t = max(t, proc[0])
        t += proc[1]
        Cmax = max(Cmax, t + proc[2])

    return Cmax


def sort123_reversed(procList: list):
    return sort123(list(reversed(procList)))


def sort123_minP(procList: list):
    return sort123(list(sorted(procList, key=lambda x: x[0])))


def sort123_maxQ(procList: list):
    return sort123(list(sorted(procList, key=lambda x: x[2], reverse=True)))


def schrage(procList: list):
    schrageUnsorted = procList
    schrageUnsorted = np.array(schrageUnsorted, dtype=np.int_)
    schrageReady = np.empty((0, 4), int)

    t: int = 0
    Cmax: int = 0
    order: str = str()

    while len(schrageReady) != 0 or len(schrageUnsorted) != 0:
        while len(schrageUnsorted) and min(schrageUnsorted[:, 0]) <= t:
            i = np.argmin(schrageUnsorted[:, 0])
            schrageReady = np.append(schrageReady, np.array([schrageUnsorted[i]]), axis=0)
            schrageUnsorted = np.delete(schrageUnsorted, i, axis=0)

        if len(schrageReady) == 0:
            t = min(schrageUnsorted[:, 0])
        else:
            i = np.argmax(schrageReady[:, 2])
            j = schrageReady[i]
            schrageReady = np.delete(schrageReady, i, axis=0)
            t += j[1]
            Cmax = max(Cmax, t + j[2])
            order += str(j[3]) + ' '

    print("Cmax:", Cmax)
    print(order)
    return Cmax

def swap_lista(lista, poz1, poz2):
    lista[poz1], lista[poz2] = lista[poz2], lista[poz1]
    return lista


def inwersja_wartosci(lista):
    lista[0], lista[1], lista[2] = lista[0] * (-1), lista[1] * (-1), lista[2] * (-1)
    return lista


def schrageHeap(tab):
    tab = [list(map(int, i)) for i in tab]

    heap_nieuszeregowane = tab
    heapq.heapify(heap_nieuszeregowane)

    heap_gotowe = list()
    heapq.heapify(heap_gotowe)

    t: int = 0
    Cmax: int = 0

    while len(heap_nieuszeregowane) != 0 or len(heap_gotowe) != 0:
        while (True):
            if len(heap_nieuszeregowane) != 0:
                if heap_nieuszeregowane[0][0] <= t:
                    temp = heap_nieuszeregowane[0]
                    swap_lista(temp, 0, 2)
                    inwersja_wartosci(temp)
                    heapq.heappush(heap_gotowe, temp)
                    heapq.heappop(heap_nieuszeregowane)
                    continue
            break
        if len(heap_gotowe) == 0:
            temp = heapq.nsmallest(1, heap_nieuszeregowane)
            t = temp[0][0]
        else:
            j = heap_gotowe[0]
            heapq.heappop(heap_gotowe)
            t += (j[1] * (-1))
            Cmax = max(Cmax, t + (j[0] * (-1)))

    return Cmax

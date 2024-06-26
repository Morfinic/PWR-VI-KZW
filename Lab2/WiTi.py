import math
from timeit import timeit


@timeit
def WiTi(task):
    n = len(task)
    N: int = 1 << n
    F: list = [math.inf] * N
    F[0] = 0
    order = [[] for _ in range(N)]

    for procOrder in range(1, N):
        b = ('0' * (n - len(bin(procOrder)[2:])) + bin(procOrder)[2:])[::-1]
        C: int = sum(elem[0] for elem in [task[i] for i in range(n) if b[i] == '1'])

        for idx, bit in enumerate(b):
            if int(bit):
                koszt = F[procOrder - 2 ** idx] + task[idx][1] * max(C - task[idx][2], 0)
                if F[procOrder] > koszt:
                    F[procOrder] = koszt
                    order[procOrder] = order[procOrder - 2 ** idx] + [idx]

    order = [n - x for x in order[-1]]

    return F[N - 1], order

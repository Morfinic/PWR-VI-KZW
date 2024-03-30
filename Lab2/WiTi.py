import math
from timeit import timeit


@timeit
def WiTi(task):
    n = len(task); N: int = 1 << n; F: list = [math.inf] * N; F[0] = 0

    for procOrder in range(1, N):
        b = ('0' * (n - len(bin(procOrder)[2:])) + bin(procOrder)[2:])[::-1]
        C: int = sum(elem[0] for elem in [task[i] for i in range(n) if b[i] == '1'])

        for idx, bit in enumerate(b):
            if int(bit):
                F[procOrder] = min(F[procOrder], F[procOrder - 2 ** idx] + task[idx][1] * max(C - task[idx][2], 0))

    b = ['1'] * n
    order = [[-1, -1]] * n
    autism = [-1] * n
    for idx in range(n):
        for i in range(n, 0, -1):
            if b[n - i] == '0':
                continue
            tmp_b = b.copy()
            tmp_b[n - i] = '0'
            kara = F[int(''.join(tmp_b), 2)]
            if kara > order[idx][1] and i not in autism:
                order[idx] = [i, kara]
                autism[idx] = i
        b[n - autism[idx]] = '0'

    print("Order:", autism[::-1])
    return F[N - 1]

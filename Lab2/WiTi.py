def WiTi(task):
    n = len(task)
    N: int = 1 << n
    F: list = [None] * N
    F[0] = 0

    for procOrder in range(1, N):
        c: int = 0
        b: int = 1
        for i in range(n):
            if procOrder & b:
                c += task[i][0]
            b *= 2

        F[procOrder] = 999999
        b = 1
        for i in range(n):
            if procOrder & b:
                F[procOrder] = min(F[procOrder],
                                   F[procOrder - b] + task[i][1] * max(c - task[i][2], 0)
                                   )
            b *= 2

    return F[N - 1]

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

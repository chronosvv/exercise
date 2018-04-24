def func(N, Ws, Qs):
    dat = [[-1 for i in range(N+1) for j in range(N+1)]]
    for W in Ws:
        start = W[0]
        end = W[1]
        weight = W[2]
        dat[start][end] = weight
        sec = start - 1
        for j in range(sec-1, 0, -1):
            if dat[sec][j] > weight:
                dat[start][j] = dat[sec][j]
            else:
                dat[start][j] = weight

    rtn = []
    for Q in Qs:
        start = Q[0]
        end = Q[1]
        if end > start:
            start, end = end, start
        rtn += [dat[start][end]]
        return rtn

def func2(N, Ws, Qs):
    dat = [[-1 for i in range(N+1) for j in range(N+1)]]
    for W in Ws:
        start = W[0]
        end = W[1]
        weight = W[2]
        dat[start][end] = weight
        sec = start - 1
        for j in range(sec-1, 0, -1):
            if dat[sec][j] > weight:
                dat[start][j] = dat[sec][j]
            else:
                dat[start][j] = weight

    rtn = []
    for Q in Qs:
        start = Q[0]
        end = Q[1]
        if end > start:
            start, end = end, start
        rtn += [dat[start][end]]
    return rtn

Ws = [[2, 1, 3],
      [3, 2, 2],
      [4, 3, 5],
      [5, 4, 1]]
Qs = [[2, 1],
      [3, 1],
      [3, 5],
      [1, 2],
      [4, 2]]
rtn1 = func(5, Ws, Qs)
print(rtn1)
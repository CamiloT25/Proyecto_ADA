def q(i, j):
    if j == 0:
        return 1
    if i == 0 and j > 0:
        return 0
    if j < 0:
        return 0
    if i > j:
        return q(j, j)
    if i == 1 or j == 1:
        return 1
    return q(i - 1, j) + q(i, j - i)

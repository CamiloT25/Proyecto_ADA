def q_R(i, j):
    if j == 0:
        return 1
    if i == 0 and j > 0:
        return 0
    if j < 0:
        return 0
    if i > j:
        return q_R(j, j)
    if i == 1 or j == 1:
        return 1
    return q_R(i - 1, j) + q_R(i, j - i)

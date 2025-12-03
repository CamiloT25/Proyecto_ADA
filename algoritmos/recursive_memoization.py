def q(i, j, m=None):  # m : meorizacion
    if m is None:
        m = {}

    if (i, j) in m:
        return m[(i, j)]

    if j == 0:
        return 1
    if j < 0:
        return 0
    if i == 0 and j > 0:
        return 0
    if i > j:
        m[(i, j)] = q(j, j, m)
        return m[(i, j)]
    if i == 1 or j == 1:
        return 1

    result = q(i - 1, j, m) + q(i, j - i, m)
    m[(i, j)] = result
    return result

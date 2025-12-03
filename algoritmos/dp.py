def q_iterativo(i, j):
    dp = [[0] * (j + 1) for _ in range(i + 1)]

    # caso base: solo hay una forma de formar 0 (la suma vacía)
    for x in range(i + 1):
        dp[x][0] = 1

    for a in range(1, i + 1):
        for b in range(1, j + 1):
            if a > b:
                dp[a][b] = dp[b][b]
            else:
                dp[a][b] = dp[a - 1][b] + dp[a][b - a]

    return dp[i][j]
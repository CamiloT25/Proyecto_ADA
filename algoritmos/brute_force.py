def partitions_count_exhaustive(n, max_part=None):
    if max_part is None:
        max_part = n
    if n == 0:
        return 1

    total = 0
    for k in range(min(n, max_part), 0, -1):
        total += partitions_count_exhaustive(n-k, k)
    return total


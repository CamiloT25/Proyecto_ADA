def partitions_count_exhaustive(n, max_part=None):
    # manejar negativos sin excepción
    if n < 0:
        return 0

    if max_part is None:
        max_part = n

    # también manejar max_part negativo o cero
    if max_part <= 0:
        return 0

    if n == 0:
        return 1

    total = 0
    for k in range(min(n, max_part), 0, -1):
        total += partitions_count_exhaustive(n - k, k)

    return total

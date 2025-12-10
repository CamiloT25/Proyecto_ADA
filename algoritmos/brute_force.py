def partitions_count_exhaustive(n, max_part=None):
    # Caso base primero SIEMPRE
    if n == 0:
        return 1

    # Manejo de negativos
    if n < 0:
        return 0

    # Configurar límite por defecto
    if max_part is None:
        max_part = n-1

    # max_part inválido = 0 particiones
    if max_part <= 0:
        return 0

    total = 0
    for k in range(min(n, max_part), 0, -1):
        total += partitions_count_exhaustive(n - k, k)

    return total

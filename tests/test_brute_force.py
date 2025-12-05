import pytest
from algoritmos.brute_force import partitions_count_exhaustive

# -------------------------
# 1. CASOS BASE
# -------------------------

def test_caso_base_cero():
    assert partitions_count_exhaustive(0) == 1


def test_caso_base_uno():
    assert partitions_count_exhaustive(1) == 1


def test_valor_negativo():
    assert partitions_count_exhaustive(-7) == 0


# -------------------------
# 2. VALORES CLÁSICOS DE p(n)
# -------------------------

def test_particion_2():
    assert partitions_count_exhaustive(2) == 2


def test_particion_3():
    assert partitions_count_exhaustive(3) == 3


def test_particion_4():
    assert partitions_count_exhaustive(4) == 5


def test_particion_5():
    assert partitions_count_exhaustive(5) == 7


def test_particion_6():
    assert partitions_count_exhaustive(6) == 11


def test_particion_7():
    assert partitions_count_exhaustive(7) == 15


# -------------------------
# 3. COMPORTAMIENTO DE max_part
# -------------------------

def test_max_parte_cero():
    assert partitions_count_exhaustive(5, max_part=0) == 0


def test_max_parte_negativa():
    assert partitions_count_exhaustive(5, max_part=-10) == 0


def test_max_parte_menor_que_n():
    # Resultado conocido: 7 particiones de 6 con partes ≤ 3
    assert partitions_count_exhaustive(6, max_part=3) == 7


def test_max_parte_grande_equivale_a_ilimitado():
    assert partitions_count_exhaustive(8, max_part=100) == partitions_count_exhaustive(8)


# -------------------------
# 4. MONOTONÍA
# -------------------------

def test_monotonia_en_n():
    assert partitions_count_exhaustive(4) < partitions_count_exhaustive(5)
    assert partitions_count_exhaustive(5) < partitions_count_exhaustive(6)
    assert partitions_count_exhaustive(6) < partitions_count_exhaustive(7)


# -------------------------
# 5. CONSISTENCIA INTERNA DEL ALGORITMO
# -------------------------

def test_consistencia_recursiva():
    total = 0
    for k in range(1, 7):
        total += partitions_count_exhaustive(6 - k, k)

    assert total == partitions_count_exhaustive(6)


# -------------------------
# 6. LIMITAR max_part DISMINUYE O IGUALA EL RESULTADO
# -------------------------

def test_limitar_nunca_aumenta():
    assert partitions_count_exhaustive(10, max_part=3) <= partitions_count_exhaustive(10)


# -------------------------
# 7. CASOS MAYORES
# -------------------------

def test_particion_10():
    assert partitions_count_exhaustive(10) == 42







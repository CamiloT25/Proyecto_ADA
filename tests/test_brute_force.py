import pytest
from algoritmos.brute_force import partitions_count_exhaustive



def test_casos_base():
    # Caso base donde n = 0 → solo existe una partición posible: la partición vacía.
    assert partitions_count_exhaustive(0) == 1

    # n = 1 → solo una partición posible (1).
    assert partitions_count_exhaustive(1) == 1


def test_valores_pequenos():
    # Verifica los valores clásicos conocidos de la función de particiones.
    # p(2) = 2  → {2}, {1+1}
    assert partitions_count_exhaustive(2) == 2

    # p(3) = 3 → {3}, {2+1}, {1+1+1}
    assert partitions_count_exhaustive(3) == 3

    # p(4) = 5
    assert partitions_count_exhaustive(4) == 5

    # p(5) = 7
    assert partitions_count_exhaustive(5) == 7


def test_valores_medianos():
    # Valores conocidos de la función de particiones.
    assert partitions_count_exhaustive(6) == 11
    assert partitions_count_exhaustive(7) == 15
    assert partitions_count_exhaustive(8) == 22
    assert partitions_count_exhaustive(9) == 30
    assert partitions_count_exhaustive(10) == 42


def test_limite_max_part():
    # Probamos que la restricción max_part funcione correctamente.
    # Particiones de 5 usando solo partes ≤ 2:
    # 2+2+1, 2+1+1+1, 1+1+1+1+1 → total = 3
    assert partitions_count_exhaustive(5, max_part=2) == 3

    # Particiones de 6 usando solo partes ≤ 3.
    # Se sabe que deben ser 7.
    assert partitions_count_exhaustive(6, max_part=3) == 7


def test_max_part_igual_n():
    # Si max_part = n, el resultado debe ser el mismo que sin especificarlo.
    assert partitions_count_exhaustive(8, max_part=8) == partitions_count_exhaustive(8)


def test_entradas_invalidas_silenciosas():
    # Si n es negativo → no hay particiones posibles.
    assert partitions_count_exhaustive(-5) == 0

    # Si max_part es 0 o negativo → no hay particiones.
    assert partitions_count_exhaustive(5, max_part=0) == 0
    assert partitions_count_exhaustive(5, max_part=-4) == 0






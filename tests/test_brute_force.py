import pytest
from algoritmos.brute_force import partitions_count_exhaustive




def test_base_cases():
    # particiones de 0 → 1
    assert partitions_count_exhaustive(0) == 1
    
    # particiones de 1 → 1
    assert partitions_count_exhaustive(1) == 1

def test_small_numbers():
    # Valores conocidos de particiones
    # p(2) = 2 -> {2}, {1+1}
    assert partitions_count_exhaustive(2) == 2

    # p(3) = 3 -> {3}, {2+1}, {1+1+1}
    assert partitions_count_exhaustive(3) == 3

    # p(4) = 5 -> {4}, {3+1}, {2+2}, {2+1+1}, {1+1+1+1}
    assert partitions_count_exhaustive(4) == 5

    # p(5) = 7
    assert partitions_count_exhaustive(5) == 7

def test_medium_numbers():
    # valores de particiones conocidos
    assert partitions_count_exhaustive(6) == 11
    assert partitions_count_exhaustive(7) == 15
    assert partitions_count_exhaustive(8) == 22
    assert partitions_count_exhaustive(9) == 30
    assert partitions_count_exhaustive(10) == 42

def test_max_part_restriction():
    # Solo se pueden usar partes de tamaño máximo 2
    # particiones de 5 usando solo 1 y 2
    # válidas: 2+2+1, 2+1+1+1, 1+1+1+1+1 → total = 3
    assert partitions_count_exhaustive(5, max_part=2) == 3

    # particiones de 6 con partes ≤ 3
    # válidas: 
    # 3+3
    # 3+2+1
    # 3+1+1+1
    # 2+2+2
    # 2+2+1+1
    # 2+1+1+1+1
    # 1+1+1+1+1+1  → total = 7
    assert partitions_count_exhaustive(6, max_part=3) == 7

def test_sequential_max_parts():
    # probar que max_part funciona igual que el comportamiento natural
    # max_part = n debe ser igual al resultado normal
    assert partitions_count_exhaustive(8, max_part=8) == partitions_count_exhaustive(8)

def test_invalid_inputs():
    with pytest.raises(TypeError):
        partitions_count_exhaustive("10")
    with pytest.raises(ValueError):
        partitions_count_exhaustive(-5)





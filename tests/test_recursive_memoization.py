import pytest
from algoritmos.recursive_memoization import q
def test_caso_base_j_cero():
    # Solo hay una forma de sumar 0: la partición vacía
    assert q(0, 0) == 1
    assert q(1, 0) == 1
    assert q(5, 0) == 1


def test_j_negativo():
    # No existen particiones con total negativo
    assert q(5, -1) == 0
    assert q(3, -10) == 0


def test_i_cero_j_positivo():
    # Si no se permiten sumandos (i=0), no puedo formar un número positivo
    assert q(0, 1) == 0
    assert q(0, 5) == 0


def test_casos_unos():
    # Si solo puedo usar el número 1 entonces solo existe una partición
    assert q(1, 1) == 1
    assert q(1, 5) == 1
    # Si busco particiones de 1 entonces siempre es 1 sin importar i>=1
    assert q(10, 1) == 1

def test_i_mayor_j():
    # si i > j entonces no tiene sentido usar <= a i por lo tanto (j,j)
    assert q(7, 3) == q(3, 3)
    assert q(10, 2) == q(2, 2)
    assert q(10, 6) == q(6, 6)

def test_ejemplos():
    assert q(2, 5) == 3
    assert q(1, 5) == 1
    assert q(4, 5) == 6


def test_valores_pequenos_comprobados():

    assert q(2, 3) == 2
    assert q(3, 3) == 3
    assert q(3, 4) == 4
    assert q(4, 4) == 5
    assert q(3, 5) == 5

def test_uso_memo_externo():
    memo = {}
    r1 = q(4, 7, memo)
    r2 = q(4, 7, memo)

    # Los valores deben coincidir
    assert r1 == r2
    # Y debe haberse guardado en memo
    assert (4, 7) in memo

import pytest
from algoritmos.recursive import q_R

# Verifica el caso base: cuando j == 0 siempre hay 1 partición (la vacía).
def test_caso_base_j_cero():
    assert q_R(5, 0) == 1
    assert q_R(100, 0) == 1


# Verifica que cuando i == 0 y j > 0 no se puede formar j.
def test_caso_base_i_cero():
    assert q_R(0, 1) == 0
    assert q_R(0, 10) == 0


# No se pueden particionar numeros negativos
def test_j_negativo():
    assert q_R(5, -1) == 0
    assert q_R(10, -20) == 0


# No tiene sentido describir j con numero mayores a el mismo
def test_propiedad_i_mayor_que_j():
    assert q_R(7, 3) == q_R(3, 3)
    assert q_R(10, 2) == q_R(2, 2)
    assert q_R(10, 6) == q_R(6, 6)


# Cuando i o j son iguales a 1, en particular solo hay una forma de particionarlo
#les llamamos casos optimizadores
def test_casos_unos():
    assert q_R(1, 10) == 1
    assert q_R(10, 1) == 1
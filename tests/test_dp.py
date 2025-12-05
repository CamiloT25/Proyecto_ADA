from algoritmos.dp import q_iterativo
# -------------------------
# 1. CASOS BASE
# -------------------------

def test_caso_base_suma_cero():
    # Solo hay una forma de formar 0
    assert q_iterativo(5, 0) == 1
    assert q_iterativo(0, 0) == 1
    assert q_iterativo(10, 0) == 1


def test_caso_base_i_cero():
    # Si i = 0, j > 0 → no se puede formar j con nada
    assert q_iterativo(0, 5) == 0
    assert q_iterativo(0, 3) == 0


# -------------------------
# 2. PRUEBAS DE CORRECTITUD CONOCIDAS
#    (q_iterativo debe coincidir con p(j) cuando i >= j)
# -------------------------

def test_valor_conocido_1():
    assert q_iterativo(1, 1) == 1  # 1


def test_valor_conocido_2():
    assert q_iterativo(2, 2) == 2  # 2, 1+1


def test_valor_conocido_3():
    assert q_iterativo(3, 3) == 3  # 3, 2+1, 1+1+1


def test_valor_conocido_4():
    assert q_iterativo(4, 4) == 5


def test_valor_conocido_5():
    assert q_iterativo(5, 5) == 7


def test_valor_conocido_6():
    assert q_iterativo(6, 6) == 11


# -------------------------
# 3. CASOS DONDE i < j
# -------------------------

def test_i_menor_que_j_1():
    # formar 5 usando partes ≤ 3
    # particiones: 3+2, 3+1+1, 2+2+1, 2+1+1+1, 1+1+1+1+1 = 5
    assert q_iterativo(3, 5) == 5


def test_i_menor_que_j_2():
    # formar 6 con partes ≤ 3:
    # 3+3
    # 3+2+1
    # 3+1+1+1
    # 2+2+2
    # 2+2+1+1
    # 2+1+1+1+1
    # 1+1+1+1+1+1
    # total = 7
    assert q_iterativo(3, 6) == 7


# -------------------------
# 4. MONOTONÍA RESPECTO A j
# -------------------------

def test_monotonia_en_j():
    assert q_iterativo(10, 4) < q_iterativo(10, 5)
    assert q_iterativo(10, 5) < q_iterativo(10, 6)


# -------------------------
# 5. CONSISTENCIA RESPECTO A i >= j
# -------------------------

def test_equivalencia_con_particiones_completas():
    # Cuando i >= j, q_iterativo(i, j) = número total de particiones de j
    # Valores conocidos:  p(7) = 15, p(8) = 22, p(9) = 30
    assert q_iterativo(20, 7) == 15
    assert q_iterativo(20, 8) == 22
    assert q_iterativo(20, 9) == 30


# -------------------------
# 6. PRUEBAS DE CASO MAYOR (SANITY CHECK)
# -------------------------

def test_valor_conocido_10():
    # El número de particiones de 10 es 42
    assert q_iterativo(20, 10) == 42

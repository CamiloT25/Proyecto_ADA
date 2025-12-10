import os
import time
from experimento.timer import Timer

from algoritmos.brute_force import partitions_count_exhaustive
from algoritmos.recursive import q_R
from algoritmos.recursive_memoization import q
from algoritmos.dp import q_iterativo


def probar_limite(funcion, nombre, n_inicial=5, paso=1, umbral_segundos=1.0, n_maximo=5000):
    """
    Explora cuál es el mayor n que 'funcion' soporta sin:
      - tardar más de 'umbral_segundos'
      - lanzar RecursionError

    Devuelve un diccionario con el resultado.
    """

    n = n_inicial
    ultimo_ok = None
    motivo_parada = None
    tiempo_ultimo = None

    while n <= n_maximo:
        try:
            with Timer() as t:
                # Usamos la misma convención que en el experimento principal: p(n) = q(n-1, n)
                funcion(n - 1, n)
            tiempo = t.elapsed
        except RecursionError:
            motivo_parada = "RecursionError"
            break

        # Si llegamos aquí, no hubo error
        ultimo_ok = n
        tiempo_ultimo = tiempo

        if tiempo > umbral_segundos:
            motivo_parada = f"> {umbral_segundos}s"
            break

        n += paso

    # Si nunca rompió por tiempo ni por recursión y se llegó a n_maximo
    if motivo_parada is None:
        motivo_parada = f"llegó a n_maximo={n_maximo}"

    return {
        "algoritmo": nombre,
        "n_max_sin_fallar": ultimo_ok,
        "tiempo_en_n_max": tiempo_ultimo,
        "motivo_parada": motivo_parada,
    }


def run_limites():
    """
    Explora hasta dónde aguanta cada algoritmo antes de explotar en tiempo
    o RecursionError.
    """

    algoritmos = {
        "bruteforce": partitions_count_exhaustive,
        "recursivo": q_R,
        "memo": q,
        "dp": q_iterativo,
    }

    # Parámetros del experimento de límites
    n_inicial = 5
    paso = 1
    umbral_segundos = 1.0
    n_maximo = 1000

    resultados = []

    print("EXPERIMENTO DE LÍMITES POR ALGORITMO\n")
    print(f"n_inicial = {n_inicial}, paso = {paso}, umbral = {umbral_segundos}s, n_maximo = {n_maximo}\n")

    for nombre, f in algoritmos.items():
        print(f"Probando límites para: {nombre}...")
        r = probar_limite(
            funcion=f,
            nombre=nombre,
            n_inicial=n_inicial,
            paso=paso,
            umbral_segundos=umbral_segundos,
            n_maximo=n_maximo,
        )
        resultados.append(r)

    # Mostrar tabla resumen
    print("\nRESUMEN DE LÍMITES (por algoritmo):\n")
    print(f"{'Algoritmo':<12} {'n_max_sin_fallar':<16} {'tiempo_en_n_max [s]':<22} {'motivo_parada':<20}")
    print("-" * 80)

    for r in resultados:
        tiempo_txt = f"{r['tiempo_en_n_max']:.6f}" if r["tiempo_en_n_max"] is not None else "None"
        print(
            f"{r['algoritmo']:<12} "
            f"{str(r['n_max_sin_fallar']):<16} "
            f"{tiempo_txt:<22} "
            f"{r['motivo_parada']:<20}"
        )



if __name__ == "__main__":
    run_limites()

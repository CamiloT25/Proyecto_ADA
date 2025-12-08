import os

from experimento.timer import Timer
import pandas as pd

from algoritmos.brute_force import partitions_count_exhaustive
from algoritmos.recursive import q_R
from algoritmos.recursive_memoization import q
from algoritmos.dp import q_iterativo


def medir(funcion, n, repeticiones):
    tiempos = []
    for _ in range(repeticiones):
        with Timer() as t:
            funcion(n - 1, n)
        tiempos.append(t.elapsed)
    return tiempos


def run():
    
    algoritmos = {
        "bruteforce": partitions_count_exhaustive,
        "recursivo": q_R,
        "memo": q,
        "dp": q_iterativo
    }

    tamaños = [10, 20, 30, 40, 50]
    repeticiones = 10

    filas = []

    for nombre, f in algoritmos.items():
        print(f"Ejecutando: {nombre}")
        for n in tamaños:
            try:
                tiempos = medir(f, n, repeticiones)
                filas.append({
                    "algoritmo": nombre,
                    "n": n,
                    "min": min(tiempos),
                    "max": max(tiempos),
                    "promedio": sum(tiempos) / repeticiones
                })
            except RecursionError:
                filas.append({
                    "algoritmo": nombre,
                    "n": n,
                    "error": "RecursionError"
                })

    df = pd.DataFrame(filas)

    # Guardar CSV con ruta absoluta
    ruta_resultados = os.path.join(os.path.dirname(__file__), "datos", "resultados.csv")
    df.to_csv(ruta_resultados, index=False)

    print("Experimento terminado.")


if __name__ == "__main__":
    run()


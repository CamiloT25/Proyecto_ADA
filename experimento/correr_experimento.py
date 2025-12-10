import os
import random

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


def run(max_n=30, num_ns=1000, max_reps=5000):
    
    algoritmos = {
        "bruteforce": partitions_count_exhaustive,
        "recursivo": q_R,
        "memo": q,
        "dp": q_iterativo
    }

    tamaños = [random.randint(10, max_n) for _ in range(num_ns)]
    repeticiones = random.randint(100, max_reps)

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
    
    print("\nRESULTADOS EN TABLA:\n")
    print(f"{'Algoritmo':<12} {'n':<4} {'min':<12} {'max':<12} {'promedio':<12}")
    print("-" * 60)

    for fila in filas:
     if "error" in fila:
        print(f"{fila['algoritmo']:<12} {fila['n']:<4} ERROR")
     else:
        print(f"{fila['algoritmo']:<12} {fila['n']:<4} "
              f"{fila['min']:<12.6g} {fila['max']:<12.6g} {fila['promedio']:<12.6g}")

    print("Experimento terminado.")


if __name__ == "__main__":
    run()


import pandas as pd
import os

def imprimir_tabla_comparativa_desde_csv():
    """
    Lee el archivo resultados.csv, reorganiza los datos y
    muestra una tabla comparativa de promedios por algoritmo y por n.
    """

    ruta_csv = os.path.join(os.path.dirname(__file__), "datos", "resultados.csv")

    if not os.path.exists(ruta_csv):
        print("No se encontró resultados.csv. Ejecuta el experimento primero.")
        return

    df = pd.read_csv(ruta_csv)

    # Filtrar columnas relevantes
    df = df[['algoritmo', 'n', 'promedio']]

    # Crear tabla pivote: filas = n, columnas = algoritmos
    tabla = pd.pivot_table(df, values='promedio', index='n', columns='algoritmo')

    # Ordenar por n
    tabla = tabla.sort_index()

    print("\nTABLA COMPARATIVA (promedios en segundos, leída desde CSV):\n")
    print(f"{'n':<6} {'bruteforce':<12} {'recursivo':<12} {'memo':<12} {'dp':<12}")
    print("-" * 65)

    for n, fila in tabla.iterrows():
        print(f"{n:<6} "
              f"{fila.get('bruteforce', float('nan')):<12.6g} "
              f"{fila.get('recursivo', float('nan')):<12.6g} "
              f"{fila.get('memo', float('nan')):<12.6g} "
              f"{fila.get('dp', float('nan')):<12.6g}")

def imprimir_tabla_relacion_velocidades_desde_csv():
    """
    Imprime una tabla con la relación de velocidad:
    bruteforce/dp, recursivo/dp y memo/dp para cada n.
    """
    ruta_csv = os.path.join(os.path.dirname(__file__), "datos", "resultados.csv")

    if not os.path.exists(ruta_csv):
        print("No se encontró resultados.csv. Ejecuta el experimento primero.")
        return

    df = pd.read_csv(ruta_csv)
    df = df[['algoritmo', 'n', 'promedio']]

    tabla = pd.pivot_table(df, values='promedio', index='n', columns='algoritmo')
    tabla = tabla.sort_index()

    print("\nTABLA RELACIÓN DE VELOCIDADES (tiempo_algoritmo ÷ tiempo_dp):\n")
    print(f"{'n':<6} {'bf ÷ dp':<15} {'rec ÷ dp':<15} {'memo ÷ dp':<15}")
    print("-" * 55)

    for n, fila in tabla.iterrows():
        dp = fila.get('dp')

        if pd.isna(dp) or dp == 0:
            continue

        bf_rel = fila.get('bruteforce', float('nan')) / dp if pd.notna(fila.get('bruteforce')) else float('nan')
        rec_rel = fila.get('recursivo', float('nan')) / dp if pd.notna(fila.get('recursivo')) else float('nan')
        memo_rel = fila.get('memo', float('nan')) / dp if pd.notna(fila.get('memo')) else float('nan')

        print(f"{n:<6} "
              f"{bf_rel:.2f}×".ljust(15) +
              f"{rec_rel:.2f}×".ljust(15) +
              f"{memo_rel:.2f}×".ljust(15))

def imprimir_tabla_estabilidad_desde_csv():
    """
    Imprime una tabla del coeficiente de variación (CV) por algoritmo y por n.
    """
    ruta_csv = os.path.join(os.path.dirname(__file__), "datos", "resultados.csv")

    if not os.path.exists(ruta_csv):
        print("No se encontró resultados.csv. Ejecuta el experimento primero.")
        return

    df = pd.read_csv(ruta_csv)

    if "cv" not in df.columns:
        print("El archivo CSV no contiene coeficiente de variación. Re-ejecuta el experimento.")
        return

    tabla = pd.pivot_table(df, values='cv', index='n', columns='algoritmo')
    tabla = tabla.sort_index()

    print("\nTABLA DE ESTABILIDAD (Coeficiente de Variación - CV):\n")
    print(f"{'n':<6} {'bruteforce':<15} {'recursivo':<15} {'memo':<15} {'dp':<15}")
    print("-" * 70)

    for n, fila in tabla.iterrows():
        print(f"{n:<6} "
              f"{fila.get('bruteforce', float('nan')):<15.4f} "
              f"{fila.get('recursivo', float('nan')):<15.4f} "
              f"{fila.get('memo', float('nan')):<15.4f} "
              f"{fila.get('dp', float('nan')):<15.4f}")

def imprimir_tabla_costo_total_desde_csv():
    """
    Calcula e imprime el costo computacional total de cada algoritmo,
    sumando los tiempos promedio de todas las instancias de n.
    """

    ruta_csv = os.path.join(os.path.dirname(__file__), "datos", "resultados.csv")

    if not os.path.exists(ruta_csv):
        print(" No se encontró resultados.csv. Ejecuta el experimento primero.")
        return

    df = pd.read_csv(ruta_csv)

    if "promedio" not in df.columns:
        print(" No se encuentra la columna 'promedio' en el CSV.")
        return

    # Agrupar por algoritmo y sumar los promedios
    totales = df.groupby("algoritmo")["promedio"].sum().sort_values()

    print("\nCOSTO COMPUTACIONAL TOTAL (suma de tiempos promedio):\n")
    print(f"{'Algoritmo':<15} {'Costo total [s]':<20}")
    print("-" * 35)

    for algoritmo, costo in totales.items():
        print(f"{algoritmo:<15} {costo:<20.6f}")

    print()

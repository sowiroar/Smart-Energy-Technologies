import pandas as pd
import numpy as np

def view(path):
    print(f"Vista del dataset: {path}")
    return pd.read_excel(path)

def recort(path):
    print(f"Funcion de recorte con ruta: {path}")
    # Itera sobre las primeras 11 columnas
    lecturas = pd.read_excel(path)
    print(f"Lecturas cargadas: {lecturas.shape}")
    for idx, col in enumerate(lecturas.columns[:11]):
        # Busca la palabra "NIC" en cada celda de la columna
        if "NIC" in lecturas[col].values:
            # Encuentra la fila y columna
            fila, columna = lecturas[lecturas[col] == "NIC"].index[0], col
            print(f"La palabra 'NIC' se encuentra en la fila {fila} y columna '{columna}' (columna número {idx}).")
            break  # Detén la iteración después de encontrar la primera ocurrencia
    else:
        print("La palabra 'NIC' no se encontró en las primeras 11 columnas.")
        return None  # Si no se encuentra 'NIC', devuelve None

    columnas = list(lecturas.columns)
    lecturas = lecturas[columnas[idx:]]
    lecturas = lecturas.iloc[fila:].reset_index(drop=True)  # Asegura que el índice esté correcto después del recorte
    lecturas=lecturas.rename(columns={f'{columna}': 'NIC'})
    lecturas.columns = lecturas.iloc[0]
    lecturas = lecturas.drop(index=0)
    lecturas = lecturas.loc[:, ~lecturas.columns.isna()]
    lecturas= lecturas.drop(columns=["Id Canal Equipo"])
    lecturas=lecturas.reset_index(drop=True)
    lecturas['NIC'] = lecturas['NIC'].fillna(method='pad')
    deleted=list(lecturas[lecturas['NIC'].isin(["0"])].index)
    lecturas=lecturas.drop(index=deleted[0])
    lecturas=lecturas.drop(index=deleted[1])
    lecturas=lecturas.drop(index=deleted[2])
    print(f"Lecturas recortadas: {lecturas.shape}")
    new_columns = []
    for col in lecturas.columns:
        try:
            # Intenta convertir la columna a una fecha y elimina las horas
            new_col = pd.to_datetime(col).strftime('%Y-%m-%d')
        except:
            new_col = col
        new_columns.append(new_col)
    lecturas.columns = new_columns
    lecturas=lecturas.groupby('NIC').sum().reset_index()
    return lecturas.reset_index(drop=True)
    

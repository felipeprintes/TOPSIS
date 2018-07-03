import pandas as pd
import numpy as np
from numpy import linalg as la


def calcule(file):

    file_df = pd.read_csv(file)
    normalizado = normaliza(file_df)
    pesos = np.array(file_df.iloc[0])
    #pesos = [0.55, 0.5, 0.15, 0.1]
    ponderado = ponderar(normalizado, pesos)
    nis = ponderado.min()
    pis = ponderado.max()
    difer_max = diferenca(ponderado, pis)
    difer_min = diferenca(ponderado, nis)
    coef = coeficientes(difer_max, difer_min)
    coef_df = pd.DataFrame(coef, columns=['coeficientes'])
    

    return coef_df.sort_values(by=['coeficientes'], ascending=False)


def normaliza(data_frame):

    data_frame_normalizado = data_frame.apply(la.norm)
    return data_frame / data_frame_normalizado


def ponderar(normalizado, pesos):
    return normalizado * pesos


def diferenca(ponderado, x):
    aux = (ponderado - x) ** 2
    aux = aux.sum(axis=1)
    aux = np.sqrt(aux)
    return aux


def coeficientes(difer_max, difer_min):
    return difer_min / (difer_max + difer_min)



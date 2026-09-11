import numpy as np
from pathlib import Path
import questionary


####################################################################################################
## Data

## GNSS Blocks 2023
gnssbl23 = {'IIR-A' : [13, 16, 20, 21, 22], 
            'IIR-B' : [2, 19], 
            'IIR-M' : [5, 7, 12, 15, 17, 29, 31], 
            'IIF' : [1, 3, 6, 8, 9, 10, 24, 25, 26, 27, 30, 32], 
            'IIIA' : [4, 11, 14, 18, 23, 28], 
            'GAL1' : [211, 212, 219, 220], 
            'GAL2' : [201, 202, 203, 204, 205, 207, 208, 209, 210, 213, 214, 215, 218, 
                      221, 222, 224, 225, 226, 227, 230, 231, 233, 234, 236]}

## Header der Daten als Liste
header_data = []


####################################################################################################
## Functions

def decision(text: str):
    answer = questionary.select(text, choices=[
        questionary.Choice("Yes", True), 
        questionary.Choice("No", False)]).ask()
    return answer


with open('output/output.txt', 'w') as file:
    file.write('Various Outputs\n\n')

def paper(text: str):
    with open('output/output.txt', 'a') as file:
        file.write(text + '\n')


##################################################

def load_data(folder='input'):
    data_name = []
    for d in Path(folder).iterdir():
        data_name.append(d.name)
    
    with open(Path(folder) / data_name[0], 'r', encoding='utf-8') as file:
        header = file.readline().strip().split()  # Liest nur die erste Zeile
        header[3:5] = [header[3] + ' ' + header[4]]
        header_data.extend(header)
    
    data = np.zeros((0, len(header_data)))
    for i in range(len(data_name)):
        data = np.vstack((data, np.loadtxt(Path(folder) / data_name[i], skiprows=1)))
    return data


##################################################

def binning_1d(data: np.ndarray, 
               bincol: tuple[int, int], 
               binning: int):
    datax = np.round(data[:, bincol[0]] / binning) * binning
    datay = data[:, bincol[1]]

    data_binx, data_biny = [], []
    for x in np.unique(datax):
        values = datay[datax == x]
        data_binx.append(x)
        data_biny.append(values)
    return np.array(data_binx), data_biny


def binning_2d(data: np.ndarray, 
               bincol: tuple[int, int, int], 
               binning: tuple[float, float]):
    datax = np.round(data[:, bincol[0]] / binning[0]) * binning[0]
    datay = np.round(data[:, bincol[1]] / binning[1]) * binning[1]
    dataz = data[:, bincol[2]]

    data_binx, data_biny, data_binz = [], [], []
    for x in np.unique(datax):
        for y in np.unique(datay):
            values = dataz[(datax == x) & (datay == y)]
            data_binx.append(x)
            data_biny.append(y)
            data_binz.append(values)
    return np.array(data_binx), np.array(data_biny), data_binz


##################################################

def weight_matrix_P(values, sigma0=1):
    C_ll = np.diag([(1 / values[i]) for i in range(len(values))])
    return sigma0**2 * np.linalg.inv(C_ll)

def A_matrix(X0, x):
    A = np.zeros((len(x), len(X0)))
    for i in range(len(x)):
        A[i, :] = np.array([np.exp(X0[1] * x[i]), X0[0] * x[i] * np.exp(X0[1] * x[i]), 1]) # d/dA, d/db, d/dd
    return A

def modelfunction(x: np.ndarray, A: float, b: float, d: float):
    return d + A * np.exp(b * x)

def unit_weight_m0(F, L, X, P):
    v = F - L
    m0 = np.sqrt((np.transpose(v) @ P @ v) / (len(L) - len(X)))
    return m0

def fitting_exp(parameters: list[float, float, float], 
                L: np.ndarray, xdata: np.ndarray, 
                P_values=None):
    maxfev = 10000
    eps = 10**(-4)
    if P_values is None: P_values = np.ones(len(xdata))
    P = weight_matrix_P(np.asarray(P_values), 1)
    X0 = parameters

    for i in range(maxfev):
        A = A_matrix(X0, xdata)
        F = modelfunction(xdata, X0[0], X0[1], X0[2])
        l = L - F
        N = np.transpose(A) @ P @ A
        b = np.transpose(A) @ P @ l
        x = np.linalg.solve(N, b)
        X = X0 + x
        if all(np.abs(x) < eps): break
        X0 = X
    
    rms = unit_weight_m0(modelfunction(xdata, *X), L, X, P)
    return X, rms


import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
import matplotlib.colors as mcolors
import pandas as pd

import genesis_functions as gf


####################################################################################################

print()
print('####################################################################################################')
print('##########' + ''.center(80) + '##########')
print('##########' + "GENESIS - Plots for the Bachelor's Thesis".center(80) + '##########')
print('##########' + 'NOTES'.center(80) + '##########')
print('##########' + ''.center(80) + '##########')
print('####################################################################################################')
print()


data = gf.load_data('input')


####################################################################################################
## Notes


##################################################
## STD fitting with P but also with E14 and E18

dataSPnGAL2 = gf.binning_1d(data[(data[:, 1] == 1) & (np.isin(data[:, 4], gf.gnssbl23['GAL2']))], (10, 5), 1)
dataSPnGAL2_FIT = gf.fitting_exp([0.000005, 0.35, 0.003], np.array([np.std(v) for v in dataSPnGAL2[1]]), dataSPnGAL2[0], np.array([len(v) for v in dataSPnGAL2[1]]))

fig, ax = plt.subplots(figsize=(6, 4))
ax.plot(dataSPnGAL2[0], np.array([np.std(v) for v in dataSPnGAL2[1]]), label='Nadir antenna', color='red', linestyle='-', marker='.', markersize=3)
ax.plot(dataSPnGAL2[0], gf.modelfunction(dataSPnGAL2[0], *dataSPnGAL2_FIT[0]), label='Modelfunction\nRMS = ' + f'${dataSPnGAL2_FIT[1]:.3e}$', color='black', linestyle='-', marker='.', markersize=3)
ax.set_xlabel('Nadir Angle $[°]$')
ax.set_ylabel('STD of Residuals $[m]$')
ax.grid(True, linestyle=':', alpha=0.6, color='gray')
ax.legend(loc='upper right')
plt.tight_layout()
plt.show(block=False)

dataSPzGAL2 = gf.binning_1d(data[(data[:, 1] == 2) & (np.isin(data[:, 4], gf.gnssbl23['GAL2']))], (10, 5), 1)
dataSPzGAL2_FIT = gf.fitting_exp([0.000003, 0.35, 0.003], np.array([np.std(v) for v in dataSPzGAL2[1]]), dataSPzGAL2[0], np.array([len(v) for v in dataSPzGAL2[1]]))

fig, ax = plt.subplots(figsize=(6, 4))
ax.plot(dataSPzGAL2[0], np.array([np.std(v) for v in dataSPzGAL2[1]]), label='Zenith antenna', color='blue', linestyle='-', marker='.', markersize=3)
ax.plot(dataSPzGAL2[0], gf.modelfunction(dataSPzGAL2[0], *dataSPzGAL2_FIT[0]), label='Modelfunction\nRMS = ' + f'${dataSPzGAL2_FIT[1]:.3e}$', color='black', linestyle='-', marker='.', markersize=3)
ax.set_xlabel('Nadir Angle $[°]$')
ax.set_ylabel('STD of Residuals $[m]$')
ax.grid(True, linestyle=':', alpha=0.6, color='gray')
ax.legend(loc='upper right')
plt.tight_layout()
plt.show(block=False)


##################################################
## STD fitting for blocks IIR-B, IIR-M, IIIA

dataSPnGAL2 = gf.binning_1d(data[(data[:, 1] == 1) & (np.isin(data[:, 4], gf.gnssbl23['IIIA'])) & (data[:, 4] != 214) & (data[:, 4] != 218)], (10, 5), 1)
dataSPnGAL2_FIT = gf.fitting_exp([0.0000025, 0.35, 0.003], np.array([np.std(v) for v in dataSPnGAL2[1]]), dataSPnGAL2[0], np.array([len(v) for v in dataSPnGAL2[1]]))

fig, ax = plt.subplots(figsize=(6, 4))
ax.plot(dataSPnGAL2[0], np.array([np.std(v) for v in dataSPnGAL2[1]]), label='Nadir antenna', color='red', linestyle='-', marker='.', markersize=3)
ax.plot(dataSPnGAL2[0], gf.modelfunction(dataSPnGAL2[0], *dataSPnGAL2_FIT[0]), label='Modelfunction\nRMS = ' + f'${1:.3e}$', color='black', linestyle='-', marker='.', markersize=3)
ax.set_xlabel('Nadir Angle $[°]$')
ax.set_ylabel('STD of Residuals $[m]$')
ax.grid(True, linestyle=':', alpha=0.6, color='gray')
ax.legend(loc='upper right')
plt.tight_layout()
plt.show(block=False)

dataSPzGAL2 = gf.binning_1d(data[(data[:, 1] == 2) & (np.isin(data[:, 4], gf.gnssbl23['IIIA'])) & (data[:, 4] != 214) & (data[:, 4] != 218)], (10, 5), 1)
dataSPzGAL2_FIT = gf.fitting_exp([0.000003, 0.35, 0.003], np.array([np.std(v) for v in dataSPzGAL2[1]]), dataSPzGAL2[0])

fig, ax = plt.subplots(figsize=(6, 4))
ax.plot(dataSPzGAL2[0], np.array([np.std(v) for v in dataSPzGAL2[1]]), label='Zenith antenna', color='blue', linestyle='-', marker='.', markersize=3)
ax.plot(dataSPzGAL2[0], gf.modelfunction(dataSPzGAL2[0], *dataSPzGAL2_FIT[0]), label='Modelfunction\nRMS = ' + f'${1:.3e}$', color='black', linestyle='-', marker='.', markersize=3)
ax.set_xlabel('Nadir Angle $[°]$')
ax.set_ylabel('STD of Residuals $[m]$')
ax.grid(True, linestyle=':', alpha=0.6, color='gray')
ax.legend(loc='upper right')
plt.tight_layout()
plt.show(block=False)


##################################################
## STD for Blocks IIR-A, IIIA for Nadir antenna

# # label_text = f"${f'{value:.1e}'.split('e')[0]} \\times 10^{{{int(f'{value:.1e}'.split('e')[1])}}}$"
# f'${dataSPnGAL1_ELE_FIT[1]:.3e}$'
# f"${f'{dataSPnGAL1_ELE_FIT[1]:.3e}'.split('e')[0]} \\times 10^{{{int(f'{dataSPnGAL1_ELE_FIT[1]:.3e}'.split('e')[1])}}}$"


##################################################
## STD for Blocks IIR-A, IIIA for Nadir antenna

blkPara = {'IIR-A' : [[8.0e-5, 0.25, 0.0044], [0.000005, 0.35, 0.003]], 
           'IIR-B' : [[0.000005, 0.35, 0.003], [0.000003, 0.35, 0.003]], 
           'IIR-M' : [[0.0000025, 0.35, 0.003], [0.000003, 0.35, 0.003]], 
           'IIF' : [[0.000005, 0.35, 0.003], [0.000005, 0.35, 0.003]], 
           'IIIA' : [[0.0000025, 0.35, 0.003], [0.000003, 0.35, 0.003]], 
           'GAL1' : [[0.000005, 0.35, 0.003], [0.000005, 0.35, 0.003]], 
           'GAL2' : [[0.000005, 0.35, 0.003], [0.000003, 0.35, 0.003]]} # [[Nadir], [Zenith]]

blkPmat = {'IIR-A' : [True, False], 
           'IIR-B' : [False, False], 
           'IIR-M' : [False, False], 
           'IIF' : [False, False], 
           'IIIA' : [True, False], 
           'GAL1' : [False, False], 
           'GAL2' : [False, False]} # [Nadir, Zenith]


def parameter_check(block, para, fitfunc=False):
    dataSPn = gf.binning_1d(data[(data[:, 1] == 1) & (np.isin(data[:, 4], gf.gnssbl23[block])) & (data[:, 4] != 214) & (data[:, 4] != 218)], (10, 5), 1)
    if fitfunc: dataSPn_FIT = gf.fitting_exp(para, np.array([np.std(v) for v in dataSPn[1]]), dataSPn[0])

    fig, ax = plt.subplots(figsize=(6, 4))
    ax.plot(dataSPn[0], np.array([np.std(v) for v in dataSPn[1]]), label='Nadir antenna', color='red', linestyle='-', marker='.', markersize=3)
    ax.plot(dataSPn[0], gf.modelfunction(dataSPn[0], *para), color='black', linestyle='-', marker='none')
    if fitfunc: ax.plot(np.arange(np.min(dataSPn[0]), np.max(dataSPn[0]) + 0.01, 0.01), gf.modelfunction(np.arange(np.min(dataSPn[0]), np.max(dataSPn[0]) + 0.01, 0.01), *dataSPn_FIT[0]), label='Modelfunction\nRMS = ' + f'${dataSPn_FIT[1]:.3e}$', color='gray', linestyle='-', marker='none')
    ax.set_xlabel('Nadir Angle $[°]$')
    ax.set_ylabel('STD of Residuals $[m]$')
    ax.grid(True, linestyle=':', alpha=0.6, color='gray')
    ax.legend(loc='upper right')
    plt.tight_layout()
    plt.show(block=False)

parameter_check('IIR-A', [8.0e-5, 0.25, 0.0044])
parameter_check('IIIA', [0.0000025, 0.35, 0.003])


##################################################
## Binning 1D: 10° = 10°-11° -> normal np.round()

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

liste = [0, 0.4, 0.5, 0.6, 1.4, 1.5, 1.6, 2.4, 2.5, 2.6, 3.4, 3.5, 3.6]
values = [i for i in range(len(liste))]

print(liste)
print(values)
print(binning_1d(np.array([[liste[i], values[i]] for i in range(len(liste))]), (0, 1), 1)[0])
print(np.round(liste))

##################################################
## Satellite track

print(gf.gnssbl23['GAL2'])
## Satellites: [201, 202, 203, 204, 205, 207, 208, 209, 210, 213, 214, 215, 218, 221, 222, 224, 225, 226, 227, 230, 231, 233, 234, 236]

for satellite in gf.gnssbl23['GAL2']:
    print(f'Satellite: {satellite}')
    dataRPzGAL2 = data[(data[:, 1] == 2) & (np.isin(data[:, 4], gf.gnssbl23['GAL2'])) & (data[:, 4] == satellite)]

    fig, ax = plt.subplots(figsize=(6, 4))
    ax.plot(dataRPzGAL2[:, 10], dataRPzGAL2[:, 5] * 100, label=f'Satellite {satellite} Zenith antenna', color='blue', linestyle='none', marker='.', markersize=1)
    ax.set_xlabel(r'Nadir Angle $(\mathrm{°})$')
    ax.set_ylabel(r'Residuals $(\mathrm{cm})$')
    ax.grid(True, linestyle=':', alpha=0.6, color='gray')
    ax.legend(loc='upper right')
    plt.tight_layout()
    # if save_plots: plt.savefig('output/res_plot_blk_GAL2_nadir_angle_zenit.png', format='png', bbox_inches='tight', dpi=300)
    plt.show(block=False)

    fig, ax = plt.subplots(figsize=(6, 4))
    ax.plot(dataRPzGAL2[:, 8], dataRPzGAL2[:, 5] * 100, label=f'Satellite {satellite} Zenith antenna', color='blue', linestyle='none', marker='.', markersize=1)
    ax.set_xlabel(r'Elevation $(\mathrm{°})$')
    ax.set_ylabel(r'Residuals $(\mathrm{cm})$')
    ax.grid(True, linestyle=':', alpha=0.6, color='gray')
    ax.legend(loc='upper right')
    plt.tight_layout()
    # if save_plots: plt.savefig('output/res_plot_blk_GAL2_elevation_zenit.png', format='png', bbox_inches='tight', dpi=300)
    plt.show(block=False)


satellite = 214
dataRPzGAL2 = data[(data[:, 1] == 2) & (np.isin(data[:, 4], gf.gnssbl23['GAL2'])) & (data[:, 4] == satellite)]

fig, ax = plt.subplots(figsize=(6, 4))
ax.plot(dataRPzGAL2[:, 10], dataRPzGAL2[:, 5] * 100, label='Zenith antenna', color='blue', linestyle='none', marker='.', markersize=1)
ax.set_xlabel(r'Nadir Angle $(\mathrm{°})$')
ax.set_ylabel(r'Residuals $(\mathrm{cm})$')
ax.grid(True, linestyle=':', alpha=0.6, color='gray')
ax.legend(loc='upper right')
plt.tight_layout()
# if save_plots: plt.savefig('output/res_plot_blk_GAL2_nadir_angle_zenit.png', format='png', bbox_inches='tight', dpi=300)
plt.show(block=False)

fig, ax = plt.subplots(figsize=(6, 4))
ax.plot(dataRPzGAL2[:, 8], dataRPzGAL2[:, 5] * 100, label='Zenith antenna', color='blue', linestyle='none', marker='.', markersize=1)
ax.set_xlabel(r'Elevation $(\mathrm{°})$')
ax.set_ylabel(r'Residuals $(\mathrm{cm})$')
ax.grid(True, linestyle=':', alpha=0.6, color='gray')
ax.legend(loc='upper right')
plt.tight_layout()
# if save_plots: plt.savefig('output/res_plot_blk_GAL2_elevation_zenit.png', format='png', bbox_inches='tight', dpi=300)
plt.show(block=False)


for satellite in gf.gnssbl23['GAL2']:
    print(f'Satellite: {satellite}')
    dataRPnGAL2 = data[(data[:, 1] == 1) & (np.isin(data[:, 4], gf.gnssbl23['GAL2'])) & (data[:, 4] == satellite)]

    fig, ax = plt.subplots(figsize=(6, 4))
    ax.plot(dataRPnGAL2[:, 10], dataRPnGAL2[:, 5] * 100, label=f'Satellite {satellite} Nadir antenna', color='red', linestyle='none', marker='.', markersize=1)
    ax.set_xlabel(r'Nadir Angle $(\mathrm{°})$')
    ax.set_ylabel(r'Residuals $(\mathrm{cm})$')
    ax.grid(True, linestyle=':', alpha=0.6, color='gray')
    ax.legend(loc='upper right')
    plt.tight_layout()
    # if save_plots: plt.savefig('output/res_plot_blk_GAL2_nadir_angle_nadir.png', format='png', bbox_inches='tight', dpi=300)
    plt.show(block=False)

    fig, ax = plt.subplots(figsize=(6, 4))
    ax.plot(dataRPnGAL2[:, 8], dataRPnGAL2[:, 5] * 100, label=f'Satellite {satellite} Nadir antenna', color='red', linestyle='none', marker='.', markersize=1)
    ax.set_xlabel(r'Elevation $(\mathrm{°})$')
    ax.set_ylabel(r'Residuals $(\mathrm{cm})$')
    ax.grid(True, linestyle=':', alpha=0.6, color='gray')
    ax.legend(loc='upper right')
    plt.tight_layout()
    # if save_plots: plt.savefig('output/res_plot_blk_GAL2_elevation_nadir.png', format='png', bbox_inches='tight', dpi=300)
    plt.show(block=False)


##################################################
## Marker Circle

dataRPnGAL2 = data[(data[:, 1] == 1) & (np.isin(data[:, 4], gf.gnssbl23['GAL2']))]

fig, ax = plt.subplots(figsize=(6, 4))
ax.plot(dataRPnGAL2[:, 10], dataRPnGAL2[:, 5] * 100, label='Nadir antenna', color='red', linestyle='none', marker='.', markersize=1)
# ax.plot((1 * np.cos(np.arange(0, 2*np.pi, 0.01)) + 10), (1 * np.sin(np.arange(0, 2*np.pi, 0.01))), color='black', linestyle='-', marker='none')
ax.plot(12, 0, marker='o', markersize=48, color='black', markerfacecolor='none', markeredgewidth=1)
ax.set_xlabel(r'Nadir Angle $(\mathrm{°})$')
ax.set_ylabel(r'Residuals $(\mathrm{cm})$')
ax.grid(True, linestyle=':', alpha=0.6, color='gray')
ax.legend(loc='upper right')
plt.tight_layout()
# if save_plots: plt.savefig('output/res_plot_blk_GAL2_nadir_angle_nadir.png', format='png', bbox_inches='tight', dpi=300)
plt.show(block=False)


##################################################
## grössere Punkte in der Legende

fig, ax = plt.subplots(figsize=(6, 4))#, dpi=300)
ax.plot(data[data[:, 1] == 1][:, 6], data[data[:, 1] == 1][:, 5] * 100, label='Nadir antenna', color='red', linestyle='none', marker=',', markersize=1)
ax.plot(data[data[:, 1] == 2][:, 6], data[data[:, 1] == 2][:, 5] * 100, label='Zenith antenna', color='blue', linestyle='none', marker=',', markersize=1)
ax.set_xlabel(r'Elevation $(\mathrm{°})$')
ax.set_ylabel(r'Residuals $(\mathrm{cm})$')
ax.grid(True, linestyle=':', alpha=0.6, color='gray')
legend = ax.legend(loc='upper right')
for handle in legend.legend_handles:
    handle.set_marker('o')
    handle.set_markersize(6)
plt.tight_layout()
# if save_plots: plt.savefig('output/res_plot_elevation.png', format='png', bbox_inches='tight', dpi=300)
plt.show(block=False)


##################################################
## Modelfunction for GNSS Blocks

parameters = {
    'IIR-A Nadir'  : [28, 4.794437e-07, 4.965612e-01, 4.456246e-03], 
    'IIR-A Zenith' : [28, 4.668740e-08, 5.661410e-01, 3.642837e-03], 
    'IIR-B Nadir'  : [28, 1.240642e-06, 4.201067e-01, 2.866971e-03], 
    'IIR-B Zenith' : [28, 9.311179e-08, 4.981462e-01, 2.322923e-03], 
    'IIR-M Nadir'  : [28, 2.037010e-04, 1.695579e-01, 8.215380e-04], 
    'IIR-M Zenith' : [28, 8.261693e-06, 2.743541e-01, 2.610453e-03], 
    'IIF Nadir'    : [28, 2.037016e-05, 2.567938e-01, 2.477394e-03], 
    'IIF Zenith'   : [28, 1.838260e-06, 3.388548e-01, 2.353042e-03], 
    'IIIA Nadir'   : [28, 8.857770e-05, 2.034767e-01, 1.269160e-03], 
    'IIIA Zenith'  : [28, 1.310130e-05, 2.576624e-01, 2.217166e-03], 
    'GAL1 Nadir'   : [25, 5.567894e-06, 3.740089e-01, 2.882756e-03], 
    'GAL1 Zenith'  : [25, 3.068913e-07, 5.030183e-01, 2.206754e-03], 
    'GAL2 Nadir'   : [25, 1.611809e-06, 3.956581e-01, 2.945887e-03], 
    'GAL2 Zenith'  : [25, 3.684445e-07, 4.435445e-01, 2.675906e-03]
} ## 09.09.2026

para = [['IIR-A Nadir', 'IIR-A Zenith', 'IIR-B Nadir', 'IIR-B Zenith', 'IIR-M Nadir', 'IIR-M Zenith', 'IIF Nadir', 'IIF Zenith', 'IIIA Nadir', 'IIIA Zenith', 'GAL1 Nadir', 'GAL1 Zenith', 'GAL2 Nadir', 'GAL2 Zenith'], 
        ['IIR-A Nadir', 'IIR-A Zenith'], 
        ['IIR-B Nadir', 'IIR-B Zenith'], 
        ['IIR-M Nadir', 'IIR-M Zenith'], 
        ['IIF Nadir', 'IIF Zenith'], 
        ['IIIA Nadir', 'IIIA Zenith'], 
        ['GAL1 Nadir', 'GAL1 Zenith'], 
        ['GAL2 Nadir', 'GAL2 Zenith']]

from matplotlib.backends.backend_pdf import PdfPages

with PdfPages('modelfunction_blocks.pdf') as pdf:

    for i in range(len(para)):
        fig, ax = plt.subplots(figsize=(6, 4))
        for key in para[i]:
            x_data = np.arange(0, parameters[key][0], 0.01)
            ax.plot(x_data, gf.modelfunction(x_data, parameters[key][1], parameters[key][2], parameters[key][3]) * 100, label=key, linestyle='-', marker='none')
        ax.set_xlabel(r'Nadir Angle $(\mathrm{°})$')
        ax.set_ylabel(r'STD of Residuals $(\mathrm{cm})$')
        ax.grid(True, linestyle=':', alpha=0.6, color='gray')
        ax.legend(loc='upper right')
        plt.tight_layout()
        # if save_plots: plt.savefig('output/std_plot_blk_GAL2_nadir_angle_nadir.png', format='png', bbox_inches='tight', dpi=300)
        # plt.show(block=False)
        pdf.savefig(fig)
        plt.close(fig)


##################################################
## Azimuth for Elevation < 25°

dataRPnGAL2 = data[(data[:, 1] == 1) & (np.isin(data[:, 4], gf.gnssbl23['GAL2'])) & (data[:, 6] < 30)]

fig, ax = plt.subplots(figsize=(6, 4))
ax.plot(dataRPnGAL2[:, 9], dataRPnGAL2[:, 5] * 100, label='Nadir antenna', color='red', linestyle='none', marker='.', markersize=1)
ax.set_xlabel(r'Azimuth of Genesis $(\mathrm{°})$')
ax.set_ylabel(r'Residuals $(\mathrm{cm})$')
ax.grid(True, linestyle=':', alpha=0.6, color='gray')
ax.legend(loc='upper right')
ax.set_ylim(-6, +6)
plt.tight_layout()
# if save_plots: plt.savefig('output/res_plot_blk_GAL2_azimut_genesis_nadir.png', format='png', bbox_inches='tight', dpi=300)
plt.show(block=False)


dataRPzGAL2 = data[(data[:, 1] == 2) & (np.isin(data[:, 4], gf.gnssbl23['GAL2'])) & (data[:, 6] < 30)]

fig, ax = plt.subplots(figsize=(6, 4))
ax.plot(dataRPzGAL2[:, 9], dataRPzGAL2[:, 5] * 100, label='Zenith antenna', color='blue', linestyle='none', marker='.', markersize=1)
ax.set_xlabel(r'Azimuth of Genesis $(\mathrm{°})$')
ax.set_ylabel(r'Residuals $(\mathrm{cm})$')
ax.grid(True, linestyle=':', alpha=0.6, color='gray')
ax.legend(loc='upper right')
ax.set_ylim(-6, +6)
plt.tight_layout()
# if save_plots: plt.savefig('output/res_plot_blk_GAL2_azimut_genesis_zenit.png', format='png', bbox_inches='tight', dpi=300)
plt.show(block=False)


print()
print()
input(10 * ' ' + '  Close Plots - Press Enter  '.center(80, '-') + 10 * ' ')
print()
print()
print('####################################################################################################')
print()


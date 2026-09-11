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
print('##########' + ''.center(80) + '##########')
print('####################################################################################################')
print()


# save_plots = True
# save_plots = False
save_plots = gf.decision('Save the plots?')

# Path('output').mkdir(exist_ok=True)
Path('output/appendix').mkdir(parents=True, exist_ok=True)

data = gf.load_data('input')
if save_plots: np.savetxt('output/data.txt', data, header=(10 * ' ').join(gf.header_data))


####################################################################################################
## Residuen-Plots
print('\n' + ' - '.rjust(10, ' ') + 'Residuen-Plots')

##################################################
## Nadir antenna & zenith antenna - Elevation
print(' * '.rjust(14, ' ') + 'Elevation: Nadir antenna & zenith antenna')

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
if save_plots: plt.savefig('output/res_plot_elevation.png', format='png', bbox_inches='tight', dpi=300)
plt.show(block=False)


##################################################
## Nadir antenna of day 1 - Elevation
print(' * '.rjust(14, ' ') + 'Elevation: Nadir antenna of day 1')

dataRPn1 = data[(data[:, 1] == 1) & (data[:, 0] == 1)]

fig, ax = plt.subplots(figsize=(6, 4))
ax.plot(dataRPn1[:, 6], dataRPn1[:, 5] * 100, label='Nadir antenna', color='red', linestyle='none', marker='.', markersize=1)
ax.set_xlabel(r'Elevation $(\mathrm{°})$')
ax.set_ylabel(r'Residuals $(\mathrm{cm})$')
ax.grid(True, linestyle=':', alpha=0.6, color='gray')
ax.legend(loc='upper right')
ax.set_ylim(-5, +5)
plt.tight_layout()
if save_plots: plt.savefig('output/res_plot_elevation_nadir.png', format='png', bbox_inches='tight', dpi=300)
plt.show(block=False)

fig, ax = plt.subplots(figsize=(6, 4))
ax.plot(dataRPn1[dataRPn1[:, 4] >= 200][:, 6], dataRPn1[dataRPn1[:, 4] >= 200][:, 5] * 100, label='Nadir antenna (Galileo)', color='red', linestyle='none', marker='.', markersize=1)
ax.set_xlabel(r'Elevation $(\mathrm{°})$')
ax.set_ylabel(r'Residuals $(\mathrm{cm})$')
ax.grid(True, linestyle=':', alpha=0.6, color='gray')
ax.legend(loc='upper right')
ax.set_ylim(-5, +5)
plt.tight_layout()
if save_plots: plt.savefig('output/res_plot_elevation_nadir_galileo.png', format='png', bbox_inches='tight', dpi=300)
plt.show(block=False)

fig, ax = plt.subplots(figsize=(6, 4))
ax.plot(dataRPn1[dataRPn1[:, 4] < 100][:, 6], dataRPn1[dataRPn1[:, 4] < 100][:, 5] * 100, label='Nadir antenna (GPS)', color='red', linestyle='none', marker='.', markersize=1)
ax.set_xlabel(r'Elevation $(\mathrm{°})$')
ax.set_ylabel(r'Residuals $(\mathrm{cm})$')
ax.grid(True, linestyle=':', alpha=0.6, color='gray')
ax.legend(loc='upper right')
ax.set_ylim(-5, +5)
plt.tight_layout()
if save_plots: plt.savefig('output/res_plot_elevation_nadir_gps.png', format='png', bbox_inches='tight', dpi=300)
plt.show(block=False)


##################################################
## Zenith antenna of day 1 - Elevation
print(' * '.rjust(14, ' ') + 'Elevation: Zenith antenna of day 1')

dataRPz1 = data[(data[:, 1] == 2) & (data[:, 0] == 1)]

fig, ax = plt.subplots(figsize=(6, 4))
ax.plot(dataRPz1[:, 6], dataRPz1[:, 5] * 100, label='Zenith antenna', color='blue', linestyle='none', marker='.', markersize=1)
ax.set_xlabel(r'Elevation $(\mathrm{°})$')
ax.set_ylabel(r'Residuals $(\mathrm{cm})$')
ax.grid(True, linestyle=':', alpha=0.6, color='gray')
ax.legend(loc='upper right')
ax.set_ylim(-5, +5)
plt.tight_layout()
if save_plots: plt.savefig('output/res_plot_elevation_zenit.png', format='png', bbox_inches='tight', dpi=300)
plt.show(block=False)

fig, ax = plt.subplots(figsize=(6, 4))
ax.plot(dataRPz1[dataRPz1[:, 4] >= 200][:, 6], dataRPz1[dataRPz1[:, 4] >= 200][:, 5] * 100, label='Zenith antenna (Galileo)', color='blue', linestyle='none', marker='.', markersize=1)
ax.set_xlabel(r'Elevation $(\mathrm{°})$')
ax.set_ylabel(r'Residuals $(\mathrm{cm})$')
ax.grid(True, linestyle=':', alpha=0.6, color='gray')
ax.legend(loc='upper right')
ax.set_ylim(-5, +5)
plt.tight_layout()
if save_plots: plt.savefig('output/res_plot_elevation_zenit_galileo.png', format='png', bbox_inches='tight', dpi=300)
plt.show(block=False)

fig, ax = plt.subplots(figsize=(6, 4))
ax.plot(dataRPz1[dataRPz1[:, 4] < 100][:, 6], dataRPz1[dataRPz1[:, 4] < 100][:, 5] * 100, label='Zenith antenna (GPS)', color='blue', linestyle='none', marker='.', markersize=1)
ax.set_xlabel(r'Elevation $(\mathrm{°})$')
ax.set_ylabel(r'Residuals $(\mathrm{cm})$')
ax.grid(True, linestyle=':', alpha=0.6, color='gray')
ax.legend(loc='upper right')
ax.set_ylim(-5, +5)
plt.tight_layout()
if save_plots: plt.savefig('output/res_plot_elevation_zenit_gps.png', format='png', bbox_inches='tight', dpi=300)
plt.show(block=False)


##################################################
## Nadir antenna, Zenith antenna of day 1 - Epoch
print(' * '.rjust(14, ' ') + 'Epoch: Nadir antenna, zenith antenna of day 1')

fig, ax = plt.subplots(figsize=(6, 4))
ax.plot((dataRPn1[:, 3] - int(dataRPn1[:, 3].min())) * 24, dataRPn1[:, 5] * 100, label='Nadir antenna', color='red', linestyle='none', marker='.', markersize=1)
ax.set_xlabel(r'Epoch $(\mathrm{hours})$')
ax.set_ylabel(r'Residuals $(\mathrm{cm})$')
ax.grid(True, linestyle=':', alpha=0.6, color='gray')
ax.legend(loc='upper right')
ax.set_ylim(-5, +5)
plt.tight_layout()
if save_plots: plt.savefig('output/res_plot_epoche_nadir.png', format='png', bbox_inches='tight', dpi=300)
plt.show(block=False)

fig, ax = plt.subplots(figsize=(6, 4))
ax.plot((dataRPz1[:, 3] - int(dataRPz1[:, 3].min())) * 24, dataRPz1[:, 5] * 100, label='Zenith antenna', color='blue', linestyle='none', marker='.', markersize=1)
ax.set_xlabel(r'Epoch $(\mathrm{hours})$')
ax.set_ylabel(r'Residuals $(\mathrm{cm})$')
ax.grid(True, linestyle=':', alpha=0.6, color='gray')
ax.legend(loc='upper right')
ax.set_ylim(-5, +5)
plt.tight_layout()
if save_plots: plt.savefig('output/res_plot_epoche_zenit.png', format='png', bbox_inches='tight', dpi=300)
plt.show(block=False)

gf.paper(f'Nadir antenna: RMS = {np.std(dataRPn1[:, 5] * 100):.3e} cm')
gf.paper(f'Zenith antenna: RMS = {np.std(dataRPz1[:, 5] * 100):.3e} cm')


####################################################################################################
## Polar-Plots
print('\n' + ' - '.rjust(10, ' ') + 'Polar-Plots')

def satellite_track(data: np.ndarray, title: str):
    values, number = np.unique(data[:, 4], return_counts=True)
    imax = np.argmax(number)

    gf.paper(f'\n{title}')
    print(14 * ' ' + f'Satellite Track of Satellite {int(values[imax])}')
    gf.paper(f'Satellite Track of Satellite {int(values[imax])}')

    data_track = data[(data[:, 4] == values[imax])]# & (data[:, 6] <= 30)]
    print(f"{'':14}{'Epoch':>6} {'Elev':>8} {'Azi':>8}\n{'':14}{'-' * 24}")
    gf.paper(f"{'Epoch':>6} {'Elev':>8} {'Azi':>8}\n{'-' * 24}")
    for row in data_track[:10, [2, 6, 7]]:
        print(f"{'':14}{row[0]:6.0f} {row[1]:8.2f} {row[2]:8.2f}")
        gf.paper(f"{row[0]:6.0f} {row[1]:8.2f} {row[2]:8.2f}")


def global_colorscale(): ## Google KI-Modus
    data_filter = [(data[:, 1] == 1) & (data[:, 4] >= 200), 
                   (data[:, 1] == 1) & (data[:, 4] < 100),
                   (data[:, 1] == 2) & (data[:, 4] >= 200), 
                   (data[:, 1] == 2) & (data[:, 4] < 100)]
    max_res, max_num = 0, 0

    for df in data_filter:
        data_z = gf.binning_2d(data[df], (7, 6, 5), (1, 1))[2]
        values_res = np.array([(np.mean(v) * 100) if len(v) > 0 else 0 for v in data_z])
        values_num = np.array([len(v) for v in data_z])

        local_max_res = max(abs(values_res.min()), values_res.max())
        local_max_num = values_num.max()
        if local_max_res > max_res: max_res = local_max_res
        if local_max_num > max_num: max_num = local_max_num
    
    return max_res, max_num

max_res, max_num = global_colorscale()
print(14 * ' ' + f'Max: Residuals {max_res:.3f} cm')
print(14 * ' ' + f'Max: Number of Measurements {max_num}')
gf.paper(f'Max: Residuals {max_res:.3f} cm')
gf.paper(f'Max: Number of Measurements {max_num}')

max_res = 4.0


##################################################
## Nadir antenna (Galileo)
print(' * '.rjust(14, ' ') + 'Nadir antenna (Galileo)')

data_theta, data_r, data_z = gf.binning_2d(data[(data[:, 1] == 1) & (data[:, 4] >= 200)], (7, 6, 5), (1, 1))

norm = mcolors.TwoSlopeNorm(vmin=-max_res, vcenter=0, vmax=max_res) # vmin=-absmax, vmax=absmax
fig, ax = plt.subplots(subplot_kw={'projection' : 'polar'}, figsize=(6, 4))
sc = ax.scatter(np.deg2rad(data_theta), data_r, c=np.array([(np.mean(v) * 100) if len(v) > 0 else 0 for v in data_z]), cmap='seismic', s=2, alpha=1, edgecolors='none', norm=norm)
ax.set_ylim(90, 0)
ax.set_theta_zero_location('N')
ax.set_theta_direction(-1) # im Uhrzeigersinn
fig.colorbar(sc, ax=ax, label=r'Residuals $(\mathrm{cm})$')
plt.tight_layout()
if save_plots: plt.savefig('output/pol_plot_nadir_galileo_res.png', format='png', bbox_inches='tight', dpi=300)
plt.show(block=False)

fig, ax = plt.subplots(subplot_kw={'projection' : 'polar'}, figsize=(6, 4))
sc = ax.scatter(np.deg2rad(data_theta), data_r, c=np.array([len(v) for v in data_z]), cmap='Blues', s=2, alpha=1, edgecolors='none', vmin=0, vmax=max_num)
ax.set_ylim(90, 0)
ax.set_theta_zero_location('N')
ax.set_theta_direction(-1) # im Uhrzeigersinn
fig.colorbar(sc, ax=ax, label='Number of measurements')
plt.tight_layout()
if save_plots: plt.savefig('output/pol_plot_nadir_galileo_num.png', format='png', bbox_inches='tight', dpi=300)
plt.show(block=False)

print(14 * ' ' + f'Mean: {np.mean(np.array([(np.mean(v) * 100) if len(v) > 0 else 0 for v in data_z])):.3e} cm')

satellite_track(data[(data[:, 1] == 1) & (data[:, 4] >= 200)], 'Polar-Plots: Nadir antenna (Galileo)')


##################################################
## Nadir antenna (GPS)
print(' * '.rjust(14, ' ') + 'Nadir antenna (GPS)')

data_theta, data_r, data_z = gf.binning_2d(data[(data[:, 1] == 1) & (data[:, 4] < 100)], (7, 6, 5), (1, 1))

norm = mcolors.TwoSlopeNorm(vmin=-max_res, vcenter=0, vmax=max_res) # vmin=-absmax, vmax=absmax
fig, ax = plt.subplots(subplot_kw={'projection' : 'polar'}, figsize=(6, 4))
sc = ax.scatter(np.deg2rad(data_theta), data_r, c=np.array([(np.mean(v) * 100) if len(v) > 0 else 0 for v in data_z]), cmap='seismic', s=2, alpha=1, edgecolors='none', norm=norm)
ax.set_ylim(90, 0)
ax.set_theta_zero_location('N')
ax.set_theta_direction(-1) # im Uhrzeigersinn
fig.colorbar(sc, ax=ax, label=r'Residuals $(\mathrm{cm})$')
plt.tight_layout()
if save_plots: plt.savefig('output/pol_plot_nadir_gps_res.png', format='png', bbox_inches='tight', dpi=300)
plt.show(block=False)

fig, ax = plt.subplots(subplot_kw={'projection' : 'polar'}, figsize=(6, 4))
sc = ax.scatter(np.deg2rad(data_theta), data_r, c=np.array([len(v) for v in data_z]), cmap='Blues', s=2, alpha=1, edgecolors='none', vmin=0, vmax=max_num)
ax.set_ylim(90, 0)
ax.set_theta_zero_location('N')
ax.set_theta_direction(-1) # im Uhrzeigersinn
fig.colorbar(sc, ax=ax, label='Number of measurements')
plt.tight_layout()
if save_plots: plt.savefig('output/pol_plot_nadir_gps_num.png', format='png', bbox_inches='tight', dpi=300)
plt.show(block=False)

print(14 * ' ' + f'Mean: {np.mean(np.array([(np.mean(v) * 100) if len(v) > 0 else 0 for v in data_z])):.3e} cm')

satellite_track(data[(data[:, 1] == 1) & (data[:, 4] < 100)], 'Polar-Plots: Nadir antenna (GPS)')


##################################################
## Zenith antenna (Galileo)
print(' * '.rjust(14, ' ') + 'Zenith antenna (Galileo)')

data_theta, data_r, data_z = gf.binning_2d(data[(data[:, 1] == 2) & (data[:, 4] >= 200)], (7, 6, 5), (1, 1))

norm = mcolors.TwoSlopeNorm(vmin=-max_res, vcenter=0, vmax=max_res) # vmin=-absmax, vmax=absmax
fig, ax = plt.subplots(subplot_kw={'projection' : 'polar'}, figsize=(6, 4))
sc = ax.scatter(np.deg2rad(data_theta), data_r, c=np.array([(np.mean(v) * 100) if len(v) > 0 else 0 for v in data_z]), cmap='seismic', s=2, alpha=1, edgecolors='none', norm=norm)
ax.set_ylim(90, 0)
ax.set_theta_zero_location('N')
ax.set_theta_direction(-1) # im Uhrzeigersinn
fig.colorbar(sc, ax=ax, label=r'Residuals $(\mathrm{cm})$')
plt.tight_layout()
if save_plots: plt.savefig('output/pol_plot_zenit_galileo_res.png', format='png', bbox_inches='tight', dpi=300)
plt.show(block=False)

fig, ax = plt.subplots(subplot_kw={'projection' : 'polar'}, figsize=(6, 4))
sc = ax.scatter(np.deg2rad(data_theta), data_r, c=np.array([len(v) for v in data_z]), cmap='Blues', s=2, alpha=1, edgecolors='none', vmin=0, vmax=max_num)
ax.set_ylim(90, 0)
ax.set_theta_zero_location('N')
ax.set_theta_direction(-1) # im Uhrzeigersinn
fig.colorbar(sc, ax=ax, label='Number of measurements')
plt.tight_layout()
if save_plots: plt.savefig('output/pol_plot_zenit_galileo_num.png', format='png', bbox_inches='tight', dpi=300)
plt.show(block=False)

print(14 * ' ' + f'Mean: {np.mean(np.array([(np.mean(v) * 100) if len(v) > 0 else 0 for v in data_z])):.3e} cm')

satellite_track(data[(data[:, 1] == 2) & (data[:, 4] >= 200)], 'Polar-Plots: Zenith antenna (Galileo)')


##################################################
## Zenith antenna (GPS)
print(' * '.rjust(14, ' ') + 'Zenith antenna (GPS)')

data_theta, data_r, data_z = gf.binning_2d(data[(data[:, 1] == 2) & (data[:, 4] < 100)], (7, 6, 5), (1, 1))

norm = mcolors.TwoSlopeNorm(vmin=-max_res, vcenter=0, vmax=max_res) # vmin=-absmax, vmax=absmax
fig, ax = plt.subplots(subplot_kw={'projection' : 'polar'}, figsize=(6, 4))
sc = ax.scatter(np.deg2rad(data_theta), data_r, c=np.array([(np.mean(v) * 100) if len(v) > 0 else 0 for v in data_z]), cmap='seismic', s=2, alpha=1, edgecolors='none', norm=norm)
ax.set_ylim(90, 0)
ax.set_theta_zero_location('N')
ax.set_theta_direction(-1) # im Uhrzeigersinn
fig.colorbar(sc, ax=ax, label=r'Residuals $(\mathrm{cm})$')
plt.tight_layout()
if save_plots: plt.savefig('output/pol_plot_zenit_gps_res.png', format='png', bbox_inches='tight', dpi=300)
plt.show(block=False)

fig, ax = plt.subplots(subplot_kw={'projection' : 'polar'}, figsize=(6, 4))
sc = ax.scatter(np.deg2rad(data_theta), data_r, c=np.array([len(v) for v in data_z]), cmap='Blues', s=2, alpha=1, edgecolors='none', vmin=0, vmax=max_num)
ax.set_ylim(90, 0)
ax.set_theta_zero_location('N')
ax.set_theta_direction(-1) # im Uhrzeigersinn
fig.colorbar(sc, ax=ax, label='Number of measurements')
plt.tight_layout()
if save_plots: plt.savefig('output/pol_plot_zenit_gps_num.png', format='png', bbox_inches='tight', dpi=300)
plt.show(block=False)

print(14 * ' ' + f'Mean: {np.mean(np.array([(np.mean(v) * 100) if len(v) > 0 else 0 for v in data_z])):.3e} cm')

satellite_track(data[(data[:, 1] == 2) & (data[:, 4] < 100)], 'Polar-Plots: Zenith antenna (GPS)')


####################################################################################################
## SD-Plots
print('\n' + ' - '.rjust(10, ' ') + 'SD-Plots')

dataPPnEx, dataPPnEy = gf.binning_1d(data[(data[:, 1] == 1) & (data[:, 4] >= 200)], (6, 5), 1)
dataPPnGx, dataPPnGy = gf.binning_1d(data[(data[:, 1] == 1) & (data[:, 4] < 100)], (6, 5), 1)
dataPPzEx, dataPPzEy = gf.binning_1d(data[(data[:, 1] == 2) & (data[:, 4] >= 200)], (6, 5), 1)
dataPPzGx, dataPPzGy = gf.binning_1d(data[(data[:, 1] == 2) & (data[:, 4] < 100)], (6, 5), 1)

fig, ax = plt.subplots(figsize=(6, 4))#, dpi=300)
ax.plot(dataPPnEx, np.array([(np.std(v) * 100) for v in dataPPnEy]), label='Nadir antenna (Galileo)', color='red', linestyle='-', marker='.', markersize=3)
ax.plot(dataPPnGx, np.array([(np.std(v) * 100) for v in dataPPnGy]), label='Nadir antenna (GPS)', color='darkred', linestyle='-', marker='.', markersize=3)
ax.plot(dataPPzEx, np.array([(np.std(v) * 100) for v in dataPPzEy]), label='Zenith antenna (Galileo)', color='blue', linestyle='-', marker='.', markersize=3)
ax.plot(dataPPzGx, np.array([(np.std(v) * 100) for v in dataPPzGy]), label='Zenith antenna (GPS)', color='darkblue', linestyle='-', marker='.', markersize=3)
ax.set_xlabel(r'Elevation $(\mathrm{°})$')
ax.set_ylabel(r'SD of Residuals $(\mathrm{cm})$')
ax.grid(True, linestyle=':', alpha=0.6, color='gray')
ax.legend(loc='upper right')
plt.tight_layout()
if save_plots: plt.savefig('output/std_plot_elevation.png', format='png', bbox_inches='tight', dpi=300)
plt.show(block=False)


####################################################################################################
## Residuen-Plots for Blocks
print('\n' + ' - '.rjust(10, ' ') + 'Residuen-Plots for Blocks')

##################################################
## Block GAL2: Nadir Angle, Elevation
print(' * '.rjust(14, ' ') + 'Block GAL2: Nadir Angle, Elevation')

dataRPnGAL2 = data[(data[:, 1] == 1) & (np.isin(data[:, 4], gf.gnssbl23['GAL2']))]

# dataRPzGAL2 = data[(data[:, 1] == 2) & (np.isin(data[:, 4], gf.gnssbl23['GAL2']))]
# ymin, ymax = np.vstack((dataRPnGAL2, dataRPzGAL2))[:, 5].min() * 100, np.vstack((dataRPnGAL2, dataRPzGAL2))[:, 5].max() * 100

fig, ax = plt.subplots(figsize=(6, 4))
ax.plot(dataRPnGAL2[:, 10], dataRPnGAL2[:, 5] * 100, label='Nadir antenna', color='red', linestyle='none', marker='.', markersize=1)
ax.plot(12, 0, marker='o', markersize=48, color='black', markerfacecolor='none', markeredgewidth=1)
ax.set_xlabel(r'Nadir Angle $(\mathrm{°})$')
ax.set_ylabel(r'Residuals $(\mathrm{cm})$')
ax.grid(True, linestyle=':', alpha=0.6, color='gray')
ax.legend(loc='upper right')
ax.set_ylim(-6, +6)
plt.tight_layout()
if save_plots: plt.savefig('output/res_plot_blk_GAL2_nadir_angle_nadir.png', format='png', bbox_inches='tight', dpi=300)
plt.show(block=False)

fig, ax = plt.subplots(figsize=(6, 4))
ax.plot(dataRPnGAL2[:, 8], dataRPnGAL2[:, 5] * 100, label='Nadir antenna', color='red', linestyle='none', marker='.', markersize=1)
ax.set_xlabel(r'Elevation $(\mathrm{°})$')
ax.set_ylabel(r'Residuals $(\mathrm{cm})$')
ax.grid(True, linestyle=':', alpha=0.6, color='gray')
ax.legend(loc='upper right')
ax.set_ylim(-6, +6)
plt.tight_layout()
if save_plots: plt.savefig('output/res_plot_blk_GAL2_elevation_nadir.png', format='png', bbox_inches='tight', dpi=300)
plt.show(block=False)


dataRPzGAL2 = data[(data[:, 1] == 2) & (np.isin(data[:, 4], gf.gnssbl23['GAL2']))]

fig, ax = plt.subplots(figsize=(6, 4))
ax.plot(dataRPzGAL2[:, 10], dataRPzGAL2[:, 5] * 100, label='Zenith antenna', color='blue', linestyle='none', marker='.', markersize=1)
ax.set_xlabel(r'Nadir Angle $(\mathrm{°})$')
ax.set_ylabel(r'Residuals $(\mathrm{cm})$')
ax.grid(True, linestyle=':', alpha=0.6, color='gray')
ax.legend(loc='upper right')
ax.set_ylim(-6, +6)
plt.tight_layout()
if save_plots: plt.savefig('output/res_plot_blk_GAL2_nadir_angle_zenit.png', format='png', bbox_inches='tight', dpi=300)
plt.show(block=False)

fig, ax = plt.subplots(figsize=(6, 4))
ax.plot(dataRPzGAL2[:, 8], dataRPzGAL2[:, 5] * 100, label='Zenith antenna', color='blue', linestyle='none', marker='.', markersize=1)
ax.set_xlabel(r'Elevation $(\mathrm{°})$')
ax.set_ylabel(r'Residuals $(\mathrm{cm})$')
ax.grid(True, linestyle=':', alpha=0.6, color='gray')
ax.legend(loc='upper right')
ax.set_ylim(-6, +6)
plt.tight_layout()
if save_plots: plt.savefig('output/res_plot_blk_GAL2_elevation_zenit.png', format='png', bbox_inches='tight', dpi=300)
plt.show(block=False)


##################################################
## Block GAL2: Azimuth of Genesis, Azimuth of GNSS
print(' * '.rjust(14, ' ') + 'Block GAL2: Azimuth of Genesis, Azimuth of GNSS')

dataRPnGAL2 = data[(data[:, 1] == 1) & (np.isin(data[:, 4], gf.gnssbl23['GAL2']))]

fig, ax = plt.subplots(figsize=(6, 4))
ax.plot(dataRPnGAL2[:, 9], dataRPnGAL2[:, 5] * 100, label='Nadir antenna', color='red', linestyle='none', marker='.', markersize=1)
ax.set_xlabel(r'Azimuth of Genesis $(\mathrm{°})$')
ax.set_ylabel(r'Residuals $(\mathrm{cm})$')
ax.grid(True, linestyle=':', alpha=0.6, color='gray')
ax.legend(loc='upper right')
ax.set_ylim(-6, +6)
plt.tight_layout()
if save_plots: plt.savefig('output/res_plot_blk_GAL2_azimut_genesis_nadir.png', format='png', bbox_inches='tight', dpi=300)
plt.show(block=False)

fig, ax = plt.subplots(figsize=(6, 4))
ax.plot(dataRPnGAL2[:, 11], dataRPnGAL2[:, 5] * 100, label='Nadir antenna', color='red', linestyle='none', marker='.', markersize=1)
ax.set_xlabel(r'Azimuth of GNSS $(\mathrm{°})$')
ax.set_ylabel(r'Residuals $(\mathrm{cm})$')
ax.grid(True, linestyle=':', alpha=0.6, color='gray')
ax.legend(loc='upper right')
ax.set_ylim(-6, +6)
plt.tight_layout()
if save_plots: plt.savefig('output/res_plot_blk_GAL2_azimut_gnss_nadir.png', format='png', bbox_inches='tight', dpi=300)
plt.show(block=False)


dataRPzGAL2 = data[(data[:, 1] == 2) & (np.isin(data[:, 4], gf.gnssbl23['GAL2']))]

fig, ax = plt.subplots(figsize=(6, 4))
ax.plot(dataRPzGAL2[:, 9], dataRPzGAL2[:, 5] * 100, label='Zenith antenna', color='blue', linestyle='none', marker='.', markersize=1)
ax.set_xlabel(r'Azimuth of Genesis $(\mathrm{°})$')
ax.set_ylabel(r'Residuals $(\mathrm{cm})$')
ax.grid(True, linestyle=':', alpha=0.6, color='gray')
ax.legend(loc='upper right')
ax.set_ylim(-6, +6)
plt.tight_layout()
if save_plots: plt.savefig('output/res_plot_blk_GAL2_azimut_genesis_zenit.png', format='png', bbox_inches='tight', dpi=300)
plt.show(block=False)

fig, ax = plt.subplots(figsize=(6, 4))
ax.plot(dataRPzGAL2[:, 11], dataRPzGAL2[:, 5] * 100, label='Zenith antenna', color='blue', linestyle='none', marker='.', markersize=1)
ax.set_xlabel(r'Azimuth of GNSS $(\mathrm{°})$')
ax.set_ylabel(r'Residuals $(\mathrm{cm})$')
ax.grid(True, linestyle=':', alpha=0.6, color='gray')
ax.legend(loc='upper right')
ax.set_ylim(-6, +6)
plt.tight_layout()
if save_plots: plt.savefig('output/res_plot_blk_GAL2_azimut_gnss_zenit.png', format='png', bbox_inches='tight', dpi=300)
plt.show(block=False)


##################################################
## Block GAL2: Nadir Angle, Elevation without the Satellites E14 and E18
print(' * '.rjust(14, ' ') + 'Block GAL2: Nadir Angle, Elevation without the Satellites E14 and E18')

dataRPnGAL2 = data[(data[:, 1] == 1) & (np.isin(data[:, 4], gf.gnssbl23['GAL2']) & (data[:, 4] != 214) & (data[:, 4] != 218))]

fig, ax = plt.subplots(figsize=(6, 4))
ax.plot(dataRPnGAL2[:, 10], dataRPnGAL2[:, 5] * 100, label='Nadir antenna', color='red', linestyle='none', marker='.', markersize=1)
ax.set_xlabel(r'Nadir Angle $(\mathrm{°})$')
ax.set_ylabel(r'Residuals $(\mathrm{cm})$')
ax.grid(True, linestyle=':', alpha=0.6, color='gray')
ax.legend(loc='upper right')
ax.set_ylim(-6, +6)
plt.tight_layout()
if save_plots: plt.savefig('output/res_plot_blk_GAL2_nadir_angle_woE14E18_nadir.png', format='png', bbox_inches='tight', dpi=300)
plt.show(block=False)

fig, ax = plt.subplots(figsize=(6, 4))
ax.plot(dataRPnGAL2[:, 8], dataRPnGAL2[:, 5] * 100, label='Nadir antenna', color='red', linestyle='none', marker='.', markersize=1)
ax.set_xlabel(r'Elevation $(\mathrm{°})$')
ax.set_ylabel(r'Residuals $(\mathrm{cm})$')
ax.grid(True, linestyle=':', alpha=0.6, color='gray')
ax.legend(loc='upper right')
ax.set_ylim(-6, +6)
plt.tight_layout()
if save_plots: plt.savefig('output/res_plot_blk_GAL2_elevation_woE14E18_nadir.png', format='png', bbox_inches='tight', dpi=300)
plt.show(block=False)


dataRPzGAL2 = data[(data[:, 1] == 2) & (np.isin(data[:, 4], gf.gnssbl23['GAL2']) & (data[:, 4] != 214) & (data[:, 4] != 218))]

fig, ax = plt.subplots(figsize=(6, 4))
ax.plot(dataRPzGAL2[:, 10], dataRPzGAL2[:, 5] * 100, label='Zenith antenna', color='blue', linestyle='none', marker='.', markersize=1)
ax.set_xlabel(r'Nadir Angle $(\mathrm{°})$')
ax.set_ylabel(r'Residuals $(\mathrm{cm})$')
ax.grid(True, linestyle=':', alpha=0.6, color='gray')
ax.legend(loc='upper right')
ax.set_ylim(-6, +6)
plt.tight_layout()
if save_plots: plt.savefig('output/res_plot_blk_GAL2_nadir_angle_woE14E18_zenit.png', format='png', bbox_inches='tight', dpi=300)
plt.show(block=False)

fig, ax = plt.subplots(figsize=(6, 4))
ax.plot(dataRPzGAL2[:, 8], dataRPzGAL2[:, 5] * 100, label='Zenith antenna', color='blue', linestyle='none', marker='.', markersize=1)
ax.set_xlabel(r'Elevation $(\mathrm{°})$')
ax.set_ylabel(r'Residuals $(\mathrm{cm})$')
ax.grid(True, linestyle=':', alpha=0.6, color='gray')
ax.legend(loc='upper right')
ax.set_ylim(-6, +6)
plt.tight_layout()
if save_plots: plt.savefig('output/res_plot_blk_GAL2_elevation_woE14E18_zenit.png', format='png', bbox_inches='tight', dpi=300)
plt.show(block=False)


##################################################
## Blocks GAL1, IIF, IIR-A: Nadir Angle
print(' * '.rjust(14, ' ') + 'Blocks GAL1, IIF, IIR-A: Nadir Angle')

dataRPnGAL1 = data[(data[:, 1] == 1) & (np.isin(data[:, 4], gf.gnssbl23['GAL1']))]

fig, ax = plt.subplots(figsize=(6, 4))
ax.plot(dataRPnGAL1[:, 10], dataRPnGAL1[:, 5] * 100, label='Nadir antenna', color='red', linestyle='none', marker='.', markersize=1)
ax.set_xlabel(r'Nadir Angle $(\mathrm{°})$')
ax.set_ylabel(r'Residuals $(\mathrm{cm})$')
ax.grid(True, linestyle=':', alpha=0.6, color='gray')
ax.legend(loc='upper right')
ax.set_ylim(-6, +6)
plt.tight_layout()
if save_plots: plt.savefig('output/res_plot_blk_GAL1_nadir_angle_nadir.png', format='png', bbox_inches='tight', dpi=300)
plt.show(block=False)

dataRPzGAL1 = data[(data[:, 1] == 2) & (np.isin(data[:, 4], gf.gnssbl23['GAL1']))]

fig, ax = plt.subplots(figsize=(6, 4))
ax.plot(dataRPzGAL1[:, 10], dataRPzGAL1[:, 5] * 100, label='Zenith antenna', color='blue', linestyle='none', marker='.', markersize=1)
ax.set_xlabel(r'Nadir Angle $(\mathrm{°})$')
ax.set_ylabel(r'Residuals $(\mathrm{cm})$')
ax.grid(True, linestyle=':', alpha=0.6, color='gray')
ax.legend(loc='upper right')
ax.set_ylim(-6, +6)
plt.tight_layout()
if save_plots: plt.savefig('output/res_plot_blk_GAL1_nadir_angle_zenit.png', format='png', bbox_inches='tight', dpi=300)
plt.show(block=False)


dataRPnIIF = data[(data[:, 1] == 1) & (np.isin(data[:, 4], gf.gnssbl23['IIF']))]

fig, ax = plt.subplots(figsize=(6, 4))
ax.plot(dataRPnIIF[:, 10], dataRPnIIF[:, 5] * 100, label='Nadir antenna', color='red', linestyle='none', marker='.', markersize=1)
ax.set_xlabel(r'Nadir Angle $(\mathrm{°})$')
ax.set_ylabel(r'Residuals $(\mathrm{cm})$')
ax.grid(True, linestyle=':', alpha=0.6, color='gray')
ax.legend(loc='upper right')
ax.set_ylim(-6, +6)
plt.tight_layout()
if save_plots: plt.savefig('output/res_plot_blk_IIF_nadir_angle_nadir.png', format='png', bbox_inches='tight', dpi=300)
plt.show(block=False)

dataRPzIIF = data[(data[:, 1] == 2) & (np.isin(data[:, 4], gf.gnssbl23['IIF']))]

fig, ax = plt.subplots(figsize=(6, 4))
ax.plot(dataRPzIIF[:, 10], dataRPzIIF[:, 5] * 100, label='Zenith antenna', color='blue', linestyle='none', marker='.', markersize=1)
ax.set_xlabel(r'Nadir Angle $(\mathrm{°})$')
ax.set_ylabel(r'Residuals $(\mathrm{cm})$')
ax.grid(True, linestyle=':', alpha=0.6, color='gray')
ax.legend(loc='upper right')
ax.set_ylim(-6, +6)
plt.tight_layout()
if save_plots: plt.savefig('output/res_plot_blk_IIF_nadir_angle_zenit.png', format='png', bbox_inches='tight', dpi=300)
plt.show(block=False)


dataRPnIIR_A = data[(data[:, 1] == 1) & (np.isin(data[:, 4], gf.gnssbl23['IIR-A']))]

fig, ax = plt.subplots(figsize=(6, 4))
ax.plot(dataRPnIIR_A[:, 10], dataRPnIIR_A[:, 5] * 100, label='Nadir antenna', color='red', linestyle='none', marker='.', markersize=1)
ax.set_xlabel(r'Nadir Angle $(\mathrm{°})$')
ax.set_ylabel(r'Residuals $(\mathrm{cm})$')
ax.grid(True, linestyle=':', alpha=0.6, color='gray')
ax.legend(loc='upper right')
ax.set_ylim(-6, +6)
plt.tight_layout()
if save_plots: plt.savefig('output/res_plot_blk_IIR-A_nadir_angle_nadir.png', format='png', bbox_inches='tight', dpi=300)
plt.show(block=False)

dataRPzIIR_A = data[(data[:, 1] == 2) & (np.isin(data[:, 4], gf.gnssbl23['IIR-A']))]

fig, ax = plt.subplots(figsize=(6, 4))
ax.plot(dataRPzIIR_A[:, 10], dataRPzIIR_A[:, 5] * 100, label='Zenith antenna', color='blue', linestyle='none', marker='.', markersize=1)
ax.set_xlabel(r'Nadir Angle $(\mathrm{°})$')
ax.set_ylabel(r'Residuals $(\mathrm{cm})$')
ax.grid(True, linestyle=':', alpha=0.6, color='gray')
ax.legend(loc='upper right')
ax.set_ylim(-6, +6)
plt.tight_layout()
if save_plots: plt.savefig('output/res_plot_blk_IIR-A_nadir_angle_zenit.png', format='png', bbox_inches='tight', dpi=300)
plt.show(block=False)


####################################################################################################
## SD-Plots and the fitted function
print('\n' + ' - '.rjust(10, ' ') + 'SD-Plots and the fitted function')

##################################################
## Block GAL2: Nadir Angle with single Satellites
print(' * '.rjust(14, ' ') + 'Block GAL2: Nadir Angle with single Satellites')

dataSPnGAL2 = gf.binning_1d(data[(data[:, 1] == 1) & (np.isin(data[:, 4], gf.gnssbl23['GAL2'])) & (data[:, 4] != 214) & (data[:, 4] != 218)], (10, 5), 1)
dataSPnE14 = gf.binning_1d(data[(data[:, 1] == 1) & (data[:, 4] == 214)], (10, 5), 1)
dataSPnE18 = gf.binning_1d(data[(data[:, 1] == 1) & (data[:, 4] == 218)], (10, 5), 1)

fig, ax = plt.subplots(figsize=(6, 4))
ax.plot(dataSPnGAL2[0], np.array([(np.std(v) * 100) for v in dataSPnGAL2[1]]), label='Nadir antenna', color='red', linestyle='-', marker='.', markersize=3)
ax.plot(dataSPnE14[0], np.array([(np.std(v) * 100) for v in dataSPnE14[1]]), label='Satellite E14', color='darkred', linestyle='-', marker='.', markersize=3)
ax.plot(dataSPnE18[0], np.array([(np.std(v) * 100) for v in dataSPnE18[1]]), label='Satellite E18', color='tomato', linestyle='-', marker='.', markersize=3)
ax.set_xlabel(r'Nadir Angle $(\mathrm{°})$')
ax.set_ylabel(r'SD of Residuals $(\mathrm{cm})$')
ax.grid(True, linestyle=':', alpha=0.6, color='gray')
ax.legend(loc='upper right')
ax.set_ylim(0.15, +2)
plt.tight_layout()
if save_plots: plt.savefig('output/std_plot_blk_GAL2_Sat_nadir_angle_nadir.png', format='png', bbox_inches='tight', dpi=300)
plt.show(block=False)


dataSPzGAL2 = gf.binning_1d(data[(data[:, 1] == 2) & (np.isin(data[:, 4], gf.gnssbl23['GAL2'])) & (data[:, 4] != 214) & (data[:, 4] != 218)], (10, 5), 1)
dataSPzE14 = gf.binning_1d(data[(data[:, 1] == 2) & (data[:, 4] == 214)], (10, 5), 1)
dataSPzE18 = gf.binning_1d(data[(data[:, 1] == 2) & (data[:, 4] == 218)], (10, 5), 1)

fig, ax = plt.subplots(figsize=(6, 4))
ax.plot(dataSPzGAL2[0], np.array([(np.std(v) * 100) for v in dataSPzGAL2[1]]), label='Zenith antenna', color='blue', linestyle='-', marker='.', markersize=3)
ax.plot(dataSPzE14[0], np.array([(np.std(v) * 100) for v in dataSPzE14[1]]), label='Satellite E14', color='darkblue', linestyle='-', marker='.', markersize=3)
ax.plot(dataSPzE18[0], np.array([(np.std(v) * 100) for v in dataSPzE18[1]]), label='Satellite E18', color='lightblue', linestyle='-', marker='.', markersize=3)
ax.set_xlabel(r'Nadir Angle $(\mathrm{°})$')
ax.set_ylabel(r'SD of Residuals $(\mathrm{cm})$')
ax.grid(True, linestyle=':', alpha=0.6, color='gray')
ax.legend(loc='upper right')
ax.set_ylim(0.15, +2)
plt.tight_layout()
if save_plots: plt.savefig('output/std_plot_blk_GAL2_Sat_nadir_angle_zenit.png', format='png', bbox_inches='tight', dpi=300)
plt.show(block=False)


##################################################
## Blocks IIR-A, IIR-B, IIR-M, IIF, IIIA, GAL1, GAL2: Values of Nadir Angle
print(' * '.rjust(14, ' ') + 'Blocks IIR-A, IIR-B, IIR-M, IIF, IIIA, GAL1, GAL2: Values of Nadir Angle')

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

blkResults = {} # [[Nadir], [Zenith]]

for key in gf.gnssbl23: # without the Satellites E14 and E18
    dataSPn = gf.binning_1d(data[(data[:, 1] == 1) & (np.isin(data[:, 4], gf.gnssbl23[key])) & (data[:, 4] != 214) & (data[:, 4] != 218)], (10, 5), 1)
    dataSPn_FIT = gf.fitting_exp(blkPara[key][0], np.array([np.std(v) for v in dataSPn[1]]), dataSPn[0], np.array([len(v) for v in dataSPn[1]]) if blkPmat[key][0] == True else None)
    dataSPz = gf.binning_1d(data[(data[:, 1] == 2) & (np.isin(data[:, 4], gf.gnssbl23[key])) & (data[:, 4] != 214) & (data[:, 4] != 218)], (10, 5), 1)
    dataSPz_FIT = gf.fitting_exp(blkPara[key][1], np.array([np.std(v) for v in dataSPz[1]]), dataSPz[0], np.array([len(v) for v in dataSPz[1]]) if blkPmat[key][1] == True else None)
    blkResults[key] = [[dataSPn_FIT[0], dataSPn_FIT[1]], [dataSPz_FIT[0], dataSPz_FIT[1]]]


with open("output/data_save_dict.txt", "w", encoding="utf-8") as datei:
    for schluessel, wert in blkPara.items():
        datei.write(f"{schluessel}: {wert}\n")
    datei.write('\n')
    for schluessel, wert in blkPmat.items():
        datei.write(f"{schluessel}: {wert}\n")
    datei.write('\n')
    for schluessel, wert in blkResults.items():
        datei.write(f"{schluessel}: {wert}\n")


with open('output/data_fitting_nadir_angle.txt', 'w') as file:
    file.write('FITTING Nadir Angle of GNSS Blocks\n')
    file.write('Modelfunction: f(x) = d + A e^(b x)\n')
    file.write('Parameters: A, b, d\n')
    file.write('\n')
    header = ['Blocks', 'Antenna', 'A (m)', 'b (1/°)', 'd (m)', 'RMS (m)']
    file.write(f'{header[0]:<10}{header[1]:<10}' + ''.join(f'{h:>15}' for h in header[2:]) + '\n')
    file.write('-' * 80 + '\n')

    for key, value in blkResults.items():
        for antenna, (para, Pmat) in zip(['Nadir', 'Zenith'], value):
            file.write(f'{key:<10}{antenna:<10}' + ''.join(f'{p:15.6e}' for p in para) + f'{Pmat:15.6f}\n')


rms_table = {'Blocks' : [], 
             'Nadir antenna' : [], 
             'Zenith antenna' : []}

for key, value in blkResults.items():
    rms_table['Blocks'].append(key)
    rms_table['Nadir antenna'].append(value[0][1])
    rms_table['Zenith antenna'].append(value[1][1])

rms_table = pd.DataFrame(rms_table)
rms_table.to_csv('output/data_rms_STD_nadir_angle.csv', sep=';', index=False, encoding='utf-8')


##################################################
## Appendix: Modelfunction Nadir Angle
print(' * '.rjust(14, ' ') + 'Appendix: Modelfunction Nadir Angle')

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

para = ['IIR-A', 'IIR-B', 'IIR-M', 'IIF', 'IIIA', 'GAL1', 'GAL2']

fig, ax = plt.subplots(figsize=(6, 4))
for key, value in parameters.items():
    x_data = np.arange(0, value[0], 0.01)
    ax.plot(x_data, gf.modelfunction(x_data, value[1], value[2], value[3]) * 100, label=key, linestyle='-', marker='none')
ax.set_xlabel(r'Nadir Angle $(\mathrm{°})$')
ax.set_ylabel(r'SD of Residuals $(\mathrm{cm})$')
ax.grid(True, linestyle=':', alpha=0.6, color='gray')
ax.legend(loc='upper left')
plt.tight_layout()
if save_plots: plt.savefig('output/appendix/std_plot_blk_all_nadir_angle.png', format='png', bbox_inches='tight', dpi=300)
plt.show(block=False)

for i in range(len(para)):
    fig, ax = plt.subplots(figsize=(6, 4))
    keyn = para[i] + ' Nadir'
    x_datan = np.arange(0, parameters[keyn][0], 0.01)
    ax.plot(x_datan, gf.modelfunction(x_datan, parameters[keyn][1], parameters[keyn][2], parameters[keyn][3]) * 100, label=keyn, linestyle='-', marker='none', color='red')
    keyz = para[i] + ' Zenith'
    x_dataz = np.arange(0, parameters[keyz][0], 0.01)
    ax.plot(x_dataz, gf.modelfunction(x_dataz, parameters[keyz][1], parameters[keyz][2], parameters[keyz][3]) * 100, label=keyz, linestyle='-', marker='none', color='blue')
    ax.set_xlabel(r'Nadir Angle $(\mathrm{°})$')
    ax.set_ylabel(r'SD of Residuals $(\mathrm{cm})$')
    ax.grid(True, linestyle=':', alpha=0.6, color='gray')
    ax.legend(loc='upper right')
    plt.tight_layout()
    if save_plots: plt.savefig(f'output/appendix/std_plot_blk_{para[i]}_nadir_angle.png', format='png', bbox_inches='tight', dpi=300)
    plt.show(block=False)


##################################################
## Block GAL1: Elevation, Nadir Angle
print(' * '.rjust(14, ' ') + 'Block GAL1: Elevation, Nadir Angle')

dataSPnGAL1_ELE = gf.binning_1d(data[(data[:, 1] == 1) & (np.isin(data[:, 4], gf.gnssbl23['GAL1']))], (8, 5), 1)
dataSPnGAL1_ELE_FIT = gf.fitting_exp([2, -0.15, 0.0035], np.array([np.std(v) for v in dataSPnGAL1_ELE[1]]), dataSPnGAL1_ELE[0])

fig, ax = plt.subplots(figsize=(6, 4))
ax.plot(dataSPnGAL1_ELE[0], np.array([(np.std(v) * 100) for v in dataSPnGAL1_ELE[1]]), label='Nadir antenna', color='red', linestyle='-', marker='.', markersize=3)
ax.plot(np.arange(np.min(dataSPnGAL1_ELE[0]), np.max(dataSPnGAL1_ELE[0]) + 0.01, 0.01), gf.modelfunction(np.arange(np.min(dataSPnGAL1_ELE[0]), np.max(dataSPnGAL1_ELE[0]) + 0.01, 0.01), *dataSPnGAL1_ELE_FIT[0]) * 100, label='Modelfunction\nRMS = ' + f"${f'{dataSPnGAL1_ELE_FIT[1]:.3e}'.split('e')[0]} \\times 10^{{{int(f'{dataSPnGAL1_ELE_FIT[1] * 100:.3e}'.split('e')[1])}}}$" + r" $\mathrm{cm}$", color='black', linestyle='-', marker='none')
ax.set_xlabel(r'Elevation $(\mathrm{°})$')
ax.set_ylabel(r'SD of Residuals $(\mathrm{cm})$')
ax.grid(True, linestyle=':', alpha=0.6, color='gray')
ax.legend(loc='upper right')
ax.set_ylim(0.15, +1.6)
plt.tight_layout()
if save_plots: plt.savefig('output/std_plot_blk_GAL1_elevation_nadir.png', format='png', bbox_inches='tight', dpi=300)
plt.show(block=False)

dataSPnGAL1 = gf.binning_1d(data[(data[:, 1] == 1) & (np.isin(data[:, 4], gf.gnssbl23['GAL1']))], (10, 5), 1)
dataSPnGAL1_FIT = gf.fitting_exp([0.000005, 0.35, 0.003], np.array([np.std(v) for v in dataSPnGAL1[1]]), dataSPnGAL1[0])

fig, ax = plt.subplots(figsize=(6, 4))
ax.plot(dataSPnGAL1[0], np.array([(np.std(v) * 100) for v in dataSPnGAL1[1]]), label='Nadir antenna', color='red', linestyle='-', marker='.', markersize=3)
ax.plot(np.arange(np.min(dataSPnGAL1[0]), np.max(dataSPnGAL1[0]) + 0.01, 0.01), gf.modelfunction(np.arange(np.min(dataSPnGAL1[0]), np.max(dataSPnGAL1[0]) + 0.01, 0.01), *dataSPnGAL1_FIT[0]) * 100, label='Modelfunction\nRMS = ' + f"${f'{dataSPnGAL1_FIT[1]:.3e}'.split('e')[0]} \\times 10^{{{int(f'{dataSPnGAL1_FIT[1] * 100:.3e}'.split('e')[1])}}}$" + r" $\mathrm{cm}$", color='black', linestyle='-', marker='none')
ax.set_xlabel(r'Nadir Angle $(\mathrm{°})$')
ax.set_ylabel(r'SD of Residuals $(\mathrm{cm})$')
ax.grid(True, linestyle=':', alpha=0.6, color='gray')
ax.legend(loc='upper right')
ax.set_ylim(0.15, +1.6)
plt.tight_layout()
if save_plots: plt.savefig('output/std_plot_blk_GAL1_nadir_angle_nadir.png', format='png', bbox_inches='tight', dpi=300)
plt.show(block=False)


dataSPzGAL1_ELE = gf.binning_1d(data[(data[:, 1] == 2) & (np.isin(data[:, 4], gf.gnssbl23['GAL1']))], (8, 5), 1)
dataSPzGAL1_ELE_FIT = gf.fitting_exp([2, -0.15, 0.0035], np.array([np.std(v) for v in dataSPzGAL1_ELE[1]]), dataSPzGAL1_ELE[0])

fig, ax = plt.subplots(figsize=(6, 4))
ax.plot(dataSPzGAL1_ELE[0], np.array([(np.std(v) * 100) for v in dataSPzGAL1_ELE[1]]), label='Zenith antenna', color='blue', linestyle='-', marker='.', markersize=3)
ax.plot(np.arange(np.min(dataSPzGAL1_ELE[0]), np.max(dataSPzGAL1_ELE[0]) + 0.01, 0.01), gf.modelfunction(np.arange(np.min(dataSPzGAL1_ELE[0]), np.max(dataSPzGAL1_ELE[0]) + 0.01, 0.01), *dataSPzGAL1_ELE_FIT[0]) * 100, label='Modelfunction\nRMS = ' + f"${f'{dataSPzGAL1_ELE_FIT[1]:.3e}'.split('e')[0]} \\times 10^{{{int(f'{dataSPzGAL1_ELE_FIT[1] * 100:.3e}'.split('e')[1])}}}$" + r" $\mathrm{cm}$", color='black', linestyle='-', marker='none')
ax.set_xlabel(r'Elevation $(\mathrm{°})$')
ax.set_ylabel(r'SD of Residuals $(\mathrm{cm})$')
ax.grid(True, linestyle=':', alpha=0.6, color='gray')
ax.legend(loc='upper right')
ax.set_ylim(0.15, +1.6)
plt.tight_layout()
if save_plots: plt.savefig('output/std_plot_blk_GAL1_elevation_zenit.png', format='png', bbox_inches='tight', dpi=300)
plt.show(block=False)

dataSPzGAL1 = gf.binning_1d(data[(data[:, 1] == 2) & (np.isin(data[:, 4], gf.gnssbl23['GAL1']))], (10, 5), 1)
dataSPzGAL1_FIT = gf.fitting_exp([0.000005, 0.35, 0.003], np.array([np.std(v) for v in dataSPzGAL1[1]]), dataSPzGAL1[0])

fig, ax = plt.subplots(figsize=(6, 4))
ax.plot(dataSPzGAL1[0], np.array([(np.std(v) * 100) for v in dataSPzGAL1[1]]), label='Zenith antenna', color='blue', linestyle='-', marker='.', markersize=3)
ax.plot(np.arange(np.min(dataSPzGAL1[0]), np.max(dataSPzGAL1[0]) + 0.01, 0.01), gf.modelfunction(np.arange(np.min(dataSPzGAL1[0]), np.max(dataSPzGAL1[0]) + 0.01, 0.01), *dataSPzGAL1_FIT[0]) * 100, label='Modelfunction\nRMS = ' + f"${f'{dataSPzGAL1_FIT[1]:.3e}'.split('e')[0]} \\times 10^{{{int(f'{dataSPzGAL1_FIT[1] * 100:.3e}'.split('e')[1])}}}$" + r" $\mathrm{cm}$", color='black', linestyle='-', marker='none')
ax.set_xlabel(r'Nadir Angle $(\mathrm{°})$')
ax.set_ylabel(r'SD of Residuals $(\mathrm{cm})$')
ax.grid(True, linestyle=':', alpha=0.6, color='gray')
ax.legend(loc='upper right')
ax.set_ylim(0.15, +1.6)
plt.tight_layout()
if save_plots: plt.savefig('output/std_plot_blk_GAL1_nadir_angle_zenit.png', format='png', bbox_inches='tight', dpi=300)
plt.show(block=False)

blkResults_ELE = {}
blkResults_ELE['GAL1'] = [[dataSPnGAL1_ELE_FIT[0], dataSPnGAL1_ELE_FIT[1]], [dataSPzGAL1_ELE_FIT[0], dataSPzGAL1_ELE_FIT[1]]]

with open('output/data_fitting_elevation.txt', 'w') as file:
    file.write('FITTING Elevation of GNSS Blocks\n')
    file.write('Modelfunction: f(x) = d + A e^(b x)\n')
    file.write('Parameters: A, b, d\n')
    file.write('\n')
    header = ['Blocks', 'Antenna', 'A (m)', 'b (1/°)', 'd (m)', 'RMS (m)']
    file.write(f'{header[0]:<10}{header[1]:<10}' + ''.join(f'{h:>15}' for h in header[2:]) + '\n')
    file.write('-' * 80 + '\n')

    for key, value in blkResults_ELE.items():
        for antenna, (para, Pmat) in zip(['Nadir', 'Zenith'], value):
            file.write(f'{key:<10}{antenna:<10}' + ''.join(f'{p:15.6e}' for p in para) + f'{Pmat:15.6f}\n')


##################################################
## Blocks GAL2 (without the Satellites E14 and E18), IIF, IIR-A: Nadir Angle
print(' * '.rjust(14, ' ') + 'Blocks GAL2 (without the Satellites E14 and E18), IIF, IIR-A: Nadir Angle')

dataSPnGAL2 = gf.binning_1d(data[(data[:, 1] == 1) & (np.isin(data[:, 4], gf.gnssbl23['GAL2'])) & (data[:, 4] != 214) & (data[:, 4] != 218)], (10, 5), 1)
dataSPnGAL2_FIT = gf.fitting_exp([0.000005, 0.35, 0.003], np.array([np.std(v) for v in dataSPnGAL2[1]]), dataSPnGAL2[0])

fig, ax = plt.subplots(figsize=(6, 4))
ax.plot(dataSPnGAL2[0], np.array([(np.std(v) * 100) for v in dataSPnGAL2[1]]), label='Nadir antenna', color='red', linestyle='-', marker='.', markersize=3)
ax.plot(np.arange(np.min(dataSPnGAL2[0]), np.max(dataSPnGAL2[0]) + 0.01, 0.01), gf.modelfunction(np.arange(np.min(dataSPnGAL2[0]), np.max(dataSPnGAL2[0]) + 0.01, 0.01), *dataSPnGAL2_FIT[0]) * 100, label='Modelfunction\nRMS = ' + f"${f'{dataSPnGAL2_FIT[1]:.3e}'.split('e')[0]} \\times 10^{{{int(f'{dataSPnGAL2_FIT[1] * 100:.3e}'.split('e')[1])}}}$" + r" $\mathrm{cm}$", color='black', linestyle='-', marker='none')
ax.set_xlabel(r'Nadir Angle $(\mathrm{°})$')
ax.set_ylabel(r'SD of Residuals $(\mathrm{cm})$')
ax.grid(True, linestyle=':', alpha=0.6, color='gray')
ax.legend(loc='upper right')
ax.set_ylim(0.15, +1.6)
plt.tight_layout()
if save_plots: plt.savefig('output/std_plot_blk_GAL2_nadir_angle_nadir.png', format='png', bbox_inches='tight', dpi=300)
plt.show(block=False)

dataSPzGAL2 = gf.binning_1d(data[(data[:, 1] == 2) & (np.isin(data[:, 4], gf.gnssbl23['GAL2'])) & (data[:, 4] != 214) & (data[:, 4] != 218)], (10, 5), 1)
dataSPzGAL2_FIT = gf.fitting_exp([0.000003, 0.35, 0.003], np.array([np.std(v) for v in dataSPzGAL2[1]]), dataSPzGAL2[0])

fig, ax = plt.subplots(figsize=(6, 4))
ax.plot(dataSPzGAL2[0], np.array([(np.std(v) * 100) for v in dataSPzGAL2[1]]), label='Zenith antenna', color='blue', linestyle='-', marker='.', markersize=3)
ax.plot(np.arange(np.min(dataSPzGAL2[0]), np.max(dataSPzGAL2[0]) + 0.01, 0.01), gf.modelfunction(np.arange(np.min(dataSPzGAL2[0]), np.max(dataSPzGAL2[0]) + 0.01, 0.01), *dataSPzGAL2_FIT[0]) * 100, label='Modelfunction\nRMS = ' + f"${f'{dataSPzGAL2_FIT[1]:.3e}'.split('e')[0]} \\times 10^{{{int(f'{dataSPzGAL2_FIT[1] * 100:.3e}'.split('e')[1])}}}$" + r" $\mathrm{cm}$", color='black', linestyle='-', marker='none')
ax.set_xlabel(r'Nadir Angle $(\mathrm{°})$')
ax.set_ylabel(r'SD of Residuals $(\mathrm{cm})$')
ax.grid(True, linestyle=':', alpha=0.6, color='gray')
ax.legend(loc='upper right')
ax.set_ylim(0.15, +1.6)
plt.tight_layout()
if save_plots: plt.savefig('output/std_plot_blk_GAL2_nadir_angle_zenit.png', format='png', bbox_inches='tight', dpi=300)
plt.show(block=False)


dataSPnIIF = gf.binning_1d(data[(data[:, 1] == 1) & (np.isin(data[:, 4], gf.gnssbl23['IIF']))], (10, 5), 1)
dataSPnIIF_FIT = gf.fitting_exp([0.000005, 0.35, 0.003], np.array([np.std(v) for v in dataSPnIIF[1]]), dataSPnIIF[0])

fig, ax = plt.subplots(figsize=(6, 4))
ax.plot(dataSPnIIF[0], np.array([(np.std(v) * 100) for v in dataSPnIIF[1]]), label='Nadir antenna', color='red', linestyle='-', marker='.', markersize=3)
ax.plot(np.arange(np.min(dataSPnIIF[0]), np.max(dataSPnIIF[0]) + 0.01, 0.01), gf.modelfunction(np.arange(np.min(dataSPnIIF[0]), np.max(dataSPnIIF[0]) + 0.01, 0.01), *dataSPnIIF_FIT[0]) * 100, label='Modelfunction\nRMS = ' + f"${f'{dataSPnIIF_FIT[1]:.3e}'.split('e')[0]} \\times 10^{{{int(f'{dataSPnIIF_FIT[1] * 100:.3e}'.split('e')[1])}}}$" + r" $\mathrm{cm}$", color='black', linestyle='-', marker='none')
ax.set_xlabel(r'Nadir Angle $(\mathrm{°})$')
ax.set_ylabel(r'SD of Residuals $(\mathrm{cm})$')
ax.grid(True, linestyle=':', alpha=0.6, color='gray')
ax.legend(loc='upper right')
ax.set_ylim(0.15, +1.6)
plt.tight_layout()
if save_plots: plt.savefig('output/std_plot_blk_IIF_nadir_angle_nadir.png', format='png', bbox_inches='tight', dpi=300)
plt.show(block=False)

dataSPzIIF = gf.binning_1d(data[(data[:, 1] == 2) & (np.isin(data[:, 4], gf.gnssbl23['IIF']))], (10, 5), 1)
dataSPzIIF_FIT = gf.fitting_exp([0.000005, 0.35, 0.003], np.array([np.std(v) for v in dataSPzIIF[1]]), dataSPzIIF[0])

fig, ax = plt.subplots(figsize=(6, 4))
ax.plot(dataSPzIIF[0], np.array([(np.std(v) * 100) for v in dataSPzIIF[1]]), label='Zenith antenna', color='blue', linestyle='-', marker='.', markersize=3)
ax.plot(np.arange(np.min(dataSPzIIF[0]), np.max(dataSPzIIF[0]) + 0.01, 0.01), gf.modelfunction(np.arange(np.min(dataSPzIIF[0]), np.max(dataSPzIIF[0]) + 0.01, 0.01), *dataSPzIIF_FIT[0]) * 100, label='Modelfunction\nRMS = ' + f"${f'{dataSPzIIF_FIT[1]:.3e}'.split('e')[0]} \\times 10^{{{int(f'{dataSPzIIF_FIT[1] * 100:.3e}'.split('e')[1])}}}$" + r" $\mathrm{cm}$", color='black', linestyle='-', marker='none')
ax.set_xlabel(r'Nadir Angle $(\mathrm{°})$')
ax.set_ylabel(r'SD of Residuals $(\mathrm{cm})$')
ax.grid(True, linestyle=':', alpha=0.6, color='gray')
ax.legend(loc='upper right')
ax.set_ylim(0.15, +1.6)
plt.tight_layout()
if save_plots: plt.savefig('output/std_plot_blk_IIF_nadir_angle_zenit.png', format='png', bbox_inches='tight', dpi=300)
plt.show(block=False)


dataSPnIIR_A = gf.binning_1d(data[(data[:, 1] == 1) & (np.isin(data[:, 4], gf.gnssbl23['IIR-A']))], (10, 5), 1)
dataSPnIIR_A_FIT = gf.fitting_exp([8.0e-5, 0.25, 0.0044], np.array([np.std(v) for v in dataSPnIIR_A[1]]), dataSPnIIR_A[0], np.array([len(v) for v in dataSPnIIR_A[1]]))

fig, ax = plt.subplots(figsize=(6, 4))
ax.plot(dataSPnIIR_A[0], np.array([(np.std(v) * 100) for v in dataSPnIIR_A[1]]), label='Nadir antenna', color='red', linestyle='-', marker='.', markersize=3)
ax.plot(np.arange(np.min(dataSPnIIR_A[0]), np.max(dataSPnIIR_A[0]) + 0.01, 0.01), gf.modelfunction(np.arange(np.min(dataSPnIIR_A[0]), np.max(dataSPnIIR_A[0]) + 0.01, 0.01), *dataSPnIIR_A_FIT[0]) * 100, label='Modelfunction\nRMS = ' + f"${f'{dataSPnIIR_A_FIT[1]:.3e}'.split('e')[0]} \\times 10^{{{int(f'{dataSPnIIR_A_FIT[1] * 100:.3e}'.split('e')[1])}}}$" + r" $\mathrm{cm}$", color='black', linestyle='-', marker='none')
ax.set_xlabel(r'Nadir Angle $(\mathrm{°})$')
ax.set_ylabel(r'SD of Residuals $(\mathrm{cm})$')
ax.grid(True, linestyle=':', alpha=0.6, color='gray')
ax.legend(loc='upper right')
ax.set_ylim(0.15, +1.6)
plt.tight_layout()
if save_plots: plt.savefig('output/std_plot_blk_IIR-A_nadir_angle_nadir.png', format='png', bbox_inches='tight', dpi=300)
plt.show(block=False)

dataSPzIIR_A = gf.binning_1d(data[(data[:, 1] == 2) & (np.isin(data[:, 4], gf.gnssbl23['IIR-A']))], (10, 5), 1)
dataSPzIIR_A_FIT = gf.fitting_exp([0.000005, 0.35, 0.003], np.array([np.std(v) for v in dataSPzIIR_A[1]]), dataSPzIIR_A[0])

fig, ax = plt.subplots(figsize=(6, 4))
ax.plot(dataSPzIIR_A[0], np.array([(np.std(v) * 100) for v in dataSPzIIR_A[1]]), label='Zenith antenna', color='blue', linestyle='-', marker='.', markersize=3)
ax.plot(np.arange(np.min(dataSPzIIR_A[0]), np.max(dataSPzIIR_A[0]) + 0.01, 0.01), gf.modelfunction(np.arange(np.min(dataSPzIIR_A[0]), np.max(dataSPzIIR_A[0]) + 0.01, 0.01), *dataSPzIIR_A_FIT[0]) * 100, label='Modelfunction\nRMS = ' + f"${f'{dataSPzIIR_A_FIT[1]:.3e}'.split('e')[0]} \\times 10^{{{int(f'{dataSPzIIR_A_FIT[1] * 100:.3e}'.split('e')[1])}}}$" + r" $\mathrm{cm}$", color='black', linestyle='-', marker='none')
ax.set_xlabel(r'Nadir Angle $(\mathrm{°})$')
ax.set_ylabel(r'SD of Residuals $(\mathrm{cm})$')
ax.grid(True, linestyle=':', alpha=0.6, color='gray')
ax.legend(loc='upper right')
ax.set_ylim(0.15, +1.6)
plt.tight_layout()
if save_plots: plt.savefig('output/std_plot_blk_IIR-A_nadir_angle_zenit.png', format='png', bbox_inches='tight', dpi=300)
plt.show(block=False)


##################################################
## Appendix: Blocks IIR-B, IIR-M, IIIA: Nadir Angle
print(' * '.rjust(14, ' ') + 'Appendix: Blocks IIR-B, IIR-M, IIIA: Nadir Angle')

dataSPnIIR_B = gf.binning_1d(data[(data[:, 1] == 1) & (np.isin(data[:, 4], gf.gnssbl23['IIR-B']))], (10, 5), 1)
dataSPnIIR_B_FIT = gf.fitting_exp([0.000005, 0.35, 0.003], np.array([np.std(v) for v in dataSPnIIR_B[1]]), dataSPnIIR_B[0])

fig, ax = plt.subplots(figsize=(6, 4))
ax.plot(dataSPnIIR_B[0], np.array([(np.std(v) * 100) for v in dataSPnIIR_B[1]]), label='Nadir antenna', color='red', linestyle='-', marker='.', markersize=3)
ax.plot(np.arange(np.min(dataSPnIIR_B[0]), np.max(dataSPnIIR_B[0]) + 0.01, 0.01), gf.modelfunction(np.arange(np.min(dataSPnIIR_B[0]), np.max(dataSPnIIR_B[0]) + 0.01, 0.01), *dataSPnIIR_B_FIT[0]) * 100, label='Modelfunction\nRMS = ' + f"${f'{dataSPnIIR_B_FIT[1]:.3e}'.split('e')[0]} \\times 10^{{{int(f'{dataSPnIIR_B_FIT[1] * 100:.3e}'.split('e')[1])}}}$" + r" $\mathrm{cm}$", color='black', linestyle='-', marker='none')
ax.set_xlabel(r'Nadir Angle $(\mathrm{°})$')
ax.set_ylabel(r'SD of Residuals $(\mathrm{cm})$')
ax.grid(True, linestyle=':', alpha=0.6, color='gray')
ax.legend(loc='upper right')
ax.set_ylim(0.15, +1.6)
plt.tight_layout()
if save_plots: plt.savefig('output/appendix/std_plot_blk_IIR-B_nadir_angle_nadir.png', format='png', bbox_inches='tight', dpi=300)
plt.show(block=False)

dataSPzIIR_B = gf.binning_1d(data[(data[:, 1] == 2) & (np.isin(data[:, 4], gf.gnssbl23['IIR-B']))], (10, 5), 1)
dataSPzIIR_B_FIT = gf.fitting_exp([0.000003, 0.35, 0.003], np.array([np.std(v) for v in dataSPzIIR_B[1]]), dataSPzIIR_B[0])

fig, ax = plt.subplots(figsize=(6, 4))
ax.plot(dataSPzIIR_B[0], np.array([(np.std(v) * 100) for v in dataSPzIIR_B[1]]), label='Zenith antenna', color='blue', linestyle='-', marker='.', markersize=3)
ax.plot(np.arange(np.min(dataSPzIIR_B[0]), np.max(dataSPzIIR_B[0]) + 0.01, 0.01), gf.modelfunction(np.arange(np.min(dataSPzIIR_B[0]), np.max(dataSPzIIR_B[0]) + 0.01, 0.01), *dataSPzIIR_B_FIT[0]) * 100, label='Modelfunction\nRMS = ' + f"${f'{dataSPzIIR_B_FIT[1]:.3e}'.split('e')[0]} \\times 10^{{{int(f'{dataSPzIIR_B_FIT[1] * 100:.3e}'.split('e')[1])}}}$" + r" $\mathrm{cm}$", color='black', linestyle='-', marker='none')
ax.set_xlabel(r'Nadir Angle $(\mathrm{°})$')
ax.set_ylabel(r'SD of Residuals $(\mathrm{cm})$')
ax.grid(True, linestyle=':', alpha=0.6, color='gray')
ax.legend(loc='upper right')
ax.set_ylim(0.15, +1.6)
plt.tight_layout()
if save_plots: plt.savefig('output/appendix/std_plot_blk_IIR-B_nadir_angle_zenit.png', format='png', bbox_inches='tight', dpi=300)
plt.show(block=False)


dataSPnIIR_M = gf.binning_1d(data[(data[:, 1] == 1) & (np.isin(data[:, 4], gf.gnssbl23['IIR-M']))], (10, 5), 1)
dataSPnIIR_M_FIT = gf.fitting_exp([0.0000025, 0.35, 0.003], np.array([np.std(v) for v in dataSPnIIR_M[1]]), dataSPnIIR_M[0])

fig, ax = plt.subplots(figsize=(6, 4))
ax.plot(dataSPnIIR_M[0], np.array([(np.std(v) * 100) for v in dataSPnIIR_M[1]]), label='Nadir antenna', color='red', linestyle='-', marker='.', markersize=3)
ax.plot(np.arange(np.min(dataSPnIIR_M[0]), np.max(dataSPnIIR_M[0]) + 0.01, 0.01), gf.modelfunction(np.arange(np.min(dataSPnIIR_M[0]), np.max(dataSPnIIR_M[0]) + 0.01, 0.01), *dataSPnIIR_M_FIT[0]) * 100, label='Modelfunction\nRMS = ' + f"${f'{dataSPnIIR_M_FIT[1]:.3e}'.split('e')[0]} \\times 10^{{{int(f'{dataSPnIIR_M_FIT[1] * 100:.3e}'.split('e')[1])}}}$" + r" $\mathrm{cm}$", color='black', linestyle='-', marker='none')
ax.set_xlabel(r'Nadir Angle $(\mathrm{°})$')
ax.set_ylabel(r'SD of Residuals $(\mathrm{cm})$')
ax.grid(True, linestyle=':', alpha=0.6, color='gray')
ax.legend(loc='upper right')
ax.set_ylim(0.15, +1.6)
plt.tight_layout()
if save_plots: plt.savefig('output/appendix/std_plot_blk_IIR-M_nadir_angle_nadir.png', format='png', bbox_inches='tight', dpi=300)
plt.show(block=False)

dataSPzIIR_M = gf.binning_1d(data[(data[:, 1] == 2) & (np.isin(data[:, 4], gf.gnssbl23['IIR-M']))], (10, 5), 1)
dataSPzIIR_M_FIT = gf.fitting_exp([0.000003, 0.35, 0.003], np.array([np.std(v) for v in dataSPzIIR_M[1]]), dataSPzIIR_M[0])

fig, ax = plt.subplots(figsize=(6, 4))
ax.plot(dataSPzIIR_M[0], np.array([(np.std(v) * 100) for v in dataSPzIIR_M[1]]), label='Zenith antenna', color='blue', linestyle='-', marker='.', markersize=3)
ax.plot(np.arange(np.min(dataSPzIIR_M[0]), np.max(dataSPzIIR_M[0]) + 0.01, 0.01), gf.modelfunction(np.arange(np.min(dataSPzIIR_M[0]), np.max(dataSPzIIR_M[0]) + 0.01, 0.01), *dataSPzIIR_M_FIT[0]) * 100, label='Modelfunction\nRMS = ' + f"${f'{dataSPzIIR_M_FIT[1]:.3e}'.split('e')[0]} \\times 10^{{{int(f'{dataSPzIIR_M_FIT[1] * 100:.3e}'.split('e')[1])}}}$" + r" $\mathrm{cm}$", color='black', linestyle='-', marker='none')
ax.set_xlabel(r'Nadir Angle $(\mathrm{°})$')
ax.set_ylabel(r'SD of Residuals $(\mathrm{cm})$')
ax.grid(True, linestyle=':', alpha=0.6, color='gray')
ax.legend(loc='upper right')
ax.set_ylim(0.15, +1.6)
plt.tight_layout()
if save_plots: plt.savefig('output/appendix/std_plot_blk_IIR-M_nadir_angle_zenit.png', format='png', bbox_inches='tight', dpi=300)
plt.show(block=False)


dataSPnIIIA = gf.binning_1d(data[(data[:, 1] == 1) & (np.isin(data[:, 4], gf.gnssbl23['IIIA']))], (10, 5), 1)
dataSPnIIIA_FIT = gf.fitting_exp([0.0000025, 0.35, 0.003], np.array([np.std(v) for v in dataSPnIIIA[1]]), dataSPnIIIA[0], np.array([len(v) for v in dataSPnIIIA[1]]))

fig, ax = plt.subplots(figsize=(6, 4))
ax.plot(dataSPnIIIA[0], np.array([(np.std(v) * 100) for v in dataSPnIIIA[1]]), label='Nadir antenna', color='red', linestyle='-', marker='.', markersize=3)
ax.plot(np.arange(np.min(dataSPnIIIA[0]), np.max(dataSPnIIIA[0]) + 0.01, 0.01), gf.modelfunction(np.arange(np.min(dataSPnIIIA[0]), np.max(dataSPnIIIA[0]) + 0.01, 0.01), *dataSPnIIIA_FIT[0]) * 100, label='Modelfunction\nRMS = ' + f"${f'{dataSPnIIIA_FIT[1]:.3e}'.split('e')[0]} \\times 10^{{{int(f'{dataSPnIIIA_FIT[1] * 100:.3e}'.split('e')[1])}}}$" + r" $\mathrm{cm}$", color='black', linestyle='-', marker='none')
ax.set_xlabel(r'Nadir Angle $(\mathrm{°})$')
ax.set_ylabel(r'SD of Residuals $(\mathrm{cm})$')
ax.grid(True, linestyle=':', alpha=0.6, color='gray')
ax.legend(loc='upper right')
ax.set_ylim(0.15, +1.6)
plt.tight_layout()
if save_plots: plt.savefig('output/appendix/std_plot_blk_IIIA_nadir_angle_nadir.png', format='png', bbox_inches='tight', dpi=300)
plt.show(block=False)

dataSPzIIIA = gf.binning_1d(data[(data[:, 1] == 2) & (np.isin(data[:, 4], gf.gnssbl23['IIIA']))], (10, 5), 1)
dataSPzIIIA_FIT = gf.fitting_exp([0.000003, 0.35, 0.003], np.array([np.std(v) for v in dataSPzIIIA[1]]), dataSPzIIIA[0])

fig, ax = plt.subplots(figsize=(6, 4))
ax.plot(dataSPzIIIA[0], np.array([(np.std(v) * 100) for v in dataSPzIIIA[1]]), label='Zenith antenna', color='blue', linestyle='-', marker='.', markersize=3)
ax.plot(np.arange(np.min(dataSPzIIIA[0]), np.max(dataSPzIIIA[0]) + 0.01, 0.01), gf.modelfunction(np.arange(np.min(dataSPzIIIA[0]), np.max(dataSPzIIIA[0]) + 0.01, 0.01), *dataSPzIIIA_FIT[0]) * 100, label='Modelfunction\nRMS = ' + f"${f'{dataSPzIIIA_FIT[1]:.3e}'.split('e')[0]} \\times 10^{{{int(f'{dataSPzIIIA_FIT[1] * 100:.3e}'.split('e')[1])}}}$" + r" $\mathrm{cm}$", color='black', linestyle='-', marker='none')
ax.set_xlabel(r'Nadir Angle $(\mathrm{°})$')
ax.set_ylabel(r'SD of Residuals $(\mathrm{cm})$')
ax.grid(True, linestyle=':', alpha=0.6, color='gray')
ax.legend(loc='upper right')
ax.set_ylim(0.15, +1.6)
plt.tight_layout()
if save_plots: plt.savefig('output/appendix/std_plot_blk_IIIA_nadir_angle_zenit.png', format='png', bbox_inches='tight', dpi=300)
plt.show(block=False)


####################################################################################################
## Distances-Plots and there SD-Plots
print('\n' + ' - '.rjust(10, ' ') + 'Distances-Plots and there SD-Plots')

##################################################
## Satellite 211 on Day 1
print(' * '.rjust(14, ' ') + 'Satellite 211 on Day 1')

dataDP211d1 = data[(data[:, 0] == 1) & (data[:, 4] == 211)]

fig, ax = plt.subplots(figsize=(6, 4))
ax.plot((dataDP211d1[dataDP211d1[:, 1] == 1][:, 3] - int(dataDP211d1[:, 3].min())) * 24, dataDP211d1[dataDP211d1[:, 1] == 1][:, 12], label='Nadir antenna', color='red', linestyle='none', marker='.', markersize=1)
ax.plot((dataDP211d1[dataDP211d1[:, 1] == 2][:, 3] - int(dataDP211d1[:, 3].min())) * 24, dataDP211d1[dataDP211d1[:, 1] == 2][:, 12], label='Zenith antenna', color='blue', linestyle='none', marker='.', markersize=1)
ax.set_xlabel(r'Epoch $(\mathrm{hours})$')
ax.set_ylabel(r'Distance $(\mathrm{km})$')
ax.grid(True, linestyle=':', alpha=0.6, color='gray')
ax.legend(loc='upper right')
plt.tight_layout()
if save_plots: plt.savefig('output/dist_plot_Sat211_d1.png', format='png', bbox_inches='tight', dpi=300)
plt.show(block=False)


##################################################
## Block GAL1: Distance
print(' * '.rjust(14, ' ') + 'Block GAL1: Distance')

dataDPnGAL1 = data[(data[:, 1] == 1) & (np.isin(data[:, 4], gf.gnssbl23['GAL1']))]
dataDPnGAL1_STD = gf.binning_1d(dataDPnGAL1, (12, 5), 1000)

fig, ax = plt.subplots(figsize=(6, 4))
ax.plot(dataDPnGAL1[:, 12], dataDPnGAL1[:, 5] * 100, label='Nadir antenna', color='red', linestyle='none', marker='.', markersize=1)
ax.set_xlabel(r'Distance $(\mathrm{km})$')
ax.set_ylabel(r'Residuals $(\mathrm{cm})$')
ax.grid(True, linestyle=':', alpha=0.6, color='gray')
ax.legend(loc='upper right')
ax.set_ylim(-5, +5)
plt.tight_layout()
if save_plots: plt.savefig('output/dist_plot_blk_GAL1_distance_nadir.png', format='png', bbox_inches='tight', dpi=300)
plt.show(block=False)

fig, ax = plt.subplots(figsize=(6, 4))
ax.plot(dataDPnGAL1_STD[0], np.array([(np.std(v) * 100) for v in dataDPnGAL1_STD[1]]), label='Nadir antenna', color='red', linestyle='-', marker='.', markersize=3)
ax.set_xlabel(r'Distance $(\mathrm{km})$')
ax.set_ylabel(r'SD of Residuals $(\mathrm{cm})$')
ax.grid(True, linestyle=':', alpha=0.6, color='gray')
ax.legend(loc='upper right')
ax.set_ylim(0.15, +1.6)
plt.tight_layout()
if save_plots: plt.savefig('output/dist_plot_blk_GAL1_distance_std_nadir.png', format='png', bbox_inches='tight', dpi=300)
plt.show(block=False)


dataDPzGAL1 = data[(data[:, 1] == 2) & (np.isin(data[:, 4], gf.gnssbl23['GAL1']))]
dataDPzGAL1_STD = gf.binning_1d(dataDPzGAL1, (12, 5), 1000)

fig, ax = plt.subplots(figsize=(6, 4))
ax.plot(dataDPzGAL1[:, 12], dataDPzGAL1[:, 5] * 100, label='Zenith antenna', color='blue', linestyle='none', marker='.', markersize=1)
ax.set_xlabel(r'Distance $(\mathrm{km})$')
ax.set_ylabel(r'Residuals $(\mathrm{cm})$')
ax.grid(True, linestyle=':', alpha=0.6, color='gray')
ax.legend(loc='upper right')
ax.set_ylim(-5, +5)
plt.tight_layout()
if save_plots: plt.savefig('output/dist_plot_blk_GAL1_distance_zenit.png', format='png', bbox_inches='tight', dpi=300)
plt.show(block=False)

fig, ax = plt.subplots(figsize=(6, 4))
ax.plot(dataDPzGAL1_STD[0], np.array([(np.std(v) * 100) for v in dataDPzGAL1_STD[1]]), label='Zenith antenna', color='blue', linestyle='-', marker='.', markersize=3)
ax.set_xlabel(r'Distance $(\mathrm{km})$')
ax.set_ylabel(r'SD of Residuals $(\mathrm{cm})$')
ax.grid(True, linestyle=':', alpha=0.6, color='gray')
ax.legend(loc='upper right')
ax.set_ylim(0.15, +1.6)
plt.tight_layout()
if save_plots: plt.savefig('output/dist_plot_blk_GAL1_distance_std_zenit.png', format='png', bbox_inches='tight', dpi=300)
plt.show(block=False)


##################################################
## Block IIF: Distance
print(' * '.rjust(14, ' ') + 'Block IIF: Distance')

dataDPnIIF = data[(data[:, 1] == 1) & (np.isin(data[:, 4], gf.gnssbl23['IIF']))]
dataDPnIIF_STD = gf.binning_1d(dataDPnIIF, (12, 5), 1000)

fig, ax = plt.subplots(figsize=(6, 4))
ax.plot(dataDPnIIF[:, 12], dataDPnIIF[:, 5] * 100, label='Nadir antenna', color='red', linestyle='none', marker='.', markersize=1)
ax.set_xlabel(r'Distance $(\mathrm{km})$')
ax.set_ylabel(r'Residuals $(\mathrm{cm})$')
ax.grid(True, linestyle=':', alpha=0.6, color='gray')
ax.legend(loc='upper right')
ax.set_ylim(-5, +5)
plt.tight_layout()
if save_plots: plt.savefig('output/dist_plot_blk_IIF_distance_nadir.png', format='png', bbox_inches='tight', dpi=300)
plt.show(block=False)

fig, ax = plt.subplots(figsize=(6, 4))
ax.plot(dataDPnIIF_STD[0], np.array([(np.std(v) * 100) for v in dataDPnIIF_STD[1]]), label='Nadir antenna', color='red', linestyle='-', marker='.', markersize=3)
ax.set_xlabel(r'Distance $(\mathrm{km})$')
ax.set_ylabel(r'SD of Residuals $(\mathrm{cm})$')
ax.grid(True, linestyle=':', alpha=0.6, color='gray')
ax.legend(loc='upper right')
ax.set_ylim(0.15, +1.6)
plt.tight_layout()
if save_plots: plt.savefig('output/dist_plot_blk_IIF_distance_std_nadir.png', format='png', bbox_inches='tight', dpi=300)
plt.show(block=False)


dataDPzIIF = data[(data[:, 1] == 2) & (np.isin(data[:, 4], gf.gnssbl23['IIF']))]
dataDPzIIF_STD = gf.binning_1d(dataDPzIIF, (12, 5), 1000)

fig, ax = plt.subplots(figsize=(6, 4))
ax.plot(dataDPzIIF[:, 12], dataDPzIIF[:, 5] * 100, label='Zenith antenna', color='blue', linestyle='none', marker='.', markersize=1)
ax.set_xlabel(r'Distance $(\mathrm{km})$')
ax.set_ylabel(r'Residuals $(\mathrm{cm})$')
ax.grid(True, linestyle=':', alpha=0.6, color='gray')
ax.legend(loc='upper right')
ax.set_ylim(-5, +5)
plt.tight_layout()
if save_plots: plt.savefig('output/dist_plot_blk_IIF_distance_zenit.png', format='png', bbox_inches='tight', dpi=300)
plt.show(block=False)

fig, ax = plt.subplots(figsize=(6, 4))
ax.plot(dataDPzIIF_STD[0], np.array([(np.std(v) * 100) for v in dataDPzIIF_STD[1]]), label='Zenith antenna', color='blue', linestyle='-', marker='.', markersize=3)
ax.set_xlabel(r'Distance $(\mathrm{km})$')
ax.set_ylabel(r'SD of Residuals $(\mathrm{cm})$')
ax.grid(True, linestyle=':', alpha=0.6, color='gray')
ax.legend(loc='upper right')
ax.set_ylim(0.15, +1.6)
plt.tight_layout()
if save_plots: plt.savefig('output/dist_plot_blk_IIF_distance_std_zenit.png', format='png', bbox_inches='tight', dpi=300)
plt.show(block=False)


##################################################
## Block GAL2: Distance
print(' * '.rjust(14, ' ') + 'Block GAL2: Distance')

dataDPnGAL2 = data[(data[:, 1] == 1) & (np.isin(data[:, 4], gf.gnssbl23['GAL2']))]

fig, ax = plt.subplots(figsize=(6, 4))
ax.plot(dataDPnGAL2[(dataDPnGAL2[:, 4] != 214) & (dataDPnGAL2[:, 4] != 218)][:, 12], dataDPnGAL2[(dataDPnGAL2[:, 4] != 214) & (dataDPnGAL2[:, 4] != 218)][:, 5] * 100, label='Nadir antenna', color='red', linestyle='none', marker='.', markersize=1)
ax.plot(dataDPnGAL2[dataDPnGAL2[:, 4] == 214][:, 12], dataDPnGAL2[dataDPnGAL2[:, 4] == 214][:, 5] * 100, label='Satellite E14', color='darkred', linestyle='none', marker='.', markersize=1)
ax.plot(dataDPnGAL2[dataDPnGAL2[:, 4] == 218][:, 12], dataDPnGAL2[dataDPnGAL2[:, 4] == 218][:, 5] * 100, label='Satellite E18', color='tomato', linestyle='none', marker='.', markersize=1)
ax.set_xlabel(r'Distance $(\mathrm{km})$')
ax.set_ylabel(r'Residuals $(\mathrm{cm})$')
ax.grid(True, linestyle=':', alpha=0.6, color='gray')
ax.legend(loc='upper right')
ax.set_ylim(-6, +6)
plt.tight_layout()
if save_plots: plt.savefig('output/dist_plot_blk_GAL2_distance_nadir.png', format='png', bbox_inches='tight', dpi=300)
plt.show(block=False)


dataDPzGAL2 = data[(data[:, 1] == 2) & (np.isin(data[:, 4], gf.gnssbl23['GAL2']))]

fig, ax = plt.subplots(figsize=(6, 4))
ax.plot(dataDPzGAL2[(dataDPzGAL2[:, 4] != 214) & (dataDPzGAL2[:, 4] != 218)][:, 12], dataDPzGAL2[(dataDPzGAL2[:, 4] != 214) & (dataDPzGAL2[:, 4] != 218)][:, 5] * 100, label='Zenith antenna', color='blue', linestyle='none', marker='.', markersize=1)
ax.plot(dataDPzGAL2[dataDPzGAL2[:, 4] == 214][:, 12], dataDPzGAL2[dataDPzGAL2[:, 4] == 214][:, 5] * 100, label='Satellite E14', color='darkblue', linestyle='none', marker='.', markersize=1)
ax.plot(dataDPzGAL2[dataDPzGAL2[:, 4] == 218][:, 12], dataDPzGAL2[dataDPzGAL2[:, 4] == 218][:, 5] * 100, label='Satellite E18', color='lightblue', linestyle='none', marker='.', markersize=1)
ax.set_xlabel(r'Distance $(\mathrm{km})$')
ax.set_ylabel(r'Residuals $(\mathrm{cm})$')
ax.grid(True, linestyle=':', alpha=0.6, color='gray')
ax.legend(loc='upper right')
ax.set_ylim(-6, +6)
plt.tight_layout()
if save_plots: plt.savefig('output/dist_plot_blk_GAL2_distance_zenit.png', format='png', bbox_inches='tight', dpi=300)
plt.show(block=False)


####################################################################################################
## 3D-Plots: Nadir Angle & Distance
print('\n' + ' - '.rjust(10, ' ') + '3D-Plots: Nadir Angle & Distance')

data3DP = gf.binning_2d(data, (10, 12, 5), (1, 1000))

fig, ax = plt.subplots(subplot_kw={'projection' : '3d'}, figsize=(8, 6))
ax.scatter(data3DP[1] / 1000, data3DP[0], np.array([np.std(v) if len(v) > 0 else np.nan for v in data3DP[2]]) * 100, color='blue')
ax.set_xlabel(r'Distance $(\mathrm{10^3\, km})$')
ax.set_ylabel(r'Nadir Angle $(\mathrm{°})$')
ax.set_zlabel(r'SD of Residuals $(\mathrm{cm})$')
plt.tight_layout() # plt.subplots_adjust(left=0.05, right=0.85, top=0.95, bottom=0.15)
if save_plots: plt.savefig('output/3d_plot_2d_binning.png', format='png', dpi=300) # bbox_inches='tight', 
plt.show(block=False)

fig, ax = plt.subplots(subplot_kw={'projection' : '3d'}, figsize=(8, 6))
ax.scatter(data3DP[1] / 1000, data3DP[0], np.array([np.std(v) if len(v) > 0 else np.nan for v in data3DP[2]]) * 100, color='blue')
# ax.set_xlabel(r'Distance $(\mathrm{10^3\, km})$')
ax.set_ylabel(r'Nadir Angle $(\mathrm{°})$')
ax.set_zlabel(r'SD of Residuals $(\mathrm{cm})$')
ax.set_xticks([])
ax.view_init(elev=0, azim=0)
plt.tight_layout()
if save_plots: plt.savefig('output/3d_plot_2d_binning_nadir_angle.png', format='png', bbox_inches='tight', dpi=300)
plt.show(block=False)

fig, ax = plt.subplots(subplot_kw={'projection' : '3d'}, figsize=(8, 6))
ax.scatter(data3DP[1] / 1000, data3DP[0], np.array([np.std(v) if len(v) > 0 else np.nan for v in data3DP[2]]) * 100, color='blue')
ax.set_xlabel(r'Distance $(\mathrm{10^3\, km})$')
# ax.set_ylabel(r'Nadir Angle $(\mathrm{°})$')
ax.set_zlabel(r'SD of Residuals $(\mathrm{cm})$')
ax.set_yticks([])
ax.view_init(elev=0, azim=-90)
plt.tight_layout()
if save_plots: plt.savefig('output/3d_plot_2d_binning_distance.png', format='png', bbox_inches='tight', dpi=300)
plt.show(block=False)


print()
print()
input(10 * ' ' + '  Close Plots - Press Enter  '.center(80, '-') + 10 * ' ')
print()
print()
print('####################################################################################################')
print()

